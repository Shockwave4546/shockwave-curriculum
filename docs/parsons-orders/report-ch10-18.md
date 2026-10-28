# Parsons orders report: chapters 10-18 (second pass, Joe's decisions of 10-28-2026)

Harness: `tools/parsons_orders/ch10-18/run.sh check` (wraps `harness.py` in `systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0`; one JVM at a time, `-Xmx384m`, 300 candidates per JVM, lazy permutations, only passing orders kept). `Runner.java` compiles and runs candidates in-process. Chapter 14 has no Micro-Parsons question.

Final output of `run.sh check` (full exhaustive re-search plus verification of every listed order):

    questions_checked=16 orders=32 mismatches=0   (missing from list: 0, not found by search: 0)

Totals: 16 questions checked, 32 orders listed (all verified), Problem text changed in 3 files (13, 16, 17.5), Why text changed in 3 files (13, 16, 17.5), mismatches 0.

## Method

- Search: every permutation of the fragments in each block body (balanced-brace prefixes only), scaffold fixed; whole-unit orders at top and class level; product of valid per-block choices re-run. Largest bodies (12: 302,400; 10.3: 120,960) searched exhaustively. Nothing "not exhaustively searched".
- **Layout rule (decision 2):** before running, each assembled program must have every `{` on the line right after its own header at the same indent (no bare blocks), every `}` at its block's indent, and every line inside a block indented deeper than the block's opening line. Orders failing this are dropped. Moving whole methods or members with their own braces is allowed.
- **No-luck rule (decision 1):** each order that passes on the original data is re-run on changed data, and must match the Answer on every variant (stages in `STAGES` in `harness.py`): 10.2 other array shapes and values; 10.3 other times and days, fastest in first/last row, all equal; 11 other mode; 12 file present with 2 lines, empty, and one line without newline (plus missing, the base run); 13 other string; 15 other strings; 16 other values; 17.3 other roller order, one roller, repeated roller; 17.4 other-type, null, different-id, same object, integer arguments; 18.3 indexes swapped to other classes.

## Per question

| File | Q | Orders listed | Problem changed | Why changed |
|---|---|---|---|---|
| ch10/10.1 | 1 | 0 | no | no |
| ch10/10.2 | 1 | 0 (was 155) | no | no |
| ch10/10.3 | 1 | 0 (was 235) | no | no |
| ch11/11 | 1 | 1 (`d`/`i` swap, same as Interchangeable) | no | no |
| ch12/12 | 1 | 0 | no | no |
| ch13/13 | 1 | 1 (field declared below `main`) | yes: "declared as a field at the top of the class" -> "declared as a field of the class" | yes: "placed at the top of the class as the problem states" -> "conventionally placed at the top of the class, but Java accepts it anywhere in the class body, even below `main`..." |
| ch15/15 | 1 | 3 | no | no |
| ch16/16 | 1 | 23 | yes: removed "Put the class's field and methods above `main`." | yes: field, both methods and `main` can go in any order; field-first/`main`-last is convention |
| ch17/17.1 | 1 | 0 | no | no |
| ch17/17.2 | 1 | 0 | no | no |
| ch17/17.3 | 1 | 0 (was 5) | no | no |
| ch17/17.4 | 1 | 2 (was 5) | no | no |
| ch17/17.5 | 1 | 1 (`fire()` before `announce()`) | yes: "a concrete `announce()` method that prints `Shooting...`, followed by an abstract `fire()` method — write `announce()` first, then `fire()`" -> "a concrete `announce()` method that prints `Shooting...` and an abstract `fire()` method" | yes: "comes next, as the Problem asks" -> "comes next (it could equally go after `fire()`, since method order doesn't matter to Java)" |
| ch18/18.1 | 1 | 0 | no | no |
| ch18/18.2 | 1 | 0 | no | no |
| ch18/18.3 | 1 | 1 (the `f`/`b` swap, same as Interchangeable) (was 27) | no | no |

The `**Also accepted:**` lines that became empty (10.2, 10.3, 12, 17.3) were removed from the files. 17.4's two remaining orders are `f, b, h, g, d, a, e, c` (the Interchangeable swap) and `f, b, h, g, a, d, e, c` (`instanceof` check, cast, then the same-object check; the cast still comes after `instanceof`, so every other-type input still works).

## Settled by the decisions (no longer flagged)

- Brace-indentation swaps and bare blocks (10.2, 10.3, 17.3, 17.4, 18.3): all dropped by the layout rule.
- 18.3 `alerts[1]` assigned inside the loop, 17.4 cast before `instanceof`: dropped (layout and changed-data runs).
- 12: the earlier file-present issue is now part of the standing data variants; nothing is listed.

## Flagged for Joe

1. **15 (3 orders), one decision left.** `i, d, b, f, h, l, e, a, g, k, c, j` (add "Note 2", remove last, then add "Note 1") passes every changed-data run, and an extra probe printing the deque's contents afterward gives the same result as the Answer: the two programs end in the same state for any data, so it is genuinely equivalent, not lucky. Rule 1 doesn't exclude it. It still contradicts the Problem's story ("loads two pieces, then feeds out") and the Why ("`Note 1` must be added before `Note 2`"). Decision: keep it as is, or drop it from the Also accepted line (and keep the other two, which are the `i`/`d` import swap).
2. **Surprising but correct (listed):** 16 accepts `main` before the field and methods and every order of the four members (23 orders); 17.5 accepts `fire()` before `announce()`; 13 accepts the field below `main`.

## Lead's follow-up (10-28-2026)

- **15:** Joe dropped the "Note 2, feed out, then Note 1" order (`i, d, b, f, h, l, e, a, g, k, c, j` and its import-swapped twin) because it contradicts the Problem. The harness keeps them out via `EXCLUDED` in `harness.py`. Re-check for 15: 0 mismatches, and 1 order listed (the import swap).
