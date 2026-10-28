import sys, glob, os; sys.path.insert(0,'.')
import parsons_orders as p
for f in sorted(glob.glob(p.ROOT+'/exercises/ch2[0-8]-*/*.md')+glob.glob(p.ROOT+'/exercises/ch19-*/*.md')):
    if '## Micro-Parsons' not in open(f).read(): continue
    q=p.parse_section(f); off,s,n=p.locate(q)
    k=os.path.basename(f)
    print(k, len(q['answer']), p.count_orders(q,off,k,cap=2_000_000), p.descents(q,off), flush=True)
