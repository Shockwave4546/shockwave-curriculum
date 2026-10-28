#!/usr/bin/env python3
"""Micro-Parsons "every correct order" harness (chapters 10-18). Standard library + JDK only.

  python3 harness.py search            # exhaustive search per question, print orders found
  python3 harness.py write             # add/refresh **Also accepted:** lines in the exercise files
  python3 harness.py check             # re-run on the edited files: every listed order must match the Answer
                                       # output, and every order found by the search must be listed (or be the Answer)
Options: --files substr (filter), --workers N
"""
import sys, os, re, glob, itertools, subprocess, threading, queue, base64, tempfile, json, hashlib, time
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
CHAPTERS = range(10, 19)
RUNNER = os.path.join(HERE, 'Runner.java')
# Joe's decision 10-28-2026 (1): an order must not match only by luck. Every candidate is re-run with changed
# input data. STAGES[file] = list of {'repl': [(old, new)] applied to the assembled source, 'files': {name: content}}.
# The base run (original data) is always stage 0.
S_ = lambda *pairs: {'repl': list(pairs)}
STAGES = {
 '10.2-2d-array-traversals-nested-loops.md': [
    S_(('{ {30, 60, 90}, {32, 58, 91} }', '{ {1, 2}, {3, 4}, {5, 6} }')),
    S_(('{ {30, 60, 90}, {32, 58, 91} }', '{ {7, 8, 9, 10} }')),
    S_(('{ {30, 60, 90}, {32, 58, 91} }', '{ {1}, {2}, {3} }'))],
 '10.3-implementing-2d-array-algorithms.md': [
    S_(('{ {42, 38, 35}, {40, 41, 33}, {45, 36, 37} }', '{ {9, 9, 9}, {1, 2, 3}, {5, 4, 0} }'), ('(swapTimes, 1)', '(swapTimes, 0)')),
    S_(('{ {42, 38, 35}, {40, 41, 33}, {45, 36, 37} }', '{ {9, 9, 9}, {1, 2, 3}, {5, 4, 0} }'), ('(swapTimes, 1)', '(swapTimes, 2)')),
    S_(('{ {42, 38, 35}, {40, 41, 33}, {45, 36, 37} }', '{ {1, 1, 1}, {2, 2, 2}, {3, 3, 3} }')),
    S_(('{ {42, 38, 35}, {40, 41, 33}, {45, 36, 37} }', '{ {3, 3, 3}, {2, 2, 2}, {1, 1, 1} }')),
    S_(('{ {42, 38, 35}, {40, 41, 33}, {45, 36, 37} }', '{ {5, 5, 5}, {5, 5, 5}, {5, 5, 5} }'))],
 '11-enums-named-choices.md': [S_(('DriveMode.PRECISION;', 'DriveMode.TURBO;'))],
 '12-exceptions-and-try-catch.md': [
    {'files': {'pit_notes.txt': 'Pit note line one\nsecond line\n'}},
    {'files': {'pit_notes.txt': ''}},
    {'files': {'pit_notes.txt': 'x'}}],
 '13-common-gotchas.md': [S_(('"Re-tension intake belt"', '"x"'))],
 '15-advanced-collections.md': [S_(('"Note 1"', '"A"'), ('"Note 2"', '"B"'))],
 '16-writing-your-own-generics.md': [S_(('kP.set(0.05);', 'kP.set(2.5);')), S_(('Tunable<Double>', 'Tunable<Double>'), ('kP.set(0.05);', 'kP.set(-1.0);'))],
 '17.3-inheritance-hierarchies.md': [
    S_(('{ new FloorRoller(), new FeederRoller() }', '{ new FeederRoller(), new FloorRoller() }')),
    S_(('{ new FloorRoller(), new FeederRoller() }', '{ new FeederRoller() }')),
    S_(('{ new FloorRoller(), new FeederRoller() }', '{ new FloorRoller(), new FloorRoller(), new FeederRoller() }'))],
 '17.4-object-superclass.md': [
    S_(('System.out.println(seen.equals(expected));', 'System.out.println(seen.equals(expected));\n        System.out.println(seen.equals("x"));\n        System.out.println(seen.equals(null));\n        System.out.println(seen.equals(new FieldTag(8)));\n        System.out.println(seen.equals(seen));')),
    S_(('FieldTag(7);\n        FieldTag expected = new FieldTag(7)', 'FieldTag(7);\n        FieldTag expected = new FieldTag(9)'),
       ('System.out.println(seen.equals(expected));', 'System.out.println(seen.equals(expected));\n        System.out.println(seen.equals(42));'))],
 '18.3-polymorphism.md': [
    S_(('alerts[0] = new RumbleAlert();', 'alerts[0] = new LightAlert();'), ('alerts[1] = new LightAlert();', 'alerts[1] = new RumbleAlert();')),
    S_(('alerts[0] = new RumbleAlert();', 'alerts[0] = new LightAlert();')),
    S_(('alerts[1] = new LightAlert();', 'alerts[1] = new RumbleAlert();'))],
}

