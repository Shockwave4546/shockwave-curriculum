#!/usr/bin/env python3
"""Micro-Parsons order harness (chapters 1-9). Standard library + JDK only.

Per exercise file: parse fragments / Answer / Also accepted, assemble candidate
programs, compile and run them (Runner.java), compare stdout + status with the
Answer program, exhaustively search block-body permutations, and (with --write)
insert the **Also accepted:** line.

Usage:
  python3 parsons_orders.py [--write] [--json out.json] [file ...]
Default files: every exercises/ch0[1-9]-*/*.md that has a ## Micro-Parsons section.
"""
import base64, glob, itertools, json, math, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CAP = 40000  # max distinct orders searched per question


def parse(path):
    txt = open(path, encoding='utf-8').read()
    m = re.search(r'^## Micro-Parsons\n', txt, re.M)
    if not m:
        return None
    start = m.end()
    n = re.search(r'^## ', txt[start:], re.M)
    end = start + n.start() if n else len(txt)
    sec = txt[start:end]
    lines = sec.split('\n')
    frags = {}
    i = 0
    letters = []
    while i < len(lines):
        mm = re.match(r'^- ([a-z])\. ?(.*)$', lines[i])
        if mm:
            L, rest = mm.group(1), mm.group(2)
            spans = re.findall(r'`([^`]*)`', rest)
            if spans and not rest.startswith('*'):
                frags[L] = spans
            else:
                # italic note then fenced block indented by two spaces
                j = i + 1
                while not lines[j].startswith('  ```'):
                    j += 1
                k = j + 1
                body = []
                while not lines[k].startswith('  ```'):
                    body.append(lines[k][2:] if lines[k].startswith('  ') else lines[k])
                    k += 1
                frags[L] = body
                i = k
            letters.append(L)
        i += 1
    ans = re.search(r'^\*\*Answer:\*\* (.*)$', sec, re.M)
    answer = [x.strip() for x in ans.group(1).split(',')]
    inter = re.search(r'^\*\*Interchangeable:\*\* (.*)$', sec, re.M)
    also = re.search(r'^\*\*Also accepted:\*\* (.*)$', sec, re.M)
    also_orders = []
    if also:
        also_orders = [[x.strip() for x in o.split(',')] for o in also.group(1).split(';')]
    # final code block after Answer
    after = sec[ans.end():]
    cb = re.search(r'^```java\n(.*?)^```$', after, re.M | re.S)
    code = cb.group(1).rstrip('\n').split('\n')
    return dict(path=path, txt=txt, sec_start=start, sec_end=end, frags=frags, letters=letters,
                answer=answer, inter=inter.group(1) if inter else None, also=also_orders,
                has_also=bool(also), code=code)


def delta(lines):
    t = '\n'.join(lines)
    return t.count('{') - t.count('}')


def kind(lines):
    t = '\n'.join(lines).strip()
    d = delta(lines)
    if d > 0:
        return 'open'
    if d < 0:
        return 'close'
    if t.endswith(';') or t.startswith('//'):
        return 'stmt'
    if t.startswith('{') and t.endswith('}'):
        return 'body'
    return 'head'


MOD = r'(?:public|private|protected|static|final|abstract)'
CLASS_STMT = re.compile(r'^\s*' + MOD + r'?\s*(?:' + MOD + r'\s+)*[\w<>\[\],.? ]+\s+\w+\s*(=.*)?;$', re.S)


