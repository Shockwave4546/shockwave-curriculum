#!/usr/bin/env python3
"""Piston gateway: the one door in front of Piston.

Piston runs untrusted student code, has no authentication of its own, and must never be
reachable from the internet. This gateway sits between the academy's back end and Piston:

    browser -> back end (checks the student's login) -> THIS GATEWAY -> Piston

It does four jobs, and deliberately nothing more:

  1. Checks a shared secret (`Authorization: Bearer <secret>`), so only the back end can use it.
  2. Caps simultaneous runs (GATEWAY_MAX_CONCURRENT) and queues the rest briefly, because Piston
     kills a run at 3 CPU-seconds and a small VM has only a couple of CPUs.
  3. Limits each student: one run at a time and N runs per minute, so one student can't hog it.
  4. Forwards the code to Piston unchanged and returns Piston's answer unchanged.

It does NOT look at what the code does. The playground planned for the end of each section lets
students run any program, so there is no "exercise-shaped" restriction. It only allows a few
request fields (language, version, files, stdin, args), so a caller can't loosen Piston's limits,
and it only exposes `POST /execute` and `GET /health`: Piston's package-install and other admin
endpoints are not reachable through it.

Standard library only. Settings come from environment variables (see Config / README.md).
Student code is never logged.

Usage:
    GATEWAY_SECRET=<long random string> python3 gateway.py
"""
import hmac
import json
import logging
import os
import re
import signal
import socket
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import deque
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

log = logging.getLogger("piston-gateway")

ALLOWED_REQUEST_KEYS = ("language", "version", "files", "stdin", "args")
STUDENT_ID = re.compile(r"^[A-Za-z0-9._@:-]{1,64}$")


def _int(name, default):
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    try:
        return int(raw)
    except ValueError:
        sys.exit(f"{name} must be a whole number, got {raw!r}")


def _float(name, default):
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    try:
        return float(raw)
    except ValueError:
        sys.exit(f"{name} must be a number, got {raw!r}")


@dataclass
class Config:
    secret: str = ""
    host: str = "127.0.0.1"                 # private by default: never 0.0.0.0 on the internet
    port: int = 8090
    piston_url: str = "http://localhost:2000"
    max_concurrent: int = 3                 # simultaneous runs sent to Piston (measure on the real VM)
    queue_wait_seconds: float = 10.0        # how long a request may wait for a free slot
    per_student_concurrent: int = 1         # runs in flight (or queued) per student
    per_student_per_minute: int = 60        # requests per student per minute
    max_body_bytes: int = 200_000
    allowed_languages: tuple = ("java", "python")
    piston_timeout_seconds: float = 20.0
    max_files: int = 10
    max_args: int = 20

    @classmethod
    def from_env(cls):
        langs = os.environ.get("GATEWAY_ALLOWED_LANGUAGES", "java,python")
        return cls(
            secret=os.environ.get("GATEWAY_SECRET", ""),
            host=os.environ.get("GATEWAY_HOST", "127.0.0.1"),
            port=_int("GATEWAY_PORT", 8090),
            piston_url=os.environ.get("PISTON_URL", "http://localhost:2000").rstrip("/"),
            max_concurrent=_int("GATEWAY_MAX_CONCURRENT", 3),
            queue_wait_seconds=_float("GATEWAY_QUEUE_WAIT_SECONDS", 10.0),
            per_student_concurrent=_int("GATEWAY_PER_STUDENT_CONCURRENT", 1),
            per_student_per_minute=_int("GATEWAY_PER_STUDENT_PER_MINUTE", 60),
            max_body_bytes=_int("GATEWAY_MAX_BODY_BYTES", 200_000),
            allowed_languages=tuple(x.strip() for x in langs.split(",") if x.strip()),
            piston_timeout_seconds=_float("GATEWAY_PISTON_TIMEOUT_SECONDS", 20.0),
        )

    def validate(self):
        problems = []
        if len(self.secret) < 16:
            problems.append("GATEWAY_SECRET must be set to a random string of at least 16 characters")
        if self.max_concurrent < 1:
            problems.append("GATEWAY_MAX_CONCURRENT must be at least 1")
        if self.per_student_concurrent < 1:
            problems.append("GATEWAY_PER_STUDENT_CONCURRENT must be at least 1")
        if self.per_student_per_minute < 1:
            problems.append("GATEWAY_PER_STUDENT_PER_MINUTE must be at least 1")
        if not self.allowed_languages:
            problems.append("GATEWAY_ALLOWED_LANGUAGES must name at least one language")
        return problems


