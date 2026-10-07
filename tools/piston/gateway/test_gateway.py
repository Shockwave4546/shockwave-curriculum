#!/usr/bin/env python3
"""Tests for gateway.py. Standard library only.

    python3 tools/piston/gateway/test_gateway.py          # unit tests (a fake Piston is started)
    PISTON_URL=http://localhost:2000 python3 ... test_gateway.py   # also runs the live check

The unit tests use a fake Piston so every rule can be checked: the secret, the field allow-list,
the cap on simultaneous runs, the per-student limits, and error handling. One extra test runs a real
Java program through the gateway when a real Piston answers on PISTON_URL (default localhost:2000).
"""
import json
import logging
import os
import threading
import time
import unittest
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import gateway

SECRET = "test-secret-0123456789abcdef"


class FakePiston:
    """Records every request, and holds each run for `delay` seconds like a real run would."""

    def __init__(self, delay=0.0, status=200, body=None):
        self.delay, self.status, self.body = delay, status, body
        self.requests = []
        self.paths = []
        self.in_flight = 0
        self.peak = 0
        self.lock = threading.Lock()
        outer = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                with outer.lock:
                    outer.requests.append(body)
                    outer.paths.append(self.path)
                    outer.in_flight += 1
                    outer.peak = max(outer.peak, outer.in_flight)
                time.sleep(outer.delay)
                with outer.lock:
                    outer.in_flight -= 1
                out = json.dumps(outer.body or {"language": "java", "run": {"stdout": "hi\n", "code": 0}}).encode()
                self.send_response(outer.status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(out)))
                self.end_headers()
                try:
                    self.wfile.write(out)
                except BrokenPipeError:     # the gateway gave up waiting (the 504 test)
                    pass

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.server.daemon_threads = True
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()


def start_gateway(piston_url, **overrides):
    cfg = gateway.Config(secret=SECRET, port=0, piston_url=piston_url, **overrides)
    gw = gateway.Gateway(cfg)
    threading.Thread(target=gw.serve_forever, daemon=True).start()
    return gw, f"http://127.0.0.1:{gw.server_address[1]}"


def call(base, method="POST", path="/execute", body=None, secret=SECRET, student="s1", raw=None, headers=None):
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    req = urllib.request.Request(base + path, data=data, method=method)
    if secret is not None:
        req.add_header("Authorization", "Bearer " + secret)
    if student is not None:
        req.add_header("X-Student-Id", student)
    req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read() or b"{}"), dict(r.headers)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read() or b"{}"), dict(e.headers)
        finally:
            e.close()


GOOD = {"language": "java", "version": "25.0.1", "files": [{"name": "Main", "content": "class Main {}"}]}