def make_atoms(F, order, pool=None):
    """Glue header fragments to the opener / single-statement body that follows them."""
    atoms = []
    i, n = 0, len(order)
    while i < n:
        L = order[i]
        k = kind(F[L])
        if k in ('stmt', 'body'):
            atoms.append(dict(l=[L], k='stmt', d=0, t='\n'.join(F[L]).strip())); i += 1; continue
        if k == 'close':
            atoms.append(dict(l=[L], k='close', d=delta(F[L]))); i += 1; continue
        heads = []
        while i < n and kind(F[order[i]]) == 'head':
            heads.append(order[i]); i += 1
        htxt = ' '.join(l.strip() for L2 in heads for l in F[L2] if not l.strip().startswith('/*'))
        if i < n and kind(F[order[i]]) == 'open':
            o = order[i]; i += 1
            if not heads:
                htxt = '\n'.join(F[o]).strip()
            assert delta(F[o]) == 1, 'multi-open fragment'
            if re.search(r'\bclass\b', htxt):
                ctx = 'class'; allow = 'top'
            elif re.match(r'^\s*' + MOD + r'\b.*\(', htxt):
                ctx = 'block'; allow = 'class'
            else:
                ctx = 'block'; allow = 'block'
            if heads and '\n'.join(F[o]).strip() == '{' and pool is not None:
                pool.append(o)
                atoms.append(dict(l=heads + [None], k='open', d=1, ctx=ctx, allow=allow)); continue
            atoms.append(dict(l=heads + [o], k='open', d=1, ctx=ctx, allow=allow)); continue
        if heads and i < n and kind(F[order[i]]) in ('body', 'stmt'):
            b2 = order[i]; i += 1
            atoms.append(dict(l=heads + [b2], k='stmt', d=0, t='block')); continue
        raise AssertionError('dangling header ' + str(heads))
    return atoms


def atom_allowed(a, ctx):
    if a['k'] == 'open':
        return ctx == a['allow']
    if a['k'] == 'stmt':
        t = a['t']
        if t == 'block':
            return ctx == 'block'
        if t.startswith(('import ', 'package ')):
            return ctx == 'top'
        if ctx == 'top':
            return False
        if ctx == 'class':
            return bool(CLASS_STMT.match(t)) and not t.startswith(('return', 'break', 'continue', 'throw'))
        return not re.match(r'^' + MOD + r'\b', t)
    return True


def prefix_ctx(pre):
    stack = ['top']
    prev = ''
    for line in pre:
        s = line.strip()
        if s == '{' or s.endswith('{'):
            h = (s if s != '{' else prev)
            stack.append('class' if re.search(r'\bclass\b', h) else 'block')
        elif s.startswith('}'):
            stack.pop()
        if s:
            prev = s
    return stack


def gen_orders(atoms, base_stack, structured=False):
    """Lazy DFS over atom orders with Java context rules; yields letter lists.
    structured=True additionally requires each block to contain exactly the atoms it has in the
    Answer (used only when the full search is too large)."""
    n = len(atoms)
    used = [False] * n
    out = []          # indices of placed atoms
    members = {}
    if structured:
        st = []
        for idx, a in enumerate(atoms):
            if a['k'] == 'close':
                for _ in range(-a['d']):
                    st.pop()
            for o in st:
                members[o].add(idx)
            if a['k'] == 'open':
                st.append(idx); members[idx] = set()
    starts = []       # (atom index of open, position in out)

    def rec(stack):
        if len(out) == n:
            if len(stack) == len(base_stack):
                yield [L for i in out for L in atoms[i]['l']]
            return
        for i in range(n):
            if used[i]:
                continue
            a = atoms[i]
            if not atom_allowed(a, stack[-1]):
                continue
            popped = None
            if a['k'] == 'close':
                k = -a['d']
                if len(stack) - k < len(base_stack):
                    continue
                if structured and k == 1 and starts:
                    oi, pos = starts[-1]
                    if set(out[pos + 1:]) != members[oi]:
                        continue
                ns = stack[:len(stack) - k]
            elif a['k'] == 'open':
                ns = stack + [a['ctx']]
            else:
                ns = stack
            used[i] = True
            out.append(i)
            if a['k'] == 'open':
                starts.append((i, len(out) - 1))
            elif a['k'] == 'close' and -a['d'] == 1 and starts:
                popped = starts.pop()
            yield from rec(ns)
            if a['k'] == 'open':
                starts.pop()
            elif popped:
                starts.append(popped)
            out.pop()
            used[i] = False

    yield from rec(list(base_stack))


def locate(q, order):
    F = q['frags']
    A = []
    for L in order:
        A += F[L]
    C = [l for l in q['code'] if l.strip() != '']
    hits = [k for k in range(len(C) - len(A) + 1) if C[k:k + len(A)] == A]
    if len(hits) != 1:
        return None
    k = hits[0]
    return C[:k], C[k + len(A):]


