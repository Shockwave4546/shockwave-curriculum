#!/bin/bash
# Runs the harness under the memory cap required by docs/parsons-orders/brief.md.
cd "$(dirname "$0")"
exec systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0 python3 -u parsons_orders.py "$@"