def stages_for(q):
    return STAGES.get(os.path.basename(q.path), [])

def apply_stage(src, st):
    for old, new in st.get('repl', []):
        assert old in src, (old,)
        src = src.replace(old, new)
    return src

# Joe's decision 10-28-2026 (2): braces stay with their own block.
def layout_ok(src):
    stack = []
    prev = None
    for l in src.rstrip('\n').split('\n'):
        s = l.strip()
        if not s:
            continue
        ind = len(l) - len(l.lstrip())
        if s == '{':
            if prev is None or prev.strip() in ('{', '}') or prev.strip().endswith((';', '}', '{')) or prev.strip().startswith('@'):
                return False
            if len(prev) - len(prev.lstrip()) != ind:
                return False
            if stack and ind <= stack[-1]:
                return False
            stack.append(ind)
        elif s == '}':
            if not stack or stack.pop() != ind:
                return False
        else:
            if stack and ind <= stack[-1]:
                return False
            if not stack and ind != 0:
                return False
        prev = l
    return not stack


# ---------------------------------------------------------------- parsing
def strip_strings(s):
    s = re.sub(r'"(\\.|[^"\\])*"', '""', s)
    return re.sub(r"'(\\.|[^'\\])'", "''", s)

def net(text):
    t = strip_strings(text)
    return t.count('{') - t.count('}')

class Question:
    pass

def parse_file(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    start = next((i for i, l in enumerate(lines) if l.startswith('## Micro-Parsons')), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith('## ')), len(lines))
    q = Question()
    q.path, q.lines, q.start, q.end = path, lines, start, end
    sec = lines[start:end]
    q.frag = {}
    first_frag = None
    for i, l in enumerate(sec):
        m = re.match(r'^- ([a-z])\. `(.*)`\s*$', l)
        if m:
            q.frag[m.group(1)] = m.group(2)
            first_frag = first_frag if first_frag is not None else i
    ans = [i for i, l in enumerate(sec) if l.startswith('**Answer:**')]
    assert len(ans) == 1, path
    q.ans_line = start + ans[0]
    q.answer = [x.strip() for x in sec[ans[0]].split(':**', 1)[1].split(',')]
    q.interch = None
    q.also_line = None
    for i, l in enumerate(sec):
        if l.startswith('**Interchangeable:**'):
            q.interch = start + i
        if l.startswith('**Also accepted:**'):
            q.also_line = start + i
    q.also = []
    if q.also_line is not None:
        body = lines[q.also_line].split(':**', 1)[1].strip()
        q.also = [[x.strip() for x in o.split(',')] for o in body.split(';') if o.strip()]
    # scaffold: first ```java block before the fragment list
    q.scaffold = None
    i = 0
    while i < first_frag:
        if sec[i].startswith('```java'):
            j = i + 1
            blk = []
            while not sec[j].startswith('```'):
                blk.append(sec[j]); j += 1
            q.scaffold = blk
            break
        i += 1
    # answer code block (after Answer)
    k = ans[0] + 1
    while not sec[k].startswith('```java'):
        k += 1
    j = k + 1
    blk = []
    while not sec[j].startswith('```'):
        blk.append(sec[j]); j += 1
    q.answer_code = blk
    q.code_start = start + k
    q.name = os.path.relpath(path, os.path.join(ROOT, 'exercises'))
    assert sorted(q.answer) == sorted(q.frag), (path, q.answer)
    # placeholder
    if q.scaffold:
        ph = [i for i, l in enumerate(q.scaffold) if l.strip().startswith('//')]
        assert len(ph) <= 1, (path, ph)
        q.insert = False
        if ph:
            q.ph_index = ph[0]
            q.level = (len(q.scaffold[ph[0]]) - len(q.scaffold[ph[0]].lstrip())) // 4
        else:
            # no placeholder: fragments are a whole class placed after the scaffold, or before it
            # when the Problem says the scaffold classes go below / the new class goes above
            prob = '\n'.join(sec[:first_frag])
            before = ('go *below*' in prob) or ('goes above' in prob)
            q.ph_index = 0 if before else len(q.scaffold)
            q.insert = True
            q.level = 0
    else:
        q.ph_index = None
        q.level = 0
    return q

