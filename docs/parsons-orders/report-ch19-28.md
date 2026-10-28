# Report: Micro-Parsons correct orders, chapters 19-28

Written 2026-10-28; second pass applied the 10-28-2026 decisions (no orders that match only by luck; braces stay with their block; 19.1 outside-lambda orders removed). Harness: `tools/parsons_orders/ch19-28/` (`Runner.java`, `parsons_orders.py`, `run_all.sh`, `ctx/ch25_cmd.py`).
Only `exercises/ch19-*` to `exercises/ch28-*` Micro-Parsons sections were edited. Nothing committed.

## Harness command and final output

```
tools/parsons_orders/ch19-28/run_all.sh search --write   # regenerate the Also accepted lines
tools/parsons_orders/ch19-28/run_all.sh check            # re-verify what is in the files
# each question runs under systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0 python3 parsons_orders.py ...
# one JVM at a time (-Xmx384m), 300 candidates per batch, lazy generation, only passing orders kept
```

Final `check` run: 20 questions checked, 42 Also-accepted orders + 20 Answers = 62 orders verified. Every listed order
compiles and matches the Answer (stdout and exit status) on the original input and under every input variant,
passes the layout rule, and every order the search finds is on the list. **Mismatches: 1**, and it is not a failing
listed order: it is the existing `**Interchangeable:** (a, i)` line in 24, which is no longer true (see Flagged 1). Everything else is 0.