def assemble(q, order, scaf):
    pre, suf = scaf
    lines = list(pre)
    for L in order:
        lines += q['frags'][L]
    lines += suf
    return '\n'.join(lines) + '\n'


def canon(q, order):
    """Identical-text fragments: reassign letters in Answer order of appearance."""
    F = q['frags']
    ans_pos = {L: i for i, L in enumerate(q['answer'])}
    groups = {}
    for L in q['letters']:
        groups.setdefault(tuple(F[L]), []).append(L)
    out = list(order)
    for g in groups.values():
        if len(g) > 1:
            idx = [i for i, L in enumerate(order) if L in g]
            letters = sorted((order[i] for i in idx), key=lambda L: ans_pos[L])
            for i, L in zip(idx, letters):
                out[i] = L
    return out


def layout_ok(text):
    """Joe's rule (10-28-2026): every { follows its own header at the same indentation, every } matches the
    indentation of the line that opened its block, every line inside a block is indented deeper than that line."""
    ind = lambda s: len(s) - len(s.lstrip(' '))
    stack = []   # indentation of the opener (header) line of each open block
    prev = None  # previous nonblank line
    for line in text.split('\n'):
        if not line.strip():
            continue
        s = line.strip()
        if s == '{':
            if prev is None or prev.strip().endswith((';', '{', '}')) or ind(prev) != ind(line):
                return False
            stack.append(ind(prev))
        else:
            if s.startswith('}'):
                if not stack or ind(line) != stack[-1]:
                    return False
                stack.pop()
                # a line like '} else {' is not used in these exercises
            else:
                if stack and ind(line) <= stack[-1]:
                    return False
                if s.endswith('{') and not s.startswith('{'):
                    stack.append(ind(line))
        prev = line
    return not stack


import re as _re
_LIT = _re.compile(r'("(?:[^"\\]|\\.)*")|(?<![\w.])(\d+\.\d+|\d+)(?![\w.])|\b(true|false)\b')


def mutate(text, mode):
    def f(m):
        if m.group(1):
            return m.group(1)
        if m.group(3):
            return 'false' if m.group(3) == 'true' else 'true'
        n = m.group(2)
        if '.' in n:
            return str(float(n) + (3.5 if mode == 0 else 11.25))
        return str(int(n) + (3 if mode == 0 else 7))
    return _LIT.sub(f, text)


def luck_ok(q, scaf, orders, ans_text):
    """True per order if it still matches the Answer under changed literal values (two mutations)."""
    if not orders:
        return []
    ok = [True] * len(orders)
    for mode in (0, 1):
        base = run_java([mutate(ans_text, mode)])[0]
        texts = [mutate(assemble(q, o, scaf), mode) for o in orders]
        for i0 in range(0, len(texts), 200):
            for j, rr in enumerate(run_java(texts[i0:i0 + 200])):
                if rr != base:
                    ok[i0 + j] = False
    return ok


def run_java(sources, stdin_path=None):
    """sources: list of program texts. Returns list of (status, stdout_bytes_or_err)."""
    with tempfile.TemporaryDirectory() as d:
        for i, s in enumerate(sources):
            open(os.path.join(d, f'{i}.java'), 'w', encoding='utf-8').write(s)
        cmd = ['systemd-run', '--user', '--scope', '-q', '-p', 'MemoryMax=1500M', '-p', 'MemorySwapMax=0', 'java', '-Xmx384m', os.path.join(HERE, 'Runner.java'), d, os.path.join(HERE, 'stubs')]
        if stdin_path:
            cmd.append(stdin_path)
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=HERE, timeout=3000)
        res = {}
        for line in p.stdout.splitlines():
            parts = line.split('\t')
            if len(parts) == 3:
                res[int(parts[0])] = (parts[1], base64.b64decode(parts[2]))
        if len(res) != len(sources):
            raise RuntimeError('runner failure: ' + p.stderr[:2000])
        return [res[i] for i in range(len(sources))]