def assemble(q, seq):
    texts = [q.frag[x] for x in seq]
    if q.scaffold is None:
        return '\n'.join(texts) + '\n'
    out = q.scaffold[:q.ph_index] + texts + q.scaffold[q.ph_index + (0 if q.insert else 1):]
    return '\n'.join(out) + '\n'

# ---------------------------------------------------------------- tree
# item: ('leaf', letter) | ('block', header_letter_or_None, open_letter, [items], close_letter)
def build_tree(q):
    stack = [[]]
    opens = []
    for x in q.answer:
        t = q.frag[x].strip()
        if t == '{':
            hdr = None
            if stack[-1] and stack[-1][-1][0] == 'leaf':
                hdr = stack[-1].pop()[1]
            stack.append([])
            opens.append((hdr, x))
        elif t == '}':
            body = stack.pop()
            hdr, o = opens.pop()
            stack[-1].append(('block', hdr, o, body, x))
        else:
            assert net(q.frag[x]) == 0, (q.name, x)
            stack[-1].append(('leaf', x))
    assert len(stack) == 1 and not opens, q.name
    return stack[0]

def item_letters(it):
    if it[0] == 'leaf':
        return [it[1]]
    _, h, o, body, c = it
    r = ([h] if h else []) + [o]
    for b in body:
        r += item_letters(b)
    return r + [c]

def list_letters(items):
    r = []
    for it in items:
        r += item_letters(it)
    return r

# dims: each dim is a list node (container) whose order can vary. Represent as a mutable "slot".
class Dim:
    def __init__(self, kind, depth, items, label):
        self.kind, self.depth, self.items, self.label = kind, depth, items, label
        self.alts = None

def collect_dims(items, depth, label, dims):
    flat = depth >= 2
    d = Dim('flat' if flat else 'units', depth, items, label)
    dims.append(d)
    if not flat:
        for it in items:
            if it[0] == 'block':
                collect_dims(it[3], depth + 1, label + '/' + (it[1] or it[2]), dims)

def render(items, depth, choice, label, dims_by_label, q):
    """Return letter sequence of this list under the chosen orders."""
    d = dims_by_label[label]
    order = choice.get(label)
    if d.kind == 'flat':
        return list(order) if order is not None else list_letters(items)
    units = items if order is None else [items[i] for i in order]
    r = []
    for it in units:
        if it[0] == 'leaf':
            r.append(it[1])
        else:
            _, h, o, body, c = it
            if h: r.append(h)
            r.append(o)
            r += render(body, depth + 1, choice, label + '/' + (h or o), dims_by_label, q)
            r.append(c)
    return r

def unit_text(q, it):
    return '\n'.join(q.frag[x] for x in item_letters(it))