class Refused(Exception):
    """A request the limiter turned away."""

    def __init__(self, status, message, retry_after=None):
        super().__init__(message)
        self.status = status
        self.message = message
        self.retry_after = retry_after


@dataclass
class Stats:
    served: int = 0
    refused_busy: int = 0
    refused_student: int = 0
    failed_upstream: int = 0
    peak_in_flight: int = 0


class Limiter:
    """Global slot cap + per-student concurrency and rate limits. Thread-safe."""

    def __init__(self, cfg, clock=time.monotonic):
        self.cfg = cfg
        self.clock = clock
        self._slots = threading.Semaphore(cfg.max_concurrent)
        self._lock = threading.Lock()
        self._student_active = {}          # student -> requests holding or waiting for a slot
        self._student_recent = {}          # student -> deque of request times (last minute)
        self._in_flight = 0
        self._waiting = 0
        self.stats = Stats()

    @property
    def in_flight(self):
        with self._lock:
            return self._in_flight

    @property
    def waiting(self):
        with self._lock:
            return self._waiting

    def acquire(self, student):
        """Returns when a run slot is held; raises Refused otherwise. Pair with release()."""
        now = self.clock()
        with self._lock:
            if len(self._student_recent) > 1000:      # forget students idle for over a minute
                for s in [s for s, r in self._student_recent.items()
                          if (not r or now - r[-1] > 60) and s not in self._student_active]:
                    del self._student_recent[s]
            recent = self._student_recent.setdefault(student, deque())
            while recent and now - recent[0] > 60:
                recent.popleft()
            if len(recent) >= self.cfg.per_student_per_minute:
                self.stats.refused_student += 1
                wait = max(1, int(60 - (now - recent[0])) + 1)
                raise Refused(429, "Too many runs this minute. Wait a moment and try again.", wait)
            if self._student_active.get(student, 0) >= self.cfg.per_student_concurrent:
                self.stats.refused_student += 1
                raise Refused(429, "You already have a run in progress. Wait for it to finish.", 1)
            recent.append(now)
            self._student_active[student] = self._student_active.get(student, 0) + 1
            self._waiting += 1
        got = self._slots.acquire(timeout=self.cfg.queue_wait_seconds)
        with self._lock:
            self._waiting -= 1
            if not got:
                self._forget_student(student)
                self.stats.refused_busy += 1
                raise Refused(503, "The code runner is busy right now. Try again in a few seconds.", 5)
            self._in_flight += 1
            self.stats.peak_in_flight = max(self.stats.peak_in_flight, self._in_flight)

    def record(self, ok):
        with self._lock:
            if ok:
                self.stats.served += 1
            else:
                self.stats.failed_upstream += 1

    def release(self, student):
        with self._lock:
            self._in_flight -= 1
            self._forget_student(student)
        self._slots.release()

    def _forget_student(self, student):
        n = self._student_active.get(student, 0) - 1
        if n <= 0:
            self._student_active.pop(student, None)
            if not self._student_recent.get(student):
                self._student_recent.pop(student, None)
        else:
            self._student_active[student] = n


class Gateway(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, cfg, clock=time.monotonic):
        self.cfg = cfg
        self.limiter = Limiter(cfg, clock)
        self._secret = cfg.secret.encode()
        super().__init__((cfg.host, cfg.port), Handler)


