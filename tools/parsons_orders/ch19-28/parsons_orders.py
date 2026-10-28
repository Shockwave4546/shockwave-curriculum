#!/usr/bin/env python3
"""Exhaustive correct-order search + verification for Micro-Parsons questions (chapters 19-28).

usage:
  python3 parsons_orders.py search [--write] [file-substring ...]   find every correct order (optionally write **Also accepted:**)
  python3 parsons_orders.py check  [file-substring ...]             re-verify the files as written (must report 0 mismatches)

A candidate order is correct when it compiles, runs, and prints byte-for-byte the same stdout (and same
exit status) as the Answer program. See docs/parsons-orders/brief.md.

Search space: the fragments are assembled (exact text, indentation offset applied) into the scaffold that
surrounds them in the Answer program. Every distinct sequence of fragment texts whose braces stay balanced
(never closing below the scaffold's own depth, ending at it) is generated and run. Identical-text fragments
are listed once, using the Answer's letter assignment. javac / the JVM are the only judges.
"""
import base64, glob, os, re, subprocess, sys, tempfile, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CHUNK = 300
WP = "/home/cjoe/piston-data/packages/java/25.0.1/wpilib"
WPCP = ":".join(f"{WP}/{j}" for j in [
    "commandsv3-java-2027.0.0-alpha-7.jar", "command3-test-support.jar", "wpilibj-java-2027.0.0-alpha-7.jar",
    "wpimath-java-2027.0.0-alpha-7.jar", "wpiunits-java-2027.0.0-alpha-7.jar", "wpiutil-java-2027.0.0-alpha-7.jar",
    "hal-java-2027.0.0-alpha-7.jar", "ntcore-java-2027.0.0-alpha-7.jar", "datalog-java-2027.0.0-alpha-7.jar",
    "quickbuf-runtime-1.4.jar"])

# ---------------------------------------------------------------- per-question overrides
# ctx: harness-supplied context for questions whose program has no main (Ch.25): prefix/suffix wrap the
# fragment region; extras are extra compilation units (drivers); all live in this folder, not in exercises.
def ctx_for(key):
    return CTX.get(key)

CTX = {}
def _load_ctx():
    d = os.path.join(HERE, "ctx")
    if not os.path.isdir(d):
        return
    for p in sorted(glob.glob(os.path.join(d, "*.py"))):
        g = {}
        exec(open(p).read(), g)
        for k,v in g["CTX"].items():
            if v.get("cp")=="__WPCP__": v["cp"]=WPCP
            CTX[k]=v
_load_ctx()