def alternatives(q, d):
    """Lazily yield distinct orders for a dim (index perm for units, letter list for flat)."""
    if d.kind == 'units':
        keys = [unit_text(q, it) for it in d.items]
        seen = set()
        for p in itertools.permutations(range(len(keys))):
            k = tuple(keys[i] for i in p)
            if k in seen:
                continue
            seen.add(k)
            yield list(p)
        return
    letters = list_letters(d.items)
    groups = {}
    for x in letters:
        groups.setdefault(q.frag[x], []).append(x)
    keys = list(groups)
    cnt = {k: len(groups[k]) for k in keys}
    knet = {k: net(k) for k in keys}
    total = len(letters)
    cur = []
    def rec(depth):
        if len(cur) == total:
            if depth == 0:
                used = Counter(); lets = []
                for k in cur:
                    lets.append(groups[k][used[k]]); used[k] += 1
                yield lets
            return
        for k in keys:
            if cnt[k] and depth + knet[k] >= 0:
                cnt[k] -= 1; cur.append(k)
                yield from rec(depth + knet[k])
                cur.pop(); cnt[k] += 1
    yield from rec(0)

def canon(q, seq):
    """canonical letter assignment for identical-text fragments (answer's assignment)."""
    groups = {}
    for x in q.answer:
        groups.setdefault(q.frag[x], []).append(x)
    used = Counter(); r = []
    for x in seq:
        t = q.frag[x]
        r.append(groups[t][used[t]]); used[t] += 1
    return r

# ---------------------------------------------------------------- running
def main_class(code):
    m = re.search(r'(?:class|enum|interface)\s+(\w+)[^{]*\{[^}]*?static\s+void\s+main', code, re.S)
    # fall back: first class that contains main
    for cm in re.finditer(r'(?:class|enum)\s+(\w+)', code):
        pos = cm.end()
        nxt = re.search(r'\n(?:public\s+|abstract\s+)?(?:class|enum|interface)\s', code[pos:])
        seg = code[pos: pos + nxt.start()] if nxt else code[pos:]
        if re.search(r'static\s+void\s+main\s*\(', seg):
            return cm.group(1)
    raise Exception('no main')

def run_batch(jobs, mainc, files=None):
    """jobs: list of <=CHUNK source strings, one JVM at a time (-Xmx384m). returns list of (status, out_b64)."""
    res = [None] * len(jobs)
    tmp = tempfile.mkdtemp(prefix='parsons_')
    try:
        rec = os.path.join(tmp, 'rec.txt')
        with open(rec, 'w', encoding='utf-8') as f:
            for i, j in enumerate(jobs):
                f.write(f"{i}\n{mainc}\n{j}\x01\n")
        cwd = os.path.join(tmp, 'cwd'); os.makedirs(cwd)
        for fn, content in (files or {}).items():
            open(os.path.join(cwd, fn), 'w').write(content)
        pos = 0
        while pos < len(jobs):
            p = subprocess.Popen(['java', '-Xmx384m', RUNNER, rec, str(pos)], cwd=cwd, stdout=subprocess.PIPE,
                                 stderr=subprocess.DEVNULL, text=True)
            qq = queue.Queue()
            def rd(p=p, qq=qq):
                for line in p.stdout:
                    qq.put(line)
                qq.put(None)
            threading.Thread(target=rd, daemon=True).start()
            last = time.time(); limit = 60
            while True:
                try:
                    line = qq.get(timeout=1)
                except queue.Empty:
                    if time.time() - last > limit:
                        p.kill(); p.wait()
                        res[pos] = ('TIMEOUT', ''); pos += 1
                        break
                    continue
                if line is None:
                    p.wait()
                    if pos < len(jobs) and res[pos] is None:
                        res[pos] = ('RUNNERERR', ''); pos += 1
                    break
                i, st, out = line.rstrip('\n').split('\t')
                res[int(i)] = (st, out)
                pos = int(i) + 1
                last = time.time(); limit = 8
    finally:
        import shutil; shutil.rmtree(tmp, ignore_errors=True)
    return res

CHUNK = 300

def norm_key(src):
    """programs identical up to indentation compile and run identically; run one representative"""
    t = '\n'.join(l.strip() for l in src.split('\n'))
    return hashlib.md5(t.encode()).digest()

