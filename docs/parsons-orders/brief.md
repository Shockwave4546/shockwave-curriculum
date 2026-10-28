# Brief: list every correct order in the Micro-Parsons exercises

Written 2026-10-27. This is the brief for the subagent(s) doing the review. Read the whole thing before starting.

## Why

The academy marks a Micro-Parsons answer wrong whenever the order doesn't match the **Answer**
sequence, except for swaps declared in an `**Interchangeable:**` line. Students are being marked wrong for
orders that make no real difference. Example: `exercises/ch02-variables-and-types/2.1-variables-and-data-types.md`.
There, `boolean isLocked = true;` (`i`) can go before `h`, between `h` and `a`, or after `a`, and all
three run identically. Only one of those orders is accepted, and the Problem text says "in that order"
to justify it.

**Joe's decision (2026-10-27):** an order is correct if it **compiles, runs and prints exactly the same
output** as the Answer program. The order in which independent variables are declared or set is not
something we grade. The Problem text no longer fixes an order that has no real effect.

## What to do, for every Micro-Parsons question in `exercises/ch*/`

There are about 81, in every exercise file that has a `## Micro-Parsons` section. Some files have more
than one question.

1. **Find every correct order.** Use the definition above. Verify each order mechanically (see
   "Verification"), never by reasoning alone.
