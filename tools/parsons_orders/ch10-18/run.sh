#!/bin/bash
# all harness runs go through a memory cap (brief: Memory limits)
exec systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0 python3 "$(dirname "$0")/harness.py" "$@"
