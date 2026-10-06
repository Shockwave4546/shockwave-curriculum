#!/usr/bin/env python3
"""Verify the `## Coding` sections of exercise files against a running Piston.

For every exercise file given (or every file under exercises/ with a `## Coding`
section), this:
  - checks the section has the fields its mode needs (see
    docs/exercise-authoring-conventions.md, "Coding exercises"),
  - runs the file's **Solution:** against every test/scenario on Piston and
    reports pass/fail,
  - with --solution-file, runs a different (e.g. deliberately wrong) solution
    instead, so an author can prove the hidden tests catch a realistic mistake.

The harness test runner built here must stay identical in behaviour to the
academy app's app/utils/codingRunner.ts (same Supplier-per-test, deepEquals,
@@TEST output lines), or a test could pass here and fail in the app.

Standard library only. Needs Piston on localhost:2000 (`sudo podman start piston_api`).

Usage:
  python3 tools/verify_coding_exercises.py                      # all files with ## Coding
  python3 tools/verify_coding_exercises.py exercises/ch10-*/10.3-*.md
  python3 tools/verify_coding_exercises.py FILE --solution-file wrong.java
"""
import argparse
import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request

PISTON = os.environ.get("PISTON_URL", "http://localhost:2000/api/v2/execute")
JAVA_VERSION = "25.0.1"
MARK = "@@TEST"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------- parsing ----------------------------------------------------------

