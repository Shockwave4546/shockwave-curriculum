import sys; sys.path.insert(0,'.')
import parsons_orders as p, os
f=[x for x in __import__('glob').glob(p.ROOT+'/exercises/ch25*/*.md') if sys.argv[1] in x][0]
q=p.parse_section(f); off,s,n=p.locate(q); key=os.path.basename(f); c=p.ctx_for(key)
r=p.run_batch({"0":p.build(q,key,q["answer"],off,s,n)},c["main"],None,c["cp"])
print(r["0"][0], r["0"][2].decode())
