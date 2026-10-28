#!/bin/bash
# usage: run_all.sh search --write | run_all.sh check   (one question at a time, memory-capped)
cd "$(dirname "$0")"
for f in ${FILES:-19-interfaces 19.1 20-the 21-static 22-the 23.1 24-optional 25.1 25.2 25.3 25.4 25.5 25.6 25.7 26-arch 27.1 28.1 28.2 28.3 28.4}; do
  systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0 python3 parsons_orders.py "$@" "$f"
  echo "[exit $? for $f]"
done