2. **Add them to the file** as one line, its own paragraph, directly after `**Answer:**` (after the
   `**Interchangeable:**` line if there is one) and before the ```java code block:

   ```
   **Also accepted:** b, e, f, g, i, h, a, j, c, d; b, e, f, g, h, i, a, j, c, d
   ```

   - The orders use the same letter format as `**Answer:**` (letters separated by `, `). Separate
     orders with `; `, all on one line, however long.
   - List **every** correct order other than the Answer itself.
   - Fragments with **identical text** (e.g. two `    }` lines) produce the same code whichever letter
     goes where. List such orders **once**, using the letter assignment the Answer uses. Fragments
     that differ only by indentation are different fragments.
   - Keep any existing `**Interchangeable:**` line exactly as it is. The orders it allows still go in
     **Also accepted** too (the list must be complete on its own).
   - If the Answer is the only correct order, add nothing.
3. **Fix the text that fixes an order.**
   - Where the **Problem** text says to do things "in that order", "first … then …", or similar, and
     the order has no real effect, reword it so it no longer demands that order. Keep everything else
     it says.
   - Where the **Why this order** text claims an order is required when it isn't (2.1 says "the
     Problem text pins that order instead"), reword it to say which lines can move and why. Example:
     "`isLocked` doesn't depend on `cableLengthInches`, so `i` can go anywhere after `g` and before
     `j`."
   - Keep the explanations of orders that really matter (declare before use, `println` after its
     values, braces closing in reverse).
4. **Flag, don't change**, when:
   - the Problem text fixes an order that **does** have a real effect, and changing that wording would
     change what the exercise teaches;
   - you can't run the program locally even with stubs (see Verification);
   - the question uses two separate fragment sequences, or anything else this brief doesn't cover;
   - anything is ambiguous.

   Joe decides these.

## What counts as "the same"

- **Same program text up to the order of fragments**: assemble the fragments in the candidate order,
  using exactly the fragment text (indentation included). For fixed-scaffold puzzles, assemble them
  into the scaffold shown in the Problem text.
- **Compiles**, with no compile errors. Warnings are fine.
- **Same standard output, byte for byte**, as the Answer program, and the same exit status. If the
  program reads input (`Scanner`), feed the identical fixed input to both and note it in the report.
- An order that compiles but prints something different is **not** correct. Neither is an order where
  only some fragments compile.

Some orders compile and print the same but look wrong, for example a method moved before another
method in a class. They count as correct: Java doesn't care about method order. List them and mention
them in the report so Joe can see them.

## Verification (required)

The machine has Java 25 (`java File.java` compiles and runs a single file; `javax.tools.ToolProvider`
is available for compiling many sources in one JVM).

Write the harness in `tools/parsons_orders/`, so it stays in the repo. It must:

1. Parse each question's fragments, Answer, scaffold (if any) and `**Also accepted:**` orders from the
   exercise file.
2. **Completeness check (exhaustive search):** generate the candidate orders and run every one.
   - Keep the outer scaffold in its Answer positions: the class line, `main` or method signature lines,
     and their braces.
   - Try **every permutation** of the fragments inside each block body.
   - Where a class has more than one method or block, also try every order of the whole blocks.
   - Compile in batches (many classes per JVM) so this is fast.
   - If one block body has more than 8 movable fragments (over 40,320 orders), don't brute-force it.
     Use dependency reasoning plus targeted runs instead, and flag the question in the report as "not
     exhaustively searched".
3. **Check what you wrote:** re-run the harness on the edited file. Every order in `**Also accepted:**`
   must compile and match the Answer's output. Every order found in step 2 must be in the list or be
   the Answer itself. Report zero mismatches.
4. **Code that can't run as plain Java** (WPILib classes, mostly Ch.25; anything not in the JDK):
   - write minimal stub classes in the harness folder (never in the exercise files) so it compiles and
     runs; or
   - use the local Piston, if it's running (`curl -s localhost:2000/api/v2/runtimes`; see
     `docs/coding-exercises/brief.md` and `tools/piston/`).

   If neither works, flag the question.

## Memory limits (required, added after the 10-27 out-of-memory crash)

The first run used up the laptop's memory: three agents had 8 JVMs going at once plus a 2.5 GB Python
process. The kernel then killed the Claude app. So:

- **Run every harness command inside a memory cap**, so only the harness dies if it grows too big:
  `systemd-run --user --scope -q -p MemoryMax=1500M -p MemorySwapMax=0 <command>`. Exit code 137
  means the cap was hit. Make the harness leaner; don't raise the cap.
- **One JVM at a time** per agent, started with `-Xmx384m`, compiling in batches of at most a few
  hundred classes. No process pools or parallel JVMs.
- **Generate permutations lazily** (`itertools.permutations` in a loop, written out in chunks). Never
  build the whole list in memory, and don't keep every compiled result: keep only the passing orders.
- Clean up compiled class files between batches.

## Rules

- **Only edit** the Micro-Parsons sections of `exercises/ch*/*.md`: the new `**Also accepted:**`
  line, the Problem text, and the Why-this-order text. Don't touch fragments, the Answer, the code
  block, MC questions, `## Coding` sections or anything else.
- **Don't commit, push or deploy.** The lead reviews the diff and commits.
- Don't install anything (no pip or npm packages). The standard library and the JDK only.
- Don't edit the academy repo (`~/dev/shockwave-programming-academy`); the lead changes the app's
  checker separately.
- If several agents work in parallel, each one edits only its assigned chapters. Nobody runs
  `git add -A` or `git commit -a`.

## Report

Write `docs/parsons-orders/report.md` (or `report-<chapters>.md` if several agents work in parallel).

- One row per question: file, question number, how many orders were added, whether the Problem text
  was changed (quote the old and new wording), and whether the Why text was changed.
- The harness command and its final output: questions checked, orders verified, mismatches (must be 0).
- **Flagged for Joe:** each flagged question, the reason, and the exact wording or decision needed.
- Any correct orders that look surprising (method order, block order), so Joe can see them.

## After the agents (lead's job, not the subagent's)

- Teach the academy checker to accept `**Also accepted:**`: `app/utils/parseExercise.ts` and
  `app/components/InteractiveParsons.vue`. A correct answer is the Answer, an Interchangeable variant,
  or any listed order. For a wrong answer, highlight it against the closest accepted order.
- Fix fragments running past their box in `InteractiveParsons.vue` (`.parsons-frag code { white-space: pre }`).
- Update `docs/exercise-authoring-conventions.md`:
  - Interchangeable section (lines ~114-125): replace it with the **Also accepted** rule.
  - Line ~425 ("pin the order in the Problem text"): retire that rule.
- Review the diff and re-run the harness, then commit, sync the academy submodule
  (`docs/academy-submodule-sync.md`), generate and deploy.