def analyze(path):
    q = parse(path)
    if q is None:
        return None
    r = dict(file=os.path.relpath(path, ROOT), flags=[], found=[], surprising=[])
    F = q['frags']
    if sorted(q['answer']) != sorted(q['letters']):
        r['flags'].append('Answer letters do not match fragment letters'); return r
    scaf = locate(q, q['answer'])
    if scaf is None:
        r['flags'].append('could not locate assembled Answer in the final code block (scaffold)'); return r
    try:
        pool = []
        atoms = make_atoms(F, q['answer'], pool)
    except AssertionError as e:
        r['flags'].append('structure parse: ' + str(e)); return r
    base_stack = prefix_ctx(scaf[0])
    r['search_space'] = None
    orders_iter = gen_orders(atoms, base_stack)
    # cheap pre-count (no compiling): fall back to a block-contiguous search if the full space is too big
    cnt = sum(1 for _ in itertools.islice(gen_orders(atoms, base_stack), 30001))
    if cnt > 30000:
        orders_iter = gen_orders(atoms, base_stack, structured=True)
        r['flags'].append('NOT EXHAUSTIVELY SEARCHED: full space over 30000 orders; searched every order that keeps each block contiguous (block bodies permuted, whole blocks permuted)')
    ans_text = assemble(q, q['answer'], scaf)
    ans_res = run_java([ans_text])[0]
    r['answer_status'] = ans_res[0]
    if ans_res[0] != 'OK':
        r['flags'].append(f'Answer program status {ans_res[0]}')
    correct, ncand, ncomp = [], 0, 0
    chunk = []

    def flush():
        nonlocal ncomp
        if not chunk:
            return
        res = run_java([t for t, _ in chunk])
        for (t, c), rr in zip(chunk, res):
            if rr[0] != 'COMPILE_ERR':
                ncomp += 1
            if rr == ans_res and rr[0] != 'COMPILE_ERR' and t != ans_text:
                correct.append(c)
        chunk.clear()

    seen = set()
    def expand(s0):
        if not pool:
            yield s0
            return
        pos = [i for i, L in enumerate(s0) if L is None]
        for perm in itertools.permutations(pool):
            s1 = list(s0)
            for i, L in zip(pos, perm):
                s1[i] = L
            yield s1

    def expanded():
        for s0 in orders_iter:
            yield from expand(s0)

    for s0 in expanded():
        s = canon(q, s0)
        h = hash(tuple(s))
        if h in seen:
            continue
        seen.add(h)
        t0 = assemble(q, s, scaf)
        if not layout_ok(t0):
            r['layout_dropped'] = r.get('layout_dropped', 0) + 1
            continue
        ncand += 1
        if ncand > CAP:
            r['flags'].append('more than %d candidate orders; stopped' % CAP)
            return r
        chunk.append((assemble(q, s, scaf), s))
        if len(chunk) >= 200:
            flush()
    flush()
    r['found'] = correct
    import classify
    cl = classify.classify(q, correct)
    excl = [o for k in ('cross', 'prints', 'other') for o in cl[k]]
    exs = {tuple(o) for o in excl}
    r['excluded'] = excl
    r['excluded_counts'] = {k: len(cl[k]) for k in ('cross', 'prints', 'other')}
    r['blocks_count'] = len(cl['blocks'])
    correct = [o for o in correct if tuple(o) not in exs]
    # luck test: same literal mutations applied to Answer and candidate must still agree
    flags_ok = luck_ok(q, scaf, correct, ans_text)
    lucky = [o for o, ok in zip(correct, flags_ok) if not ok]
    correct = [o for o, ok in zip(correct, flags_ok) if ok]
    r['lucky'] = lucky
    r['kept'] = correct
    r['candidates'] = ncand
    r['compile_ok'] = ncomp
    mism = []
    written_texts = set()
    also_t = [(o, assemble(q, o, scaf)) for o in q['also']]
    for i0 in range(0, len(also_t), 200):
        part = also_t[i0:i0 + 200]
        res = run_java([t for _, t in part])
        for (o, t), rr in zip(part, res):
            if t == ans_text:
                mism.append((o, 'equals the Answer'))
            elif rr != ans_res:
                mism.append((o, f'differs: {rr[0]} {rr[1][:80]!r}'))
            written_texts.add(t)
    missing = [c for c in correct if assemble(q, c, scaf) not in written_texts]
    wrongly = [o for o in q['also'] if tuple(o) in exs]
    mism += [(o, 'brace layout wrong') for o in q['also'] if not layout_ok(assemble(q, o, scaf))]
    lk = luck_ok(q, scaf, q['also'], ans_text)
    mism += [(o, 'matches only by luck (changed values differ)') for o, k in zip(q['also'], lk) if not k]
    mism += [(o, 'is an excluded coincidence order') for o in wrongly]
    r['mismatch_written'] = mism
    r['missing_from_written'] = missing
    r['written_count'] = len(q['also'])
    # surprising: any found order where a method/head unit moved relative to the Answer is noted by caller
    r['q'] = q
    r['scaf_note'] = (len(scaf[0]), len(scaf[1]))
    return r


