#!/usr/bin/env python3
"""Build docs/parsons-orders/report-ch01-09.md from a harness --json run: make_report.py run.json harness_output.txt"""
import json, os, sys
import parsons_orders as P

res = json.load(open(sys.argv[1]))
out_txt = open(sys.argv[2]).read().strip()

PC = {  # file prefix -> (old Problem wording, new Problem wording) ; Why changed noted separately
 '2.1-': ("Declare and assign the cable length first (in two separate steps), then declare and assign `isLocked`, in that order.",
          "Declare the cable length and assign it in two separate steps, and declare and assign `isLocked`."),
 '2.5-': ("Declare `climbExtension` first, then `maxExtension`, in that order.", "Declare both `climbExtension` and `maxExtension`."),
 '3.2-': ("Put `main` first and the documented `rawToPercent` method below it.", "`main` and the documented `rawToPercent` method can come in either order."),
 '4.1-': ("Put `main` first and the `reportMatchScore` method below it.", "`main` and the `reportMatchScore` method can come in either order."),
 '4.2-': ("Put `main` first and the `toPercent` method below it.", "`main` and the `toPercent` method can come in either order."),
 '7.2-': ("the field, then its getter, then its setter.", "the field, its getter and its setter."),
 '8.1-': ("Order the class body as: the field first, then the constructor, then `main`.", "The class body holds the field, the constructor and `main`."),
}
WHY = {'2.1-', '2.5-', '3.2-', '4.1-', '4.4-', '4.5-', '7.2-', '8.1-'}

def key(r):
    n = os.path.basename(r['file'])
    return n

rows = []
tot = dict(q=0, kept=0, excl=0, probs=0, whys=0, mism=0, miss=0)
for r in res:
    n = key(r)
    pre = n.split('-')[0] + '-'
    if n.startswith('5.1-5.2'):
        pre = '5.1-5.2'
    ex = r.get('excluded_counts', {})
    exn = sum(ex.values())
    kept = len(r.get('kept', []))
    prob = PC.get(pre)
    why = pre in WHY
    tot['q'] += 1; tot['kept'] += kept; tot['excl'] += exn
    tot['probs'] += 1 if prob else 0; tot['whys'] += 1 if why else 0
    tot['mism'] += len(r.get('mismatch_written', [])); tot['miss'] += len(r.get('missing_from_written', []))
    fl = '; '.join(r['flags']) if r['flags'] else ''
    rows.append((n, kept, exn, ex, r.get('blocks_count', 0), prob, why, fl, r.get('candidates')))

L = []
L.append('# Micro-Parsons orders, chapters 1-9\n')
L.append('Harness: `tools/parsons_orders/ch01-09/` (`parsons_orders.py`, `Runner.java`, `classify.py`, `stubs/`, `run.sh`). '
         'Run as `tools/parsons_orders/ch01-09/run.sh` (wraps `systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0`, one JVM at a time with `-Xmx384m`, batches of 200 classes, lazy permutations, only passing orders kept). '
         'Add `--write` to insert/replace the `**Also accepted:**` lines, `--json out.json` to dump results.\n')
L.append('## Final harness output (verification run on the edited files, no `--write`)\n')
L.append('```\n' + out_txt.split('\n\n')[-1] + '\n```\n')
L.append('Totals: ' + ', '.join(f'{k}={v}' for k, v in tot.items()) + ' (q=questions, kept=orders listed in Also accepted, excl=orders found but deliberately not listed, probs/whys=texts changed).\n')
L.append('## How the search works\n')
L.append('- Fragments are glued into atoms: header fragments + the opener (or merged one-statement body) that follows them. Pure `{` fragments are a pool that may fill any header slot (so `{` fragments that differ only by indentation can swap, as the brief requires). Every ordering of atoms is generated lazily by a DFS that applies Java context rules (only `import`/`package`/class at top level, only members in a class body, only statements in a method body, braces balanced), keeping the scaffold from the Problem text around the fragments. Every candidate is compiled and run by `Runner.java` (in memory, stubs on the source path) and must match the Answer program\'s stdout and exit status exactly.\n'
         '- Identical-text fragments (e.g. two `    }` lines) are listed once, using the Answer\'s letter assignment.\n'
         '- Fixed stdin: none of chapters 1-9 reads input. 9.8 reads `matchLog.txt`; the harness folder holds a 4-line fixture (`matchLog.txt`) that both the Answer and every candidate read.\n'
         '- Stubs (never in exercise files): `Encoder` (fresh reading 42.0, `reset()` zeroes it, so read-before-reset differs), `Elevator` (`moveToPosition` stores the height `getPosition` returns), `DigitalOutput`, `Timer`. Used by 3.1, 3.3, 4.4, 4.5, 4.6.\n')
L.append('## Per question\n')
L.append('| File | Q | Orders added | Excluded (see Flagged) | Problem text | Why text |')
L.append('|---|---|---|---|---|---|')
for n, kept, exn, ex, blk, prob, why, fl, cand in rows:
    pt = f'changed: "{prob[0]}" -> "{prob[1]}"' if prob else 'unchanged'
    exs = f"{exn} ({', '.join(f'{k} {v}' for k, v in ex.items() if v)})" if exn else '0'
    L.append(f'| {n} | 1 | {kept} | {exs} | {pt} | {"changed" if why else "unchanged"} |')
L.append('\nWhy-text changes: 2.1 and 2.5 (the "Problem text pins that order" sentences replaced by which lines can move), 3.2 and 4.1 ("as the problem asks" removed, method order stated as free), 4.4 (confirmation message can go anywhere in `main`), 4.5 (comment and confirmation message can go anywhere in `main`; `a` before `h` kept), 7.2 (getter/setter/field order stated as free), 8.1 (the "Problem text pins the required order" paragraph replaced).\n')
L.append('## Flagged for Joe\n')
L.append('@@FLAGGED@@')
L.append('## Surprising correct orders (listed in Also accepted)\n')
L.append('@@SURPRISING@@')
open(sys.argv[3], 'w').write('\n'.join(L))
