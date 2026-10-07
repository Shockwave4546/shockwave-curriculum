# Piston gateway

The one door in front of Piston. Piston runs untrusted student code and has no login of its own, so
it must never be reachable from the internet. The gateway sits between the academy's back end and
Piston:

```
browser -> back end (checks the student is logged in) -> gateway -> Piston
```

It only does four things: checks a shared secret, caps simultaneous runs, limits each student, and
forwards the code unchanged. It does **not** inspect the code (the end-of-section playground lets
students run any program). Standard library only; student code is never logged.

## The API

| | |
|---|---|
| `POST /execute` | Same JSON body as Piston's `/api/v2/execute` (the app's `codingRunner.ts` already sends it). Headers: `Authorization: Bearer <secret>` and `X-Student-Id: <id>` (the back end sets both). Answer: Piston's JSON, unchanged. |
| `GET /health` | No login. Counters only: `in_flight`, `waiting`, `max_concurrent`, `served`, `refused_busy`, `refused_student`, `failed_upstream`, `peak_in_flight`. |
| anything else | 404. Piston's package install and other admin endpoints are not reachable through it. |

Only `language`, `version`, `files`, `stdin` and `args` reach Piston, so a caller can't ask for looser
time or memory limits. Languages are limited to `GATEWAY_ALLOWED_LANGUAGES`.

| Answer | Meaning |
|---|---|
| 400 | bad request (reason in `error`) |
| 401 | missing or wrong secret |
| 413 | body over `GATEWAY_MAX_BODY_BYTES` |
| 429 | this student already has a run going, or is over the per-minute limit (`Retry-After` set) |
| 503 | all slots stayed busy for `GATEWAY_QUEUE_WAIT_SECONDS` (`Retry-After` set) |
| 502 / 504 | Piston is down / too slow |

## Settings (environment variables)

| Variable | Default | |
|---|---|---|
| `GATEWAY_SECRET` | none | **required**, at least 16 characters; the gateway refuses to start without it |
| `GATEWAY_HOST` / `GATEWAY_PORT` | `127.0.0.1` / `8090` | listen on a private address only |
| `PISTON_URL` | `http://localhost:2000` | |
| `GATEWAY_MAX_CONCURRENT` | `3` | runs at once; the rest wait up to the queue time. **Measure on the real VM** (below) |
| `GATEWAY_QUEUE_WAIT_SECONDS` | `10` | how long a request may wait for a slot |
| `GATEWAY_PER_STUDENT_CONCURRENT` | `1` | runs in flight per student (the app sends one at a time) |
| `GATEWAY_PER_STUDENT_PER_MINUTE` | `60` | one Run click on a full-program exercise sends up to 6 requests |
| `GATEWAY_MAX_BODY_BYTES` | `200000` | |
| `GATEWAY_ALLOWED_LANGUAGES` | `java,python` | |
| `GATEWAY_PISTON_TIMEOUT_SECONDS` | `20` | |

## Run it

```bash
GATEWAY_SECRET=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))") python3 tools/piston/gateway/gateway.py
python3 tools/piston/gateway/test_gateway.py        # 24 tests (also runs real Java if Piston is up)
```

On a server, use [piston-gateway.service](piston-gateway.service) (example systemd unit with the
settings in a root-only env file).

## Choosing `GATEWAY_MAX_CONCURRENT`

Piston kills a run at 3 CPU-seconds, and a Java run uses about 1.2 CPU-seconds even with the JVM
flags the installer sets. A machine with N CPUs therefore finishes about N / 1.2 runs per second, and
runs slow down as they share the CPUs. Measure instead of guessing:

```bash
# on the Piston VM, with the gateway running:
GATEWAY_SECRET=... python3 tools/piston/gateway/loadtest.py --students 8 --runs 10
GATEWAY_SECRET=... python3 tools/piston/gateway/loadtest.py --students 12 --runs 10 --think 5
```

It prints failures, how long a student waits (median and slowest), Piston's CPU time per run, and the
gateway's peak in-flight. Raise the cap while there are **no failures** and the CPU time stays well
under 3000 ms and wall time under 3 s; keep it a notch below the point where those degrade.

Measured on the dev laptop (8 cores), cap 3, real Commands v3 scheduler runs, students submitting
back to back: 0 failures in 138 runs at 3, 8 and 12 students; about 1.17 CPU-seconds per run; 3.7 runs
per second; a student waits a median of 0.8 s (3 students), 2.3 s (8) and 3.2 s (12).