class GatewayTests(unittest.TestCase):
    def setUp(self):
        self.piston = FakePiston()
        self.servers = []

    def tearDown(self):
        for gw in self.servers:
            gw.shutdown()
            gw.server_close()
        self.piston.stop()

    def gateway(self, **overrides):
        url = overrides.pop("piston_url", self.piston.url)
        gw, base = start_gateway(url, **overrides)
        self.servers.append(gw)
        return base

    # ---- access ----
    def test_health_needs_no_secret_and_reveals_no_secret(self):
        base = self.gateway()
        status, body, _ = call(base, "GET", "/health", secret=None, student=None)
        self.assertEqual(status, 200)
        self.assertTrue(body["ok"])
        self.assertEqual(body["max_concurrent"], 3)
        self.assertNotIn(SECRET, json.dumps(body))

    def test_wrong_or_missing_secret_is_refused(self):
        base = self.gateway()
        for secret in (None, "", "nope", SECRET + "x", SECRET[:-1]):
            status, _, _ = call(base, body=GOOD, secret=secret)
            self.assertEqual(status, 401, secret)
        self.assertEqual(self.piston.requests, [])

    def test_right_secret_forwards_and_returns_pistons_answer_unchanged(self):
        base = self.gateway()
        status, body, _ = call(base, body=GOOD)
        self.assertEqual(status, 200)
        self.assertEqual(body, {"language": "java", "run": {"stdout": "hi\n", "code": 0}})
        self.assertEqual(self.piston.paths, ["/api/v2/execute"])

    def test_student_id_is_required_and_checked(self):
        base = self.gateway()
        for student in (None, "", "a b", "x" * 65, "bad/char"):
            status, _, _ = call(base, body=GOOD, student=student)
            self.assertEqual(status, 400, student)

    def test_only_execute_is_exposed(self):
        base = self.gateway()
        for method, path in (("POST", "/packages"), ("POST", "/api/v2/packages"), ("POST", "/api/v2/execute"),
                             ("GET", "/runtimes"), ("GET", "/execute"), ("POST", "/")):
            status, _, _ = call(base, method, path, body=GOOD if method == "POST" else None)
            self.assertEqual(status, 404, (method, path))
        self.assertEqual(self.piston.requests, [])

    # ---- request checking ----
    def test_only_allowed_fields_reach_piston(self):
        base = self.gateway()
        sneaky = dict(GOOD, run_timeout=999999, compile_timeout=999999, run_memory_limit=-1,
                      run_cpu_time=999999, stdin="3\n", args=["a"])
        sneaky["files"] = [{"name": "Main", "content": "x", "encoding": "hex"}]
        status, _, _ = call(base, body=sneaky)
        self.assertEqual(status, 200)
        sent = self.piston.requests[0]
        self.assertEqual(set(sent), {"language", "version", "files", "stdin", "args"})
        self.assertEqual(sent["files"], [{"name": "Main", "content": "x"}])

    def test_bad_requests_are_refused_before_piston(self):
        base = self.gateway()
        cases = [
            dict(raw=b"not json"), dict(raw=b"[1,2]"),
            dict(body=dict(GOOD, language="bash")), dict(body={k: v for k, v in GOOD.items() if k != "language"}),
            dict(body=dict(GOOD, files=[])), dict(body=dict(GOOD, files="x")),
            dict(body=dict(GOOD, files=[{"name": "Main"}])), dict(body=dict(GOOD, files=[{"content": 5}])),
            dict(body=dict(GOOD, stdin=5)), dict(body=dict(GOOD, args="x")), dict(body=dict(GOOD, args=[1])),
            dict(body=dict(GOOD, files=[{"content": "x"}] * 11)),
        ]
        for case in cases:
            status, body, _ = call(base, **case)
            self.assertEqual(status, 400, case)
            self.assertIn("error", body)
        self.assertEqual(self.piston.requests, [])

    def test_oversized_body_is_refused(self):
        base = self.gateway(max_body_bytes=500)
        status, _, _ = call(base, body=dict(GOOD, files=[{"content": "x" * 1000}]))
        self.assertEqual(status, 413)
        self.assertEqual(self.piston.requests, [])

    # ---- the caps ----
    def test_never_more_than_the_cap_run_at_once_and_everyone_still_gets_served(self):
        self.piston.delay = 0.25
        base = self.gateway(max_concurrent=2, queue_wait_seconds=10)
        results = []
        threads = [threading.Thread(target=lambda i=i: results.append(call(base, body=GOOD, student=f"s{i}")[0]))
                   for i in range(8)]
        [t.start() for t in threads]
        [t.join() for t in threads]
        self.assertEqual(results, [200] * 8)
        self.assertEqual(self.piston.peak, 2)

    def test_cap_is_a_setting(self):
        self.piston.delay = 0.2
        base = self.gateway(max_concurrent=5, queue_wait_seconds=10)
        threads = [threading.Thread(target=lambda i=i: call(base, body=GOOD, student=f"s{i}")) for i in range(10)]
        [t.start() for t in threads]
        [t.join() for t in threads]
        self.assertEqual(self.piston.peak, 5)

    def test_busy_gateway_says_try_again_after_the_queue_wait(self):
        self.piston.delay = 0.8
        base = self.gateway(max_concurrent=1, queue_wait_seconds=0.2)
        first = []
        t = threading.Thread(target=lambda: first.append(call(base, body=GOOD, student="a")[0]))
        t.start()
        time.sleep(0.15)
        status, body, headers = call(base, body=GOOD, student="b")
        t.join()
        self.assertEqual(status, 503)
        self.assertIn("busy", body["error"])
        self.assertIn("Retry-After", headers)
        self.assertEqual(first, [200])

    def test_one_run_at_a_time_per_student(self):
        self.piston.delay = 0.5
        base = self.gateway(max_concurrent=3)
        first = []
        t = threading.Thread(target=lambda: first.append(call(base, body=GOOD, student="same")[0]))
        t.start()
        time.sleep(0.15)
        status, _, headers = call(base, body=GOOD, student="same")
        other, _, _ = call(base, body=GOOD, student="someone-else")
        t.join()
        self.assertEqual(status, 429)
        self.assertIn("Retry-After", headers)
        self.assertEqual(other, 200)
        self.assertEqual(first, [200])

    def test_per_student_runs_per_minute(self):
        base = self.gateway(per_student_per_minute=3)
        codes = [call(base, body=GOOD, student="busy")[0] for _ in range(5)]
        self.assertEqual(codes, [200, 200, 200, 429, 429])
        self.assertEqual(call(base, body=GOOD, student="fresh")[0], 200)

    def test_rate_limit_window_slides(self):
        now = [0.0]
        cfg = gateway.Config(secret=SECRET, port=0, piston_url=self.piston.url, per_student_per_minute=2)
        lim = gateway.Limiter(cfg, clock=lambda: now[0])
        for _ in range(2):
            lim.acquire("s")
            lim.release("s")
        with self.assertRaises(gateway.Refused):
            lim.acquire("s")
        now[0] = 61.0
        lim.acquire("s")
        lim.release("s")

    def test_slot_is_freed_after_each_request(self):
        base = self.gateway(max_concurrent=1, per_student_per_minute=100)
        for _ in range(5):
            self.assertEqual(call(base, body=GOOD)[0], 200)
        _, health, _ = call(base, "GET", "/health", secret=None, student=None)
        self.assertEqual((health["in_flight"], health["waiting"], health["served"]), (0, 0, 5))

    # ---- when Piston misbehaves ----
    def test_piston_down_is_a_502(self):
        base = self.gateway(piston_url="http://127.0.0.1:1")
        status, body, _ = call(base, body=GOOD)
        self.assertEqual(status, 502)
        self.assertIn("not available", body["error"])
        _, health, _ = call(base, "GET", "/health", secret=None, student=None)
        self.assertEqual(health["in_flight"], 0)

    def test_piston_rejecting_the_request_is_a_400_with_its_reason(self):
        self.piston.status, self.piston.body = 400, {"message": "java-9 runtime is unknown"}
        base = self.gateway()
        status, body, _ = call(base, body=GOOD)
        self.assertEqual((status, body), (400, {"error": "java-9 runtime is unknown"}))

    def test_piston_internal_error_is_a_502(self):
        self.piston.status = 500
        base = self.gateway()
        self.assertEqual(call(base, body=GOOD)[0], 502)

    def test_slow_piston_is_a_504(self):
        self.piston.delay = 1.0
        base = self.gateway(piston_timeout_seconds=0.3)
        self.assertEqual(call(base, body=GOOD)[0], 504)

    # ---- privacy ----
    def test_student_code_is_never_logged(self):
        records = []

        class Grab(logging.Handler):
            def emit(self, record):
                records.append(record.getMessage())

        handler = Grab()
        logging.getLogger("piston-gateway").addHandler(handler)
        logging.getLogger("piston-gateway").setLevel(logging.INFO)
        try:
            base = self.gateway()
            call(base, body=dict(GOOD, files=[{"content": "SECRET_STUDENT_CODE_42"}], stdin="PRIVATE_INPUT"))
            call(base, body=GOOD, secret="wrong")
        finally:
            logging.getLogger("piston-gateway").removeHandler(handler)
        text = "\n".join(records)
        self.assertIn("student=s1", text)
        self.assertNotIn("SECRET_STUDENT_CODE_42", text)
        self.assertNotIn("PRIVATE_INPUT", text)
        self.assertNotIn(SECRET, text)