# input variants: replace text in the assembled program and re-compare each Also-accepted order with the
# Answer's output under that variant. Orders that only match on the original fixed input are "input-specific".
VARIANTS = {
    "19-interfaces-as-contracts.md": [[("return 2;", "return 5;")]],
    "19.1-lambdas-and-method-references.md": [[("97.5", "40.0"), ("7.5", "3.0")]],
    "20-the-io-layer-pattern.md": [[("boolean runningOnRobot = false;", "boolean runningOnRobot = true;")]],
    "21-static-factories.md": [[("createGripper(false)", "createGripper(true)")]],
    "22-the-builder-pattern.md": [[("setMaxAngle(110.0)", "setMaxAngle(70.0)"), ("setGearRatio(50.0)", "setGearRatio(9.0)"), ("setBrakeMode(true)", "setBrakeMode(false)")]],
    "23.1-scope-and-access.md": [[('"Red"', '"Blue"')]],
    "24-optional-avoiding-null-pointer-exceptions.md": [[("String chosenAuto = null;", 'String chosenAuto = "Four Note";')]],
    "25.1-what-is-command-based-programming.md": [
        [("{false, true, true, false, true}", "{true, true, false, true, false}")],
        [("{false, true, true, false, true}", "{false, true, false, true, true, false, true, true}")],
        [("{false, true, true, false, true}", "{true, false, true, true, true}")]],
    "25.2-commands-and-command-compositions.md": [[("int topAfter = 2;", "int topAfter = 0;")], [("int topAfter = 2;", "int topAfter = 3;")]],
    "25.4-state-machines-logic.md": [[("GearState.LOW;", "GearState.HIGH;")]],
    "25.5-managing-transitions.md": [[("3200.0", "2000.0")], [("3200.0", "5000.0")]],
    "25.6-binding-commands-to-triggers.md": [[("{1,1}, {1,1}, {1,1}, {1,1}, {1,0}", "{0,1}, {1,1}, {1,1}, {0,1}, {1,0}")]],
    "25.7-structuring-a-command-based-robot-project.md": [[("Seconds.of(2)", "Seconds.of(3)")], [("Seconds.of(2)", "Seconds.of(1)")]],
    "26-architecture-takeaways.md": [[("0.7;", "0.3;")]],
    "27.1-abstraction-and-program-design.md": [[("4000.0", "1234.0"), ("6000.0", "999.0")], [("/ 8.0", "/ 5.0")]],
    "28.1-searching-algorithms.md": [[('"Shooter"', '"Climber"')], [('"Shooter"', '"Nothing"')], [('"Shooter"', '"Drivetrain"')]],
    "28.2-sorting-algorithms.md": [[("{12.4, 11.9, 12.8, 12.1}", "{3.0, 2.0, 1.0}")], [("{12.4, 11.9, 12.8, 12.1}", "{1.0, 2.0, 3.0, 4.0}")]],
    "28.3-recursion.md": [[("totalReduction(4, 3)", "totalReduction(3, 2)")], [("totalReduction(4, 3)", "totalReduction(5, 0)")], [("totalReduction(4, 3)", "totalReduction(2, 1)")]],
    "28.4-recursive-searching-and-sorting.md": [[("110));", "20));")], [("110));", "150));")], [("110));", "999));"), ("{20, 45, 80, 110, 150}", "{}")]],
}

# Joe's decision (10-28-2026): orders must keep these (earlier, later) pairs in this relative order
# 19.1: the lambda header `d` must come before the declarations `f` and `c` (declared inside the lambda)
REQUIRE_BEFORE = {"19.1-lambdas-and-method-references.md": [("d", "f"), ("d", "c")]}

# max fragments held fixed at the head/tail of the Answer to bound the search (none by default)
FIXED = {}

# ---------------------------------------------------------------- parsing
def strip_code(line):
    line = re.sub(r'"(\\.|[^"\\])*"', '""', line)
    line = re.sub(r"'(\\.|[^'\\])'", "''", line)
    return re.sub(r"//.*", "", line)

def delta(text):
    s = strip_code(text)
    return s.count("{") - s.count("}")

def parse_section(path):
    txt = open(path).read()
    m = re.search(r"^## Micro-Parsons\n(.*?)(?=^## |\Z)", txt, re.S | re.M)
    sec = m.group(1)
    lines = sec.split("\n")
    frags = {}
    i = 0
    cur = None
    while i < len(lines):
        ln = lines[i]
        fm = re.match(r"^- ([a-z])\.(.*)$", ln)
        if fm:
            letter, rest = fm.group(1), fm.group(2).strip()
            if rest:
                spans = re.findall(r"`([^`]*)`", rest)
                frags[letter] = list(spans)
            else:  # fenced block on following lines
                j = i + 1
                assert lines[j].strip().startswith("```"), (path, letter)
                j += 1
                body = []
                while not lines[j].strip().startswith("```"):
                    body.append(lines[j])
                    j += 1
                ind = len(lines[i + 1]) - len(lines[i + 1].lstrip())
                frags[letter] = [b[ind:] if b.strip() else b for b in body]
                i = j
        i += 1
    am = re.search(r"^\*\*Answer:\*\* (.*)$", sec, re.M)
    answer = [x.strip() for x in am.group(1).split(",")]
    im = re.search(r"^\*\*Interchangeable:\*\* (.*)$", sec, re.M)
    inter = re.findall(r"\(([^)]*)\)", im.group(1)) if im else []
    inter = [[x.strip() for x in g.split(",")] for g in inter]
    om = re.search(r"^\*\*Also accepted:\*\* (.*)$", sec, re.M)
    also = []
    if om:
        also = [[x.strip() for x in o.split(",")] for o in om.group(1).split(";")]
    after = sec[am.end():]
    pm = re.search(r"```java\n(.*?)```", after, re.S)
    program = [l for l in pm.group(1).rstrip("\n").split("\n") if l.strip()]
    return dict(path=path, frags=frags, answer=answer, inter=inter, also=also, program=program, has_also=bool(om))