class Handler(BaseHTTPRequestHandler):
    server_version = "PistonGateway/1.0"
    server: Gateway
    timeout = 30        # a client that stalls mid-request is dropped after 30 s

    def log_message(self, fmt, *args):  # we log one line per request ourselves
        pass

    # ---- plumbing ---------------------------------------------------------------
    def _send(self, status, body, retry_after=None):
        data = json.dumps(body).encode() if not isinstance(body, bytes) else body
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        if retry_after is not None:
            self.send_header("Retry-After", str(retry_after))
        self.end_headers()
        self.wfile.write(data)

    def _error(self, status, message, retry_after=None):
        self._send(status, {"error": message}, retry_after)

    def _authorized(self):
        header = self.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return False
        return hmac.compare_digest(header[7:].encode(), self.server._secret)

    # ---- routes -----------------------------------------------------------------
    def do_GET(self):
        if self.path == "/health":
            lim = self.server.limiter
            self._send(200, {
                "ok": True,
                "in_flight": lim.in_flight,
                "waiting": lim.waiting,
                "max_concurrent": self.server.cfg.max_concurrent,
                "served": lim.stats.served,
                "refused_busy": lim.stats.refused_busy,
                "refused_student": lim.stats.refused_student,
                "failed_upstream": lim.stats.failed_upstream,
                "peak_in_flight": lim.stats.peak_in_flight,
            })
        else:
            self._error(404, "Not found")

    def do_POST(self):
        if self.path != "/execute":
            self._error(404, "Not found")
            return
        if not self._authorized():
            self._error(401, "Missing or wrong gateway secret")
            return
        student = self.headers.get("X-Student-Id", "")
        if not STUDENT_ID.match(student):
            self._error(400, "X-Student-Id header is required (letters, digits, . _ @ : -; max 64)")
            return
        try:
            length = int(self.headers.get("Content-Length", ""))
        except ValueError:
            self._error(411, "Content-Length is required")
            return
        if length < 0 or length > self.server.cfg.max_body_bytes:
            self._error(413, f"Request is too large (limit {self.server.cfg.max_body_bytes} bytes)")
            return
        raw = self.rfile.read(length)
        try:
            request = self._validate(raw)
        except ValueError as e:
            self._error(400, str(e))
            return

        lim = self.server.limiter
        started = time.monotonic()
        try:
            lim.acquire(student)
        except Refused as r:
            log.info("student=%s lang=%s status=%d refused", student, request["language"], r.status)
            self._error(r.status, r.message, r.retry_after)
            return
        try:
            status, body = self._forward(request)
        finally:
            lim.release(student)
        lim.record(status == 200)
        log.info("student=%s lang=%s status=%d ms=%d", student, request["language"], status,
                 (time.monotonic() - started) * 1000)
        self._send(status, body)

    # ---- request handling -------------------------------------------------------
    def _validate(self, raw):
        """Parses the body and keeps only the allowed fields. Raises ValueError with a student-safe message."""
        cfg = self.server.cfg
        try:
            req = json.loads(raw)
        except (ValueError, UnicodeDecodeError):
            raise ValueError("Body must be JSON")
        if not isinstance(req, dict):
            raise ValueError("Body must be a JSON object")
        language = req.get("language")
        if language not in cfg.allowed_languages:
            raise ValueError(f"language must be one of: {', '.join(cfg.allowed_languages)}")
        files = req.get("files")
        if not isinstance(files, list) or not files or len(files) > cfg.max_files:
            raise ValueError(f"files must be a list of 1 to {cfg.max_files} files")
        for f in files:
            if not isinstance(f, dict) or not isinstance(f.get("content"), str):
                raise ValueError("every file needs a text 'content'")
            if "name" in f and not isinstance(f["name"], str):
                raise ValueError("a file's 'name' must be text")
        for key in ("version", "stdin"):
            if key in req and not isinstance(req[key], str):
                raise ValueError(f"{key} must be text")
        if "args" in req and (not isinstance(req["args"], list) or len(req["args"]) > cfg.max_args
                              or not all(isinstance(a, str) for a in req["args"])):
            raise ValueError(f"args must be a list of at most {cfg.max_args} strings")
        # Only these fields reach Piston, so a caller can't ask for looser time or memory limits.
        clean = {k: req[k] for k in ALLOWED_REQUEST_KEYS if k in req}
        clean["files"] = [{k: f[k] for k in ("name", "content") if k in f} for f in files]
        return clean

    def _forward(self, request):
        cfg = self.server.cfg
        data = json.dumps(request).encode()
        req = urllib.request.Request(
            cfg.piston_url + "/api/v2/execute", data=data, method="POST",
            headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=cfg.piston_timeout_seconds) as resp:
                return 200, resp.read()
        except urllib.error.HTTPError as e:
            # Piston said no (for example an unknown language version): tell the caller why.
            detail = ""
            try:
                detail = json.loads(e.read()).get("message", "")
            except Exception:
                pass
            if 400 <= e.code < 500:
                return 400, {"error": detail or "Piston rejected the request"}
            return 502, {"error": "The code runner had an internal error"}
        except (socket.timeout, TimeoutError):
            return 504, {"error": "The code runner took too long to answer"}
        except (urllib.error.URLError, ConnectionError, OSError):
            return 502, {"error": "The code runner is not available"}


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    cfg = Config.from_env()
    problems = cfg.validate()
    if problems:
        sys.exit("Cannot start:\n  " + "\n  ".join(problems))
    server = Gateway(cfg)
    log.info("listening on %s:%d -> %s (max %d at once, queue wait %.0fs, per student: %d at once, %d/min)",
             cfg.host, server.server_address[1], cfg.piston_url, cfg.max_concurrent,
             cfg.queue_wait_seconds, cfg.per_student_concurrent, cfg.per_student_per_minute)
    signal.signal(signal.SIGTERM, lambda *_: threading.Thread(target=server.shutdown).start())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