class ConfigTests(unittest.TestCase):
    def test_refuses_to_start_without_a_real_secret(self):
        self.assertTrue(gateway.Config(secret="").validate())
        self.assertTrue(gateway.Config(secret="short").validate())
        self.assertEqual(gateway.Config(secret="x" * 16).validate(), [])

    def test_bad_numbers_are_caught(self):
        self.assertTrue(gateway.Config(secret="x" * 16, max_concurrent=0).validate())
        self.assertTrue(gateway.Config(secret="x" * 16, per_student_per_minute=0).validate())

    def test_defaults_are_private_and_cautious(self):
        cfg = gateway.Config()
        self.assertEqual((cfg.host, cfg.max_concurrent, cfg.per_student_concurrent), ("127.0.0.1", 3, 1))


@unittest.skipUnless(os.environ.get("PISTON_LIVE", "1") == "1", "live check disabled")
class LivePistonTest(unittest.TestCase):
    """Runs real Java through the gateway when a real Piston answers."""

    def test_hello_world_and_a_crash_through_the_gateway(self):
        url = os.environ.get("PISTON_URL", "http://localhost:2000")
        try:
            urllib.request.urlopen(url + "/api/v2/runtimes", timeout=3).read()
        except Exception:
            self.skipTest("no live Piston at " + url)
        gw, base = start_gateway(url, max_concurrent=2)
        try:
            ok = {"language": "java", "version": "25.0.1", "files": [{"name": "Main", "content":
                  'public class Main { public static void main(String[] a) { System.out.println("hello " + new java.util.Scanner(System.in).next()); } }'}],
                  "stdin": "gateway\n"}
            status, body, _ = call(base, body=ok)
            self.assertEqual(status, 200)
            self.assertEqual(body["run"]["stdout"], "hello gateway\n")
            bad = {"language": "java", "version": "25.0.1", "files": [{"name": "Main", "content": "public class Main { oops }"}]}
            status, body, _ = call(base, body=bad)
            self.assertEqual(status, 200)               # a compile error is still a normal Piston answer
            self.assertNotEqual(body["run"]["code"], 0)
            self.assertIn("error", body["run"]["stderr"])
        finally:
            gw.shutdown()
            gw.server_close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