def locate(q):
    """find offset + position of the answer's fragment lines inside the program"""
    ans_lines = []
    for l in q["answer"]:
        ans_lines += q["frags"][l]
    prog = q["program"]
    for off in range(0, 25):
        sh = [(" " * off + l) if l.strip() else l for l in ans_lines]
        hits = [s for s in range(len(prog) - len(sh) + 1) if prog[s:s + len(sh)] == sh]
        if hits:
            assert len(hits) == 1, ("ambiguous", q["path"], hits)
            return off, hits[0], len(sh)
    raise SystemExit("cannot locate answer fragments in program: " + q["path"])

# ---------------------------------------------------------------- candidate assembly
def frag_text(q, letter, off):
    return "\n".join((" " * off + l) if l.strip() else l for l in q["frags"][letter])

def build(q, key, order, off, start, n, rep=()):
    c = ctx_for(key)
    region = "\n".join(frag_text(q, l, off) for l in order)
    if c:
        pre, suf, extras = c["prefix"], c["suffix"], c["extras"]
    else:
        pre = "\n".join(q["program"][:start])
        suf = "\n".join(q["program"][start + n:])
        extras = []
    main = "\n".join(x for x in [pre, region, suf] if x != "") + "\n"
    if c and c.get("replace"):
        main = main.replace(*c["replace"])
    units = [main] + extras
    for a, b in rep:
        assert any(a in u for u in units), ("variant text not found", key, a)
        units = [u.replace(a, b) for u in units]
    return units

# ---------------------------------------------------------------- layout rule (Joe, 10-28-2026)
def layout_ok(text):
    """braces stay with their own block: `{` alone follows its header at the header's indent; `}` has the indent
    of the line that opened its block; every line inside a block is indented further than the opener."""
    stack = []
    prev = None  # (stripped, indent) of previous non-blank line
    for raw in text.split("\n"):
        if not raw.strip():
            continue
        s = raw.strip()
        n = len(raw) - len(raw.lstrip())
        code = strip_code(raw).strip()
        if code == "{":
            if prev is None or prev[1] != n or prev[0].endswith((";", "{", "}")) or prev[0] in ("{", "}"):
                return False
            stack.append(n)
        elif code.startswith("}"):
            if not stack or n != stack[-1]:
                return False
            stack.pop()
            if code.endswith("{"):
                stack.append(n)
        else:
            if stack and n <= stack[-1]:
                return False
            if code.endswith("{"):
                stack.append(n)
        prev = (strip_code(raw).strip(), n)
    return not stack

def empty_blocks(text):
    """how many `{ ... }` blocks have nothing inside (Joe, 10-28-2026: an order that leaves a block empty,
    e.g. `if (x) { } else ...`, is wrong unless the Answer itself has that empty block)."""
    lines = [strip_code(r).strip() for r in text.split("\n") if strip_code(r).strip()]
    return sum(1 for a, b in zip(lines, lines[1:]) if a.endswith("{") and b.startswith("}"))

# ---------------------------------------------------------------- run
def run_batch(cands, mainname, stdin, cp):
    """cands: dict id -> list of unit texts (no package line). returns id -> (status, exit, stdout bytes)"""
    res = {}
    ids = list(cands)
    for k in range(0, len(ids), CHUNK):
        part = ids[k:k + CHUNK]
        with tempfile.TemporaryDirectory() as td:
            cf, rf = os.path.join(td, "c.txt"), os.path.join(td, "r.txt")
            with open(cf, "w") as f:
                for i in part:
                    f.write(f"@@@CAND {i}\n")
                    for u in cands[i]:
                        f.write("@@@UNIT\n" + f"package p{i};\n" + u)
            sf = "-"
            if stdin is not None:
                sf = os.path.join(td, "in.txt")
                open(sf, "w").write(stdin)
            cmd = ["java", "--add-opens", "java.base/jdk.internal.vm=ALL-UNNAMED", "--add-opens", "java.base/java.lang=ALL-UNNAMED",
                   "-Xmx384m", os.path.join(HERE, "Runner.java"), cf, rf, mainname, sf] + ([cp] if cp else [])
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=(None if os.environ.get("PO_DEBUG") else subprocess.DEVNULL))
            for line in open(rf):
                i, st, ex, b = line.rstrip("\n").split("\t")
                res[i] = (st, ex, base64.b64decode(b))
    return res

