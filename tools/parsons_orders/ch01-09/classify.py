#!/usr/bin/env python3
"""Classify the found orders of each question (reads the --json output of parsons_orders.py).
Categories: brace-only (only brace-only fragments / identical-structure moves), cross-block (a statement or
member ends up in a different block than in the Answer), print-reordered (System.out fragments in a different
relative order), block-order (sibling blocks, e.g. methods, in a different order)."""
import json, sys, os
import parsons_orders as P

ROOT = P.ROOT


def parents(q, order):
    F = q['frags']
    stack = ['<root>']
    par = {}
    last_head = None
    sib = {}
    for L in order:
        k = P.kind(F[L])
        t = '\n'.join(F[L]).strip()
        pure = t in ('{', '}')
        if k == 'close':
            for _ in range(-P.delta(F[L])):
                stack.pop()
            continue
        if k == 'open':
            bid = L if not pure else last_head
            par[bid] = stack[-1]
            sib.setdefault(stack[-1], []).append(bid)
            stack.append(bid)
            if not pure:
                par[L] = par[bid]
            last_head = None
            continue
        if k == 'head':
            last_head = L
            par[L] = stack[-1]
            continue
        par[L] = stack[-1]
        last_head = None
    return par, sib


def classify(q, found):
    F = q['frags']
    A = q['answer']
    pA, sA = parents(q, A)
    out = dict(cross=[], prints=[], blocks=[], other=[])
    pr = [L for L in A if any('System.out' in l for l in F[L])]
    for o in found:
        try:
            po, so = parents(q, o)
        except Exception:
            out['other'].append(o); continue
        # compare parents only for non-pure-brace fragments; identical-text fragments are interchangeable
        cross = any(po.get(L) != pA.get(L) for L in A if '\n'.join(F[L]).strip() not in ('{', '}'))
        if cross:
            out['cross'].append(o); continue
        prs = [L for L in o if L in pr]
        if prs != pr:
            out['prints'].append(o); continue
        if any(so.get(k) != v for k, v in sA.items()):
            out['blocks'].append(o); continue
    return out


if __name__ == '__main__':
    res = json.load(open(sys.argv[1]))
    for r in res:
        if not r.get('found'):
            continue
        q = P.parse(os.path.join(ROOT, r['file']))
        c = classify(q, r['found'])
        print(r['file'].split('/')[-1], 'found', len(r['found']), {k: len(v) for k, v in c.items()})