def also_line(orders):
    return '**Also accepted:** ' + '; '.join(', '.join(o) for o in orders)


def write_also(q, orders):
    """Insert (or replace) the **Also accepted:** line; re-reads the file so other edits are never clobbered."""
    txt = open(q['path'], encoding='utf-8').read()
    m = re.search(r'^## Micro-Parsons\n', txt, re.M)
    start = m.end()
    n = re.search(r'^## ', txt[start:], re.M)
    end = start + n.start() if n else len(txt)
    sec = txt[start:end]
    line = also_line(orders) if orders else None
    if not orders:
        sec = re.sub(r'\n\n\*\*Also accepted:\*\* [^\n]*', '', sec, count=1)
        return txt[:start] + sec + txt[end:]
    if re.search(r'^\*\*Also accepted:\*\* .*$', sec, re.M):
        sec = re.sub(r'^\*\*Also accepted:\*\* .*$', lambda _m: line, sec, count=1, flags=re.M)
    else:
        mm = re.search(r'^\*\*Answer:\*\* .*$', sec, re.M)
        pos = mm.end()
        im = re.match(r'\n\n\*\*Interchangeable:\*\* [^\n]*', sec[pos:])
        if im:
            pos += im.end()
        sec = sec[:pos] + '\n\n' + line + sec[pos:]
    return txt[:start] + sec + txt[end:]


def main():
    args = sys.argv[1:]
    write = '--write' in args
    jout = None
    if '--json' in args:
        jout = args[args.index('--json') + 1]
    files = [a for a in args if a.endswith('.md')]
    if not files:
        files = sorted(glob.glob(os.path.join(ROOT, 'exercises', 'ch0[1-9]-*', '*.md')))
    results = []
    tot_q = tot_found = tot_written_ok = tot_mism = tot_missing = 0
    for f in files:
        r = analyze(f)
        if r is None:
            continue
        tot_q += 1
        q = r.pop('q', None)
        if 'found' in r:
            tot_found += len(r.get('kept', []))
        mism = len(r.get('mismatch_written', []))
        miss = len(r.get('missing_from_written', []))
        tot_mism += mism
        tot_missing += miss
        tot_written_ok += r.get('written_count', 0) - mism
        if write and q is not None and all(f.startswith('NOT EXHAUSTIVELY') for f in r['flags']) and (r.get('kept') or q['has_also']):
            new = write_also(q, r.get('kept', []))
            open(f, 'w', encoding='utf-8').write(new)
            r['wrote'] = True
        results.append(r)
        print(f"{r['file']}: space={r.get('search_space')} cand={r.get('candidates')} compiled={r.get('compile_ok')} "
              f"found={len(r.get('found', []))} kept={len(r.get('kept', []))} lucky={len(r.get('lucky', []))} layout_dropped={r.get('layout_dropped', 0)} written={r.get('written_count')} mism={mism} missing={miss} flags={r['flags']}")
    print(f"\nQUESTIONS CHECKED: {tot_q}\nCORRECT ORDERS FOUND (other than Answer): {tot_found}\n"
          f"ORDERS WRITTEN AND VERIFIED: {tot_written_ok}\nMISMATCHES (written order wrong): {tot_mism}\n"
          f"MISSING (found but not written): {tot_missing}")
    if jout:
        json.dump(results, open(jout, 'w'), indent=1)


if __name__ == '__main__':
    main()