# ---------------------------------------------------------------- search
WINDOW = 7
# extra (head, tail) searches in which the middle is split into balanced units (descend into a block body)
EXTRA_UNITS = {}

def descents(q, off):
    """interiors of every balanced block in the Answer: (head, tail, True) with the interior cut into units"""
    ans = q["answer"]
    n = len(ans)
    d = [delta(frag_text(q, l, off)) for l in ans]
    cum = []
    c = 0
    for x in d:
        c += x
        cum.append(c)
    out = []
    for i in range(n):
        before = cum[i] - d[i]
        if d[i] > 0:
            for j in range(i + 1, n):
                if cum[j] <= before:
                    # interior is i+1 .. j-1 (j closes the block); may be empty/one item
                    if j - i - 1 >= 2:
                        mid = ans[i + 1:j]
                        if len(make_units(q, off, mid)) <= 8:
                            out.append((i + 1, n - j, True))
                    break
    return sorted(set(out))

def searches(q, key, off=0):
    n = len(q["answer"])
    if n <= 8:
        return [(0, 0, False)]
    sp = [(0, 0, True)] + [(s, n - s - WINDOW, False) for s in range(0, n - WINDOW + 1)]
    sp += descents(q, off)
    sp += [(h, t, True) for (h, t) in EXTRA_UNITS.get(key, [])]
    return sp

def make_units(q, off, mid):
    """cut the middle fragments into statements / balanced blocks (cut where depth returns to 0 after ';' or '}')"""
    units, cur, depth = [], [], 0
    for l in mid:
        t = frag_text(q, l, off)
        cur.append(l)
        depth += delta(t)
        last = strip_code(t).rstrip()[-1:]
        if depth == 0 and last in (";", "}"):
            units.append(cur)
            cur = []
    if cur:
        units.append(cur)
    return units

def gen_orders(q, off, key, spec=(0, 0, False)):
    """lazily yield distinct unit sequences (balanced braces) as letter lists, Answer's letters for equal text"""
    ans = q["answer"]
    fh, ft, split = spec
    head = ans[:fh]
    tail = ans[len(ans) - ft:] if ft else []
    mid = ans[fh:len(ans) - ft]
    units = make_units(q, off, mid) if split else [[l] for l in mid]
    utext = [("\n".join(frag_text(q, l, off) for l in u)) for u in units]
    bytext = {}
    for u, t in zip(units, utext):
        bytext.setdefault(t, []).append(u)
    uniq = list(bytext)
    cnt = {t: len(bytext[t]) for t in uniq}
    dl = {t: delta(t) for t in uniq}
    base = sum(delta(frag_text(q, l, off)) for l in head)
    tail_d = sum(delta(frag_text(q, l, off)) for l in tail)
    used = {t: 0 for t in uniq}
    seq = []
    total = len(units)

    def rec(depth):
        if len(seq) == total:
            if depth + tail_d == 0:
                taken = {t: 0 for t in uniq}
                full = list(head)
                for t in seq:
                    full += bytext[t][taken[t]]
                    taken[t] += 1
                yield full + tail
            return
        for t in uniq:
            if used[t] < cnt[t]:
                nd = depth + dl[t]
                if nd < 0:
                    continue
                used[t] += 1
                seq.append(t)
                yield from rec(nd)
                seq.pop()
                used[t] -= 1
    yield from rec(base)

def all_orders(q, off, key):
    """union over the searches, deduped (a set of tuples only of already-generated orders is kept lazily via seen-hash)"""
    seen = set()
    for sp in searches(q, key, off):
        for o in gen_orders(q, off, key, sp):
            h = tuple(o)
            if h in seen:
                continue
            seen.add(h)
            yield o

def count_orders(q, off, key, cap=10**9):
    n = 0
    for _ in all_orders(q, off, key):
        n += 1
        if n >= cap:
            break
    return n