def stream_run(q, seqs_iter, ans_res):
    """Run an iterator of letter sequences in chunks; return (count_run, skipped_layout, passing seqs).
    Only layout-valid orders are run; only passing orders are kept; results cached by indentation-normalised hash."""
    mc = main_class('\n'.join(q.answer_code))
    stages = stages_for(q)
    ans_src = assemble(q, q.answer)
    stage_ans = [run_batch([apply_stage(ans_src, st)], mc, st.get('files'))[0] for st in stages]
    n = 0; skipped = 0; good = []
    cache = {}
    buf = []
    def flush():
        nonlocal n
        if not buf: return
        reps = {}
        for seq, key, src in buf:
            if key not in cache and key not in reps:
                reps[key] = src
        keys = list(reps)
        rs = run_batch([reps[k] for k in keys], mc) if keys else []
        for k, r in zip(keys, rs):
            cache[k] = (r == ans_res)
        for st, sa in zip(stages, stage_ans):
            surv = [k for k in keys if cache[k]]
            if not surv: break
            rs2 = run_batch([apply_stage(reps[k], st) for k in surv], mc, st.get('files'))
            for k, r in zip(surv, rs2):
                cache[k] = (r == sa)
        for seq, key, _ in buf:
            if cache[key]: good.append(seq)
        n += len(buf); buf.clear()
    for s in seqs_iter:
        src = assemble(q, list(s))
        if not layout_ok(src):
            skipped += 1
            continue
        buf.append((s, norm_key(src), src))
        if len(buf) >= CHUNK: flush()
    flush()
    return n, skipped, good

def run_orders(q, orders, workers=1):
    """result per order: tuple of results over base + every stage (compare tuples for equality)."""
    mc = main_class('\n'.join(q.answer_code))
    stages = stages_for(q)
    out = []
    for i in range(0, len(orders), CHUNK):
        srcs = [assemble(q, o) for o in orders[i:i + CHUNK]]
        cols = [run_batch(srcs, mc)]
        for st in stages:
            cols.append(run_batch([apply_stage(x, st) for x in srcs], mc, st.get('files')))
        out += list(zip(*cols))
    return out

def search(q, workers=1):
    tree = build_tree(q)
    dims = []
    collect_dims(tree, q.level, '', dims)
    by_label = {d.label: d for d in dims}
    assert layout_ok(assemble(q, q.answer)), q.name
    ans_res = run_batch([assemble(q, q.answer)], main_class('\n'.join(q.answer_code)))[0]
    assert ans_res[0] == 'OK0', (q.name, ans_res)
    info = {'dims': [], 'tested': 1}
    valid_per_dim = {}
    for d in dims:
        specs = {}
        def gen(d=d, specs=specs):
            for a in alternatives(q, d):
                seq = tuple(canon(q, render(tree, q.level, {d.label: a}, '', by_label, q)))
                specs.setdefault(seq, a)
                yield seq
        n, sk, good = stream_run(q, gen(), ans_res)
        valid_per_dim[d.label] = [(specs[s], s) for s in good]
        specs.clear()
        info['tested'] += n
        info['dims'].append((d.label or '<top>', d.kind, n, len(good)))
    labels = list(valid_per_dim)
    combos = 1
    for l in labels:
        combos *= len(valid_per_dim[l])
    info['product'] = combos
    info['product_bad'] = 0
    if combos > 20000:
        info['capped'] = True
        return [], info
    def pgen():
        seen = set()
        for pick in itertools.product(*[valid_per_dim[l] for l in labels]):
            choice = {l: a for l, (a, _) in zip(labels, pick)}
            seq = tuple(canon(q, render(tree, q.level, choice, '', by_label, q)))
            if seq not in seen:
                seen.add(seq); yield seq
    n, sk, good = stream_run(q, pgen(), ans_res)
    info['tested'] += n
    seen = set()
    expected = sum(1 for _ in pgen())
    info['product_bad'] = expected - len(good)
    good = [list(s) for s in good if list(s) != q.answer]
    return good, info