def coding_section(text):
    """The text from '## Coding' to the next '## ' heading (or the end)."""
    m = re.search(r"^## Coding[ \t]*$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def label_value(section, label):
    m = re.search(r"^\*\*" + re.escape(label) + r"\*\*[ \t]*(.*)$", section, re.M)
    return m.group(1).strip() if m else None


def code_after(section, label):
    """Content of the first fenced block after a **Label:** line."""
    m = re.search(r"^\*\*" + re.escape(label) + r"\*\*.*$", section, re.M)
    if not m:
        return None
    f = re.search(r"^```[a-zA-Z]*[ \t]*\n(.*?)^```[ \t]*$", section[m.end():], re.M | re.S)
    return f.group(1) if f else None


def strip_code(cell):
    cell = cell.strip()
    if cell.startswith("`") and cell.endswith("`"):
        cell = cell.strip("`").strip()
    return cell


def harness_tests(section):
    m = re.search(r"^\*\*Tests:\*\*", section, re.M)
    if not m:
        return None
    tests = []
    for line in section[m.end():].splitlines():
        line = line.strip()
        if not line.startswith("|"):
            if tests:
                break
            continue
        cells = [c for c in line.strip("|").split("|")]
        if len(cells) < 3 or set(cells[0].strip()) <= set("-: "):
            continue
        vis = cells[0].strip().lower()
        if vis not in ("yes", "no"):
            continue  # header row
        tests.append({"visible": vis == "yes", "args": strip_code(cells[1]), "expected": strip_code("|".join(cells[2:]))})
    return tests


def scenarios(section):
    """**Scenario N (visible|hidden):** blocks, each with optional **Input:**
    and required **Expected output:** fenced blocks."""
    out = []
    heads = list(re.finditer(r"^\*\*Scenario (\d+) \((visible|hidden)\):\*\*.*$", section, re.M))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(section)
        block = section[h.start():end]
        out.append({
            "n": int(h.group(1)),
            "visible": h.group(2) == "visible",
            "stdin": code_after(block, "Input:") or "",
            "expected": code_after(block, "Expected output:"),
        })
    return out


# ---------- running ----------------------------------------------------------

def build_runner(method, tests):
    calls = "\n".join(
        f"        check({i + 1}, () -> Solution.{method}({t['args']}), {t['expected']});"
        for i, t in enumerate(tests)
    )
    return f"""import java.util.function.Supplier;

public class Main
{{
    static String show(Object o)
    {{
        if (o == null) return "null";
        if (o.getClass().isArray())
        {{
            String s = java.util.Arrays.deepToString(new Object[] {{ o }});
            return s.substring(1, s.length() - 1);
        }}
        return String.valueOf(o);
    }}

    static void check(int n, Supplier<Object> call, Object expected)
    {{
        String result;
        try
        {{
            Object actual = call.get();
            boolean ok = java.util.Objects.deepEquals(actual, expected);
            result = (ok ? "PASS" : "FAIL") + "\\t" + show(actual);
        }}
        catch (Throwable t)
        {{
            result = "FAIL\\tthrew " + t.getClass().getSimpleName();
        }}
        System.out.println("{MARK}\\t" + n + "\\t" + result);
    }}

    public static void main(String[] args)
    {{
{calls}
    }}
}}
"""


def piston(files, stdin=""):
    # Piston's Java package renames the FIRST file by appending ".java";
    # callers pass the first file's name without an extension.
    body = {"language": "java", "version": JAVA_VERSION, "files": files, "stdin": stdin}
    req = urllib.request.Request(PISTON, json.dumps(body).encode(), {"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)["run"]
    except urllib.error.URLError as e:
        sys.exit(f"Can't reach Piston at {PISTON} ({e}). Start it: sudo podman start piston_api")


def normalize(out):
    """Trailing whitespace on each line and trailing blank lines are ignored."""
    return "\n".join(line.rstrip() for line in (out or "").splitlines()).rstrip("\n")


# ---------- checks -----------------------------------------------------------

def check_file(path, solution_override=None):
    text = open(path, encoding="utf-8").read()
    section = coding_section(text)
    rel = os.path.relpath(path, ROOT)
    if section is None:
        return rel, ["no ## Coding section"], []
    problems, lines = [], []
    mode = label_value(section, "Mode:")
    for label in ("Mode:", "Problem:", "Starter:", "Solution:", "Why:"):
        if label_value(section, label) is None:
            problems.append(f"missing **{label}**")
    starter = code_after(section, "Starter:")
    solution = solution_override if solution_override is not None else code_after(section, "Solution:")
    if starter is None:
        problems.append("**Starter:** has no ```java block")
    if not solution:
        problems.append("**Solution:** has no ```java block")
    if problems:
        return rel, problems, lines

    if mode == "harness":
        sig = label_value(section, "Signature:") or ""
        mm = re.search(r"(\w+)\s*\(", sig)
        tests = harness_tests(section) or []
        if not mm:
            problems.append("missing/unreadable **Signature:**")
        if not tests:
            problems.append("no rows in the **Tests:** table")
        if problems:
            return rel, problems, lines
        vis = sum(t["visible"] for t in tests)
        hid = len(tests) - vis
        if not 2 <= vis <= 3:
            problems.append(f"{vis} visible tests (want 2-3)")
        if hid < 2:
            problems.append(f"{hid} hidden tests (want at least 2)")
        run = piston([{"name": "Main", "content": build_runner(mm.group(1), tests)},
                      {"name": "Solution.java", "content": solution}])
        got = {}
        for ln in (run.get("stdout") or "").splitlines():
            if ln.startswith(MARK + "\t"):
                _, n, verdict, *rest = ln.split("\t")
                got[int(n)] = (verdict == "PASS", "\t".join(rest))
        if not got:
            problems.append("did not compile/run:\n" + (run.get("stderr") or run.get("output") or "")[:1500])
        for i, t in enumerate(tests, 1):
            ok, actual = got.get(i, (False, "(did not run)"))
            tag = "visible" if t["visible"] else "hidden "
            lines.append(f"  {'PASS' if ok else 'FAIL'} {tag} #{i}: expected {t['expected']}, got {actual}")
            if not ok:
                problems.append(f"test #{i} fails")
    elif mode == "full-program":
        scs = scenarios(section)
        if not scs:
            problems.append("no **Scenario N (visible|hidden):** blocks")
            return rel, problems, lines
        vis = sum(s["visible"] for s in scs)
        if not 2 <= vis <= 3:
            problems.append(f"{vis} visible scenarios (want 2-3)")
        if len(scs) - vis < 2:
            problems.append(f"{len(scs) - vis} hidden scenarios (want at least 2)")
        for s in scs:
            if s["expected"] is None:
                problems.append(f"scenario {s['n']} has no **Expected output:** block")
                continue
            run = piston([{"name": "Main", "content": solution}], s["stdin"])
            ok = run.get("code") == 0 and normalize(run.get("stdout")) == normalize(s["expected"])
            tag = "visible" if s["visible"] else "hidden "
            lines.append(f"  {'PASS' if ok else 'FAIL'} {tag} scenario {s['n']}")
            if not ok:
                detail = (run.get("stderr") or "")[:800] or f"expected:\n{s['expected']}\ngot:\n{run.get('stdout')}"
                problems.append(f"scenario {s['n']} fails:\n{detail}")
    elif mode == "compile-only":
        problems.append("compile-only mode isn't supported by this script yet (needs WPILib jars in Piston)")
    else:
        problems.append(f"unknown **Mode:** {mode!r} (harness | full-program | compile-only)")
    return rel, problems, lines


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--solution-file", help="run this solution instead of the file's **Solution:** (one exercise file only)")
    a = ap.parse_args()
    files = a.files or sorted(
        f for f in glob.glob(os.path.join(ROOT, "exercises", "*", "*.md"))
        if coding_section(open(f, encoding="utf-8").read()) is not None
    )
    if a.solution_file and len(files) != 1:
        sys.exit("--solution-file needs exactly one exercise file")
    override = open(a.solution_file, encoding="utf-8").read() if a.solution_file else None
    failed = 0
    for f in files:
        rel, problems, lines = check_file(f, override)
        print(("OK   " if not problems else "FAIL ") + rel)
        for ln in lines:
            print(ln)
        for p in problems:
            print("  problem: " + p)
        failed += bool(problems)
    print(f"\n{len(files) - failed}/{len(files)} files OK")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