def key_of(path, idx=0):
    return os.path.basename(path) + (f"#{idx}" if idx else "")

def process(path, mode):
    q = parse_section(path)
    key = key_of(path)
    off, start, n = locate(q)
    c = ctx_for(key)
    mainname = c["main"] if c else None
    if mainname is None:
        pub = [l for l in q["program"] if "static void main" in l]
        # the class holding main: nearest preceding class line
        mainname = None
        for i, l in enumerate(q["program"]):
            if "static void main" in l:
                for j in range(i, -1, -1):
                    m = re.match(r"\s*(?:public\s+)?(?:final\s+)?class (\w+)", q["program"][j])
                    if m:
                        mainname = m.group(1)
                        break
                break
    cp = c.get("cp", "") if c else ""
    stdin = c.get("stdin") if c else None
    pos = {l: i for i, l in enumerate(q["answer"])}
    ref_c = {"0": build(q, key, q["answer"], off, start, n)}
    for j, o in enumerate(q["also"]):
        ref_c[f"x{j}"] = build(q, key, o, off, start, n)
    res = run_batch(ref_c, mainname, stdin, cp)
    ref = res["0"]
    if ref[0] != "OK":
        return dict(path=path, error=f"Answer program did not run cleanly: {ref[0]}", q=q)
    def same(r):
        return r[0] == "OK" and r[2] == ref[2] and r[1] == ref[1]
    extra = {f"x{j}": o for j, o in enumerate(q["also"])}
    good = []
    searched = 0
    batch = {}
    allo = {}
    def flush():
        nonlocal batch, allo
        if not batch:
            return
        r = run_batch(batch, mainname, stdin, cp)
        for i, v in r.items():
            if same(v):
                good.append(allo[i])
        batch, allo = {}, {}
    ans_empty = empty_blocks(build(q, key, q["answer"], off, start, n)[0])
    for o in all_orders(q, off, key):
        searched += 1
        if tuple(o) == tuple(q["answer"]):
            continue
        i = str(searched)
        if any(o.index(x) > o.index(y) for x, y in REQUIRE_BEFORE.get(key, [])):
            continue
        bu = build(q, key, o, off, start, n)
        if not layout_ok(bu[0]) or empty_blocks(bu[0]) > ans_empty:
            continue
        allo[i] = o
        batch[i] = bu
        if len(batch) >= CHUNK:
            flush()
    flush()
    orders = range(searched)
    assert layout_ok(build(q, key, q["answer"], off, start, n)[0]), ("Answer fails layout rule", key)
    # drop orders that match only by luck: re-run under every input variant
    luck = 0
    for rep in VARIANTS.get(key, []):
        if not good:
            break
        vc = {"0": build(q, key, q["answer"], off, start, n, rep)}
        for j, o in enumerate(good):
            vc[f"v{j}"] = build(q, key, o, off, start, n, rep)
        vr = run_batch(vc, mainname, stdin, cp)
        vref = vr["0"]
        assert vref[0] == "OK", ("variant answer failed", key, rep, vref[0])
        keep = [o for j, o in enumerate(good) if vr[f"v{j}"][0] == "OK" and vr[f"v{j}"][2] == vref[2] and vr[f"v{j}"][1] == vref[1]]
        luck += len(good) - len(keep)
        good = keep
    ansT = tuple(q["answer"])
    good.sort(key=lambda o: [pos[l] for l in o])
    declared_bad = [o for j, o in extra.items() if not same(res[j])]
    goodset = {tuple(o) for o in good}
    alsoset = {tuple(o) for o in q["also"]}
    # an order listed under Also accepted must be one the search considers distinct from the Answer
    missing = [list(o) for o in goodset - alsoset]
    bogus = [list(o) for o in alsoset - goodset]
    inter_bad = []
    for g in q["inter"]:
        # every swap inside an interchangeable group must be a correct order
        idxs = [q["answer"].index(l) for l in g]
        for perm in itertools.permutations(g):
            o = list(q["answer"])
            for ii, l in zip(idxs, perm):
                o[ii] = l
            if tuple(o) != ansT:
                texts = {frag_text(q, l, off) for l in g}
                if len(texts) == 1:
                    continue
                if tuple(o) not in goodset:
                    inter_bad.append(o)
    nonrobust = []
    if mode == "check" and key in VARIANTS and q["also"]:
        robust = {tuple(o) for o in q["also"]}
        for rep in VARIANTS[key]:
            vc = {"0": build(q, key, q["answer"], off, start, n, rep)}
            for j, o in enumerate(q["also"]):
                vc[f"x{j}"] = build(q, key, o, off, start, n, rep)
            vr = run_batch(vc, mainname, stdin, cp)
            vref = vr["0"]
            assert vref[0] == "OK", ("variant answer failed", key, rep, vref[0])
            for j, o in enumerate(q["also"]):
                v = vr[f"x{j}"]
                if not (v[0] == "OK" and v[2] == vref[2] and v[1] == vref[1]):
                    robust.discard(tuple(o))
        nonrobust = [o for o in q["also"] if tuple(o) not in robust]
    return dict(path=path, q=q, good=good, nonrobust=nonrobust, luck=luck, searched=searched, declared_bad=declared_bad,
                missing=missing, bogus=bogus, inter_bad=inter_bad, ref_out=ref[2], mainname=mainname,
                nfrag=len(q["answer"]))