How an order is judged now: assembled into the Answer's scaffold (exact fragment text, indentation offset), then
1. **layout rule** (`layout_ok`): a `{` alone must follow its header line at the same indent; a `}` must have the indent of the line that opened its block; every line inside a block must be indented more than the opener. Moving whole methods/members with their own braces still passes.
2. compiled in one JVM with javac and run; stdout and exit status must equal the Answer's;
3. re-run with changed input values (`VARIANTS` in `parsons_orders.py`, now defined for every question whose output depends on data, 19 through 28); an order that stops matching under any variant is dropped;
4. 19.1 only: the lambda header `d` must come before the declarations `f` and `c` (Joe's decision), via `REQUIRE_BEFORE`.

Ch.25.2/25.6/25.7 have no `main`, so harness-only driver classes in `ctx/ch25_cmd.py` call the factory methods and print what
the real WPILib Commands v3 scheduler does (jars from `~/piston-data/packages/java/25.0.1/wpilib`). Piston itself wasn't running.

## Questions

Orders added = count on the new `**Also accepted:**` line (not counting the Answer); a dash means no line. "Search": E = exhaustive
(8 or fewer fragments, every permutation); P = partial (see Flagged 4). "Dropped" = orders that were correct on the original input
but failed an input variant (luck). The long lists of the first pass shrank mostly because of the layout rule.

| File | Orders added | Search | Dropped as luck | Problem changed | Why changed |
|---|---|---|---|---|---|
| 19-interfaces-as-contracts.md | - (was 3) | E | 0 | no | no |
| 19.1-lambdas-and-method-references.md | 1 (was 5) | E | 0 | no | no |
| 20-the-io-layer-pattern.md | 1 (was 63) | P | 5 | no | no |
| 21-static-factories.md | 0 (was 48) | P | 0 | no | no |
| 22-the-builder-pattern.md | 5 | E | 0 | no | no |
| 23.1-scope-and-access.md | 1 (was 3) | P | 0 | yes (below) | yes |
| 24-optional-avoiding-null-pointer-exceptions.md | - (was 5) | P | 1 | no | no |
| 25.1-what-is-command-based-programming.md | 2 (was 559) | P | 16 | no | no |
| 25.2-commands-and-command-compositions.md | - (was 25) | P | 0 | no | no |
| 25.3-the-command-scheduler.md | - (was 2) | P | 0 | no | no |
| 25.4-state-machines-logic.md | 1 (was 6) | P | 0 | yes | yes |
| 25.5-managing-transitions.md | 3 (was 138) | P | 0 | no | no |
| 25.6-binding-commands-to-triggers.md | 17 (was 30) | P | 0 | no | yes |
| 25.7-structuring-a-command-based-robot-project.md | - (was 2) | P | 0 | no | no |
| 26-architecture-takeaways.md | 1 (was 5) | P | 0 | yes | yes |
| 27.1-abstraction-and-program-design.md | 1 (was 5) | P | 0 | yes | yes |
| 28.1-searching-algorithms.md | - (was 239) | P | 0 | no | no |
| 28.2-sorting-algorithms.md | 1 (was 6) | P | 0 | no | no |
| 28.3-recursion.md | - (was 31) | E | 0 | no | no |
| 28.4-recursive-searching-and-sorting.md | 2 (was 4) | E | 2 | no | no |

Totals: 20 questions checked, 42 orders added (first pass: 1184), 62 orders verified including Answers, 4 Problem texts changed, 5 Why texts changed.

### Problem text changes (old -> new)

All four still fit, because the orders they allow (field after constructor, class before enum, constant after `main`, `main` before `outputRpm`) are still accepted.
- 23.1: "Keep the field, constructor, and `main` in the usual order a class is written in: the field first, then the constructor, then `main`." -> "The usual style is the field first, then the constructor, then `main`, but Java doesn't require that order."
- 25.4: "Declare the enum first in the file, above the class that uses it." -> "The enum is a separate top-level declaration, outside the class."
- 26: "Declare the constant field before `main`." -> "Declare the constant as a field of the class, not inside `main`."
- 27.1: removed " Declare `outputRpm` above `main`."

### Why text changes

- 23.1: field "declared before the constructor" -> by convention before it, but Java accepts the field anywhere inside the class.
- 25.4: added that the enum could also go after the class (checked with `java GearboxStatus.java`, which prints `LOW`).
- 25.6: fields "have to exist before the constructor can use them" -> by convention first; field initializers run before the constructor body either way.
- 26: added that the field can also go after `main`.
- 27.1: says the two methods can go in either order.

Not changed (order really matters): 27.1 "first 4000, then 6000", 26 "driver first", 22 "then print", 25.3 "in order", `import` before the class in 24, declare-before-use, braces in reverse.

## Lead's follow-up (10-28-2026)

Joe settled the remaining flags:
- **24:** the Interchangeable (a, i) line was deleted, and the Why now says `ifPresent` comes first. Re-check: 0 mismatches.
- **25.2:** `whenExited` stays (real in allwpilib `main`, not yet released). Tracked in `docs/wpilib-version-tracking.md`.
- **Empty blocks (flag 5):** an order that leaves a block empty that the Answer doesn't is now rejected (`empty_blocks()` in `parsons_orders.py`). A full `search --write` + `check` re-run for ch19-28 gave 0 mismatches. 20 now lists 1 order, and 21 lists none.

The flags below are the agent's original wording, kept for the record.

## Flagged for Joe

1. **24: the existing `**Interchangeable:** (a, i)` is no longer true.** It swaps `ifPresent` and the `orElse` println. It only works because `chosenAuto` is `null`: with a real routine the two lines print in a different order (the Why text already says so). The harness reports it as the 1 mismatch. I did not edit the Interchangeable line or the Why (outside what I'm allowed to change). Decision: delete the line, or accept it as is. The same applies to any other Interchangeable line that fails a variant; I found no other (25.1, 28.2, 28.4, 22, 20, 19.1 all pass).
2. **25.2: `.whenExited(` is replaced by `.whenCanceled(`.** Joe is deciding (per coordinator): `whenExited` is not in alpha-7. Every order was found with the replace in place; none are listed for 25.2 anyway after this pass (0), so nothing in the file depends on it, but "no other correct order" for 25.2 is only checked against `whenCanceled`.
3. **25.6 still uses a stub for the controller.** The real `org/wpilib/command3/button/CommandXboxController.class` is in the alpha-7 jar, but it can't load here: `ClassNotFoundException: org.wpilib.telemetry.TelemetryLoggable`. That class is in none of the 10 jars in `~/piston-data/packages/java/25.0.1/wpilib` (checked all with `unzip -l`). It would also need HAL natives to read buttons, so a stub is needed anyway. The stub's `leftBumper()`/`rightBumper()` return real `Trigger`s, with a fake clock for `debounce`. Everything else (Trigger, Scheduler, Command) is the real library. If the missing jar is found, the stub can be dropped.
4. **Not exhaustively searched (more than 8 fragments):** 20, 21, 23.1, 24, 25.1-25.7, 26, 27.1, 28.1, 28.2 (12, 12, 12, 11, 12, 10, 11, 12, 12, 10, 11, 9, 12, 11, 11 fragments). Run instead: every sequence of balanced blocks/statements of the whole Answer, every permutation of every 7-position window, and the inside of every block cut into units. Orders that move many fragments across several blocks at once could be missed. 19, 19.1, 22, 28.3, 28.4 are exhaustive.
5. **Some listed orders are odd but equivalent for every input I tried.** For example 20: `feederIO = new FeederIOReal();` placed before `if (runningOnRobot)` with an empty `{ }` body (the else then overrides it), and 21: `if (onRobot) { } else { return Sim }` followed by `return Real`. They keep the layout rule and match under the variants (including the other value of the flag). Say if you want these removed as well.

Settled and removed from the flags: the old "match only on the fixed input" flag (decision 1), the long-list flag and brace-style flag (decision 2), and 19.1 (four orders removed, Problem unchanged).

## Surprising correct orders (still listed)

- Members moved with their own braces: 27.1 `d, j, i, k, h, c, l, a, f, e, b, g` (`main` before `outputRpm`); 23.1 `b, d, c, f, e, j, a, g, k, h, i, l` (`final` field after the constructor); 25.6 fields after the constructor (most of its 17 orders); 26 `c, g, h, b, f, a, i, e, d` (constant after `main`'s closing brace); 25.4 `b, k, e, j, a, i, c, l, d, h, g, f` (class before enum; confirmed with `java`).
- Independent statements swapped: 22 (all 6 setter orders), 28.2 `temp`/`possibleIndex`, 28.4 `f`/`a` and an `else if` before the match check, 19.1 `f`/`c`.
- 25.1 (2 orders), 25.5 (3 orders): the `pressed`/`print` statements and the transition `if` moved within or after their blocks while keeping the same behavior; all pass every variant.
