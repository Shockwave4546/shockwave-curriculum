#!/usr/bin/env python3
"""Load test for the gateway (or for Piston directly): many "students" run a real exercise at once.

Use it to find the right GATEWAY_MAX_CONCURRENT for a machine: raise --students until runs start
failing or the wait gets long, then set the cap a little below that. Standard library only.

  # through a gateway (needs its secret):
  GATEWAY_SECRET=... python3 loadtest.py --url http://127.0.0.1:8090 --students 8 --runs 10
  # straight at Piston, no limits (shows what the machine can take):
  python3 loadtest.py --url http://localhost:2000 --direct --students 8 --runs 10

By default it runs the model solution of Ch.25 exercise 25.5 (the heaviest kind: the real Commands v3
scheduler). Use --exercise FILE.md --scenario N to test another exercise, or --hello for a tiny one.
"""
import argparse
import glob
import json
import os
import statistics
import sys
import threading
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))          # tools/ (for verify_coding_exercises)
import verify_coding_exercises as v                          # noqa: E402

HELLO = {"language": "java", "version": "25.0.1", "files": [{"name": "Main", "content":
         'public class Main { public static void main(String[] a) { System.out.println("hi"); } }'}]}


def load_request(args):
    if args.hello:
        return HELLO
    path = args.exercise or glob.glob(os.path.join(HERE, "..", "..", "..", "exercises", "ch25-*", "25.5-*.md"))[0]
    section = v.coding_section(open(path, encoding="utf-8").read())
    solution = v.code_after(section, "Solution:")
    scenario = v.scenarios(section)[args.scenario - 1]
    return {"language": "java", "version": "25.0.1", "files": [{"name": "Main", "content": solution}],
            "stdin": scenario["stdin"]}


def one_run(args, body, student, results):
    url = args.url.rstrip("/") + ("/api/v2/execute" if args.direct else "/execute")
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST")
    req.add_header("Content-Type", "application/json")
    if not args.direct:
        req.add_header("Authorization", "Bearer " + os.environ.get("GATEWAY_SECRET", ""))
        req.add_header("X-Student-Id", student)
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
            run = data.get("run", {})
            ok = run.get("code") == 0 and not run.get("signal") and not run.get("status")
            results.append(("ok" if ok else f"piston:{run.get('status') or run.get('code')}", time.monotonic() - t0, run.get("cpu_time"), run.get("wall_time")))
    except urllib.error.HTTPError as e:
        results.append((f"http {e.code}", time.monotonic() - t0, None, None))
        e.close()
    except Exception as e:                                      # noqa: BLE001
        results.append((f"error {type(e).__name__}", time.monotonic() - t0, None, None))


def student(args, body, k, results):
    for _ in range(args.runs):
        one_run(args, body, f"load-{k}", results)
        if args.think:
            time.sleep(args.think)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", default="http://127.0.0.1:8090")
    ap.add_argument("--direct", action="store_true", help="talk to Piston itself (no gateway, no secret)")
    ap.add_argument("--students", type=int, default=8)
    ap.add_argument("--runs", type=int, default=5, help="runs per student, one after another")
    ap.add_argument("--think", type=float, default=0.0, help="seconds each student waits between runs")
    ap.add_argument("--exercise")
    ap.add_argument("--scenario", type=int, default=3)
    ap.add_argument("--hello", action="store_true")
    args = ap.parse_args()
    body = load_request(args)
    results = []
    threads = [threading.Thread(target=student, args=(args, body, k, results)) for k in range(args.students)]
    t0 = time.monotonic()
    [t.start() for t in threads]
    [t.join() for t in threads]
    total = time.monotonic() - t0
    counts = {}
    for r in results:
        counts[r[0]] = counts.get(r[0], 0) + 1
    lat = sorted(r[1] for r in results)
    cpu = [r[2] for r in results if r[2]]
    print(f"{args.students} students x {args.runs} runs = {len(results)} requests in {total:.1f}s ({len(results) / total:.1f} runs/s)")
    print("results:", ", ".join(f"{k}: {n}" for k, n in sorted(counts.items())))
    print(f"latency s (what a student waits): min {lat[0]:.2f}  median {statistics.median(lat):.2f}  p95 {lat[int(len(lat) * 0.95) - 1]:.2f}  max {lat[-1]:.2f}")
    if cpu:
        print(f"Piston cpu_time ms per run: avg {sum(cpu) // len(cpu)}  max {max(cpu)}  (limit 3000)")
    if not args.direct:
        try:
            with urllib.request.urlopen(args.url.rstrip("/") + "/health", timeout=5) as r:
                h = json.load(r)
            print(f"gateway: cap {h['max_concurrent']}, peak in flight {h['peak_in_flight']}, served {h['served']}, "
                  f"refused busy {h['refused_busy']}, refused per-student {h['refused_student']}")
        except Exception as e:                                  # noqa: BLE001
            print("gateway /health not reachable:", e)
    sys.exit(0 if list(counts) == ["ok"] else 1)


if __name__ == "__main__":
    main()