def order_str(o):
    return ', '.join(o)

def also_line(orders):
    return '**Also accepted:** ' + '; '.join(order_str(o) for o in orders)

def load_questions(filt):
    qs = []
    for ch in CHAPTERS:
        for p in sorted(glob.glob(os.path.join(ROOT, 'exercises', f'ch{ch:02d}-*', '*.md'))):
            if filt and filt not in p:
                continue
            q = parse_file(p)
            if q:
                qs.append(q)
    return qs

def write_also(q, orders):
    lines = open(q.path, encoding='utf-8').read().split('\n')
    # insertion point: after Interchangeable if present else after Answer
    idx = (q.interch if q.interch is not None else q.ans_line)
    if q.also_line is not None:
        if orders:
            lines[q.also_line] = also_line(orders)
        else:
            del lines[q.also_line - 1: q.also_line + 1]
    elif orders:
        lines[idx + 1: idx + 1] = ['', also_line(orders)]
    open(q.path, 'w', encoding='utf-8').write('\n'.join(lines))

# Orders Joe ruled out by hand (10-28-2026): equivalent code that contradicts what the Problem describes.
# Keyed by a substring of the question name; each order is a tuple of letters.
EXCLUDED = {
    # 15: loads "Note 2", feeds it out, then loads "Note 1" -- the Problem says it loads two pieces, then feeds out.
    '15-advanced-collections': {tuple('idbfhleagkcj'), tuple('dibfhleagkcj')},
}

def excluded(q, o):
    return any(k in q.name and tuple(o) in v for k, v in EXCLUDED.items())

def main():
    argv = sys.argv[1:]
    cmd = argv[0] if argv else 'search'
    filt = argv[argv.index('--files') + 1] if '--files' in argv else None
    workers = int(argv[argv.index('--workers') + 1]) if '--workers' in argv else 7
    qs = load_questions(filt)
    tot_q = tot_orders = mism = 0
    for q in qs:
        # sanity: assembled answer == answer code block
        asm = assemble(q, q.answer).rstrip('\n').split('\n')
        nb = lambda ls: [l.rstrip() for l in ls if l.strip()]
        same = nb(asm) == nb(q.answer_code)
        found, info = search(q, workers)
        found = [o for o in found if not excluded(q, o)]
        tot_q += 1
        print(f"{q.name}: dims={info['dims']} product={info['product']} tested={info['tested']} found={len(found)} answer_code_matches={same}")
        if info.get('capped'):
            print('   CAPPED (not exhaustively combined)')
        if info['product_bad']:
            print(f"   WARNING: {info['product_bad']} product combos failed")
        if cmd == 'search':
            for o in found:
                print('   ', order_str(o))
        elif cmd == 'write':
            write_also(q, found)
            tot_orders += len(found)
        elif cmd == 'check':
            listed = {tuple(o) for o in q.also}
            # every listed order must run and match
            lres = run_orders(q, [list(o) for o in q.also], workers)
            ans_res = run_orders(q, [q.answer])[0]
            bad = [o for o, r in zip(q.also, lres) if r != ans_res or not layout_ok(assemble(q, o))]
            miss = [o for o in found if tuple(o) not in listed]
            extra = [o for o in q.also if tuple(canon(q, o)) not in {tuple(f) for f in found}]
            # interchangeable variants must be in the list too (list complete on its own)
            tot_orders += len(q.also)
            m = len(bad) + len(miss) + len(extra)
            mism += m
            print(f"   listed={len(q.also)} verified={len(q.also)-len(bad)} missing_from_list={len(miss)} not_found_by_search={len(extra)} mismatches={m}")
            for o in bad: print('    BAD', order_str(o))
            for o in miss: print('    MISSING', order_str(o))
            for o in extra: print('    EXTRA', order_str(o))
        if not same:
            print('   !! scaffold assembly differs from answer code block')
    print(f"questions_checked={tot_q} orders={'(added)' if cmd=='write' else ''}{tot_orders} mismatches={mism}")

if __name__ == '__main__':
    main()