def fmt(orders):
    return "; ".join(", ".join(o) for o in orders)

def write_also(path, good):
    txt = open(path).read()
    m = re.search(r"^## Micro-Parsons\n.*?(?=^## |\Z)", txt, re.S | re.M)
    sec = m.group(0)
    sec = re.sub(r"^\*\*Also accepted:\*\* .*\n\n", "", sec, flags=re.M)
    if not good:
        new = sec
    else:
        line = f"**Also accepted:** {fmt(good)}\n\n"
        am = re.search(r"^\*\*Answer:\*\* .*\n\n", sec, re.M)
        end = am.end()
        im = re.compile(r"^\*\*Interchangeable:\*\* .*\n\n", re.M).match(sec, end)
        if im:
            end = im.end()
        new = sec[:end] + line + sec[end:]
    open(path, "w").write(txt[:m.start()] + new + txt[m.end():])

def main():
    mode = sys.argv[1]
    args = sys.argv[2:]
    write = "--write" in args
    args = [a for a in args if a != "--write"]
    files = sorted(glob.glob(os.path.join(ROOT, "exercises", "ch*", "*.md")))
    sel = []
    for f in files:
        ch = re.match(r"ch(\d+)-", os.path.basename(os.path.dirname(f)))
        if not ch or not (19 <= int(ch.group(1)) <= 28):
            continue
        if "## Micro-Parsons" not in open(f).read():
            continue
        if args and not any(a in f for a in args):
            continue
        sel.append(f)
    tot_q = tot_orders = mism = 0
    for f in sel:
        r = process(f, mode)
        rel = os.path.relpath(f, ROOT)
        tot_q += 1
        if "error" in r:
            print(f"ERROR {rel}: {r['error']}")
            mism += 1
            continue
        if mode == "search":
            print(f"{rel}: {r['nfrag']} fragments, {r['searched']} balanced orders run, {len(r['good'])} correct besides Answer ({r['luck']} dropped as input-specific)")
            if r["good"]:
                print("   Also accepted:", fmt(r["good"]))
            if write:
                write_also(f, r["good"])
        else:
            tot_orders += len(r["good"]) + 1
            bad = r["declared_bad"] or r["missing"] or r["bogus"] or r["inter_bad"]
            n = len(r["declared_bad"]) + len(r["missing"]) + len(r["bogus"]) + len(r["inter_bad"])
            mism += n
            print(f"{rel}: searched {r['searched']}, verified {len(r['good'])} also-accepted + Answer, mismatches {n}")
            if r["nonrobust"]:
                print(f"    input-specific (match only on the fixed input, differ under input variants): {len(r['nonrobust'])} of {len(r['q']['also'])}")
            for k in ("declared_bad", "missing", "bogus", "inter_bad"):
                if r[k]:
                    print("   ", k, r[k])
    if mode == "check":
        print(f"SUMMARY questions checked: {tot_q}; orders verified (incl. Answers): {tot_orders}; mismatches: {mism}")

if __name__ == "__main__":
    main()
