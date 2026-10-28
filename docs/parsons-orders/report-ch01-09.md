# Micro-Parsons orders, chapters 1-9

Harness: `tools/parsons_orders/ch01-09/` (`parsons_orders.py`, `Runner.java`, `classify.py`, `stubs/`, `run.sh`). Run as `tools/parsons_orders/ch01-09/run.sh` (wraps `systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0`, one JVM at a time with `-Xmx384m`, batches of 200 classes, lazy permutations, only passing orders kept). Add `--write` to insert/replace the `**Also accepted:**` lines, `--json out.json` to dump results.

## Final harness output (verification run on the edited files, no `--write`)

```
QUESTIONS CHECKED: 41
CORRECT ORDERS FOUND (other than Answer): 93
ORDERS WRITTEN AND VERIFIED: 93
MISMATCHES (written order wrong): 0
MISSING (found but not written): 0
```

Totals: q=41, kept=93, excl=142, probs=7, whys=8, mism=0, miss=0 (q=questions, kept=orders listed in Also accepted, excl=orders found but deliberately not listed, probs/whys=texts changed).

## How the search works

- Fragments are glued into atoms: header fragments + the opener (or merged one-statement body) that follows them. Pure `{` fragments are a pool that may fill any header slot; candidates are then dropped unless the assembled code is properly laid out (Joe's 10-28-2026 brace rule: each `{` follows its own header at the same indentation, each `}` matches its block opener's indentation, block contents are indented deeper). That drops every brace-indentation swap and bare block. Every ordering of atoms is generated lazily by a DFS that applies Java context rules (only `import`/`package`/class at top level, only members in a class body, only statements in a method body, braces balanced), keeping the scaffold from the Problem text around the fragments. Every candidate is compiled and run by `Runner.java` (in memory, stubs on the source path) and must match the Answer program's stdout and exit status exactly.
- Luck test (Joe's 10-28-2026 rule): every surviving order is re-run, together with the Answer, with all numeric literals changed (two different shifts) and `true`/`false` flipped; it must still print the same as the Answer under both. Orders that print the same only because of the sample data are not listed. The luck test dropped none beyond the ones `classify.py` had already excluded (statement moved to a different block, or `println`s reordered), so those exclusions stand.
- Identical-text fragments (e.g. two `    }` lines) are listed once, using the Answer's letter assignment.
- Fixed stdin: none of chapters 1-9 reads input. 9.8 reads `matchLog.txt`; the harness folder holds a 4-line fixture (`matchLog.txt`) that both the Answer and every candidate read.
- Stubs (never in exercise files): `Encoder` (fresh reading 42.0, `reset()` zeroes it, so read-before-reset differs), `Elevator` (`moveToPosition` stores the height `getPosition` returns), `DigitalOutput`, `Timer`. Used by 3.1, 3.3, 4.4, 4.5, 4.6.

## Per question

| File | Q | Orders added | Excluded (see Flagged) | Problem text | Why text |
|---|---|---|---|---|---|
| 1.2-intro-to-algorithms-programming-and-compilers.md | 1 | 0 | 0 | unchanged | unchanged |
| 2.1-variables-and-data-types.md | 1 | 2 | 0 | changed: "Declare and assign the cable length first (in two separate steps), then declare and assign `isLocked`, in that order." -> "Declare the cable length and assign it in two separate steps, and declare and assign `isLocked`." | changed |
| 2.2-expressions-and-output.md | 1 | 0 | 0 | unchanged | unchanged |
| 2.3-assignment-and-input.md | 1 | 0 | 0 | unchanged | unchanged |
| 2.4-casting-and-ranges-of-values.md | 1 | 0 | 0 | unchanged | unchanged |
| 2.5-compound-assignment-operators.md | 1 | 2 | 0 | changed: "Declare `climbExtension` first, then `maxExtension`, in that order." -> "Declare both `climbExtension` and `maxExtension`." | changed |
| 3.1-apis-and-libraries.md | 1 | 0 | 0 | unchanged | unchanged |
| 3.2-documentation-with-comments-and-preconditions.md | 1 | 1 | 0 | changed: "Put `main` first and the documented `rawToPercent` method below it." -> "`main` and the documented `rawToPercent` method can come in either order." | changed |
| 3.3-packages-and-imports.md | 1 | 0 | 0 | unchanged | unchanged |
| 4.1-methods-signatures-and-parameters.md | 1 | 1 | 0 | changed: "Put `main` first and the `reportMatchScore` method below it." -> "`main` and the `reportMatchScore` method can come in either order." | changed |
| 4.2-calling-class-methods.md | 1 | 1 | 0 | changed: "Put `main` first and the `toPercent` method below it." -> "`main` and the `toPercent` method can come in either order." | unchanged |
| 4.3-using-the-math-class.md | 1 | 1 | 0 | unchanged | unchanged |
| 4.4-objects-instances-of-classes.md | 1 | 23 | 96 (cross 96) | unchanged | changed |
| 4.5-creating-and-initializing-objects-constructors.md | 1 | 11 | 0 | unchanged | changed |
| 4.6-calling-instance-methods.md | 1 | 0 | 0 | unchanged | unchanged |
| 5.1-5.2-if-statements-and-for-loops.md | 1 | 0 | 2 (cross 2) | unchanged | unchanged |
| 5.10-nested-iteration.md | 1 | 0 | 0 | unchanged | unchanged |
| 5.11-informal-runtime-analysis-of-loops.md | 1 | 0 | 0 | unchanged | unchanged |
| 5.12-switch-statements-and-expressions.md | 1 | 5 | 0 | unchanged | unchanged |
| 5.3-algorithms-with-selection-and-repetition.md | 1 | 0 | 2 (cross 2) | unchanged | unchanged |
| 5.4-boolean-expressions.md | 1 | 1 | 3 (prints 3) | unchanged | unchanged |
| 5.5-nested-if-statements.md | 1 | 0 | 0 | unchanged | unchanged |
| 5.6-compound-boolean-expressions.md | 1 | 0 | 0 | unchanged | unchanged |
| 5.7-comparing-boolean-expressions-de-morgans-laws.md | 1 | 1 | 0 | unchanged | unchanged |
| 5.8-while-loops.md | 1 | 1 | 0 | unchanged | unchanged |
| 5.9-implementing-selection-and-iteration-algorithms.md | 1 | 0 | 0 | unchanged | unchanged |
| 6.1-strings.md | 1 | 0 | 0 | unchanged | unchanged |
| 6.2-string-algorithms.md | 1 | 1 | 0 | unchanged | unchanged |
| 7.1-anatomy-of-a-java-class.md | 1 | 23 | 0 | unchanged | unchanged |
| 7.2-methods-how-to-write-them.md | 1 | 5 | 0 | changed: "the field, then its getter, then its setter." -> "the field, its getter and its setter." | changed |
| 7.3-methods-passing-and-returning-references-of-an-object.md | 1 | 5 | 36 (cross 36) | unchanged | unchanged |
| 7.4-class-static-variables-and-methods.md | 1 | 3 | 0 | unchanged | unchanged |
| 8.1-8.2-constructors-and-this.md | 1 | 3 | 0 | changed: "Order the class body as: the field first, then the constructor, then `main`." -> "The class body holds the field, the constructor and `main`." | changed |
| 9.1-array-creation-and-access.md | 1 | 0 | 0 | unchanged | unchanged |
| 9.2-arraylist-and-its-methods.md | 1 | 0 | 0 | unchanged | unchanged |
| 9.3-optional-hashmap-dictionary-data-structure.md | 1 | 0 | 0 | unchanged | unchanged |
| 9.4-array-traversals.md | 1 | 0 | 0 | unchanged | unchanged |
| 9.5-implementing-array-algorithms.md | 1 | 0 | 2 (cross 2) | unchanged | unchanged |
| 9.6-arraylist-traversals.md | 1 | 0 | 1 (cross 1) | unchanged | unchanged |
| 9.7-implementing-arraylist-algorithms.md | 1 | 0 | 0 | unchanged | unchanged |
| 9.8-using-text-files.md | 1 | 3 | 0 | unchanged | unchanged |

Why-text changes: 2.1 and 2.5 (the "Problem text pins that order" sentences replaced by which lines can move), 3.2 and 4.1 ("as the problem asks" removed, method order stated as free), 4.4 (confirmation message can go anywhere in `main`), 4.5 (comment and confirmation message can go anywhere in `main`; `a` before `h` kept), 7.2 (getter/setter/field order stated as free), 8.1 (the "Problem text pins the required order" paragraph replaced).

## Flagged for Joe

1. **9.8 is not exhaustively searched.** The full space is over 30,000 orders (10 movable pieces). The harness searched every order that keeps each block's contents together (block bodies permuted, whole blocks permuted): 240 candidates. Result: 3 orders (`c`/`d` swap, already Interchangeable; `g`/`h` swap; both). 9.8 reads `matchLog.txt`; I used a 4-line fixture in the harness folder.
2. **3.1: the Problem fixes "reset, then read", which does have a real effect** on a real `Encoder`. The local check rests on my stub (`Encoder` starts at 42.0, `reset()` zeroes it); real WPILib can't run here. Problem text unchanged; only the Answer's order is accepted. Please confirm that is what you want.
3. **Stubs stand in for non-JDK classes** (3.1, 3.3, 4.4, 4.5, 4.6): `Encoder`, `Elevator`, `DigitalOutput`, `Timer`. 4.6's `moveToPosition` / `getPosition` order is checked only against my stub.
4. **7.1, 7.3 and 7.4 still say members are declared "per the usual order / conventionally".** Descriptions, not demands, so left alone.

Settled by Joe's 10-28-2026 decisions (no longer flags): the luck-only orders stay out (4.4: 96 excluded, 5.1-5.2: 2, 5.3: 2, 5.4: 3, 7.3: 36, 9.5: 2, 9.6: 1), and brace-indentation swaps / bare blocks are not accepted (they removed the 3-order lists and all of 9.5).

## Surprising correct orders (listed in Also accepted)

- **Method and member order** (Java doesn't care): 3.2 (`rawToPercent` before `main`), 4.1 and 4.2 (method before `main`), 7.1 (members reordered), 7.2 (getter/setter/field order), 7.3 (5 orders: field, constructor, `main` order), 7.4, 8.1.
- **Fused-brace fragments**: in 4.1 and 4.2 the merged `}` / `}` fragment ends whichever method comes last, so the brace fragments swap roles with a method moved before `main`. Layout stays correct.
- **Free statements**: 2.1 (`isLocked` anywhere after `g`, before `j`), 2.5 (`maxExtension`), 4.4 (23 orders: `println` before the lights, lights in any order), 4.5 (the comment and the `println` anywhere in `main`).
- 22 of 41 questions now have no Also accepted line, because the Answer is the only properly laid-out order.
