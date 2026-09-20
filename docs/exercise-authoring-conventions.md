# Worked example & exercise authoring conventions

## The three-tier model

Every Ch.1-9 lesson (`lessons/chNN-*/N.N-*.md`) now has two companion files:

1. **`examples/chNN-*/N.N-*.md`** — a worked example: one fresh problem, fully solved,
   walked step by step. Not something the student attempts — it's the "I do" step between
   the lesson (concept) and the exercise (independent practice).
2. **`exercises/chNN-*/N.N-*.md`** — one Multiple Choice question and one Micro-Parsons
   (scrambled-code-reordering) problem. This is the beginner-tier exercise type, chosen
   over free-text "debug this program" exercises (which Ch.1-2 originally used and have
   since been rewritten) because it needs no code-execution backend. An advanced tier
   (text-submit, checked live against Piston) is planned for later chapters but not yet
   designed.

Both companion files must:
- Use a **fresh scenario**, different from the lesson's own example and from each other
  (exercise avoids the worked example's scenario, worked example avoids the lesson's).
- Use **only concepts already taught** by that lesson or an earlier one — no forward
  references (a checked, real risk — see "Known pre-existing lesson issues" below).
- Match the paired lesson's own **complexity budget** — see next section.

## Worked-example complexity rubric

A worked example's job is to model the lesson's concept clearly, not to showcase every
related idea at once. The rule that emerged after auditing all 40 Ch.1-9 examples:

> Compare how many variables/objects/concepts the **lesson's own examples** use together
> at once against how many the worked example uses together at once. They should be
> similarly proportioned — not simpler to the point of triviality, but never stacking more
> simultaneous moving parts than the lesson itself demonstrates.

This is a *relative* rubric, not an absolute difficulty floor — a Ch.9 worked example is
expected to be more complex than a Ch.2 one, because Ch.9's lessons are. The question is
never "is this hard for a beginner," it's "does this combine more at once than its own
lesson already does."

Concrete violations found and fixed during the first full audit (all in `examples/`):

- **`ch02/2.5`** (original version) — stacked 3 variables × 3 operators (`--`, `++`, `*=`)
  × 3 manually-unrolled repetitions, when the lesson's own example used one operator on
  one variable, checked once. Fixed to a single variable/operator. This was the case that
  established the rubric above — every other fix in this list follows the same shape.
- **`ch02/2.2`** — an unplanned "Step 5" aside re-ran an entire extra scenario (a second
  variable, re-demonstrating truncating division) that wasn't in the stated problem or
  plan. Cut.
- **`ch03/3.1`** — used two `Timer` objects, each unrolled through the same 4-statement
  block, plus a return-valued call the lesson's own example never showed. Trimmed to one
  object (the "objects are independent" point is still made in prose, just not doubled up
  in code).
- **`ch04/4.3`** — combined two unrelated sub-problems (a 9-variable 2D-distance
  calculation, plus a separate random-position task) into one file. Rewritten as a single
  Pythagorean-diagonal problem (6 variables) plus the random-range demo.
- **`ch06/6.1`** — duplicated an entire multi-step string-parsing routine a second time
  (14 variables total) purely to manufacture something to compare with `.equals()`/`==`.
  Rewritten to compare against a literal instead of re-parsing a second value (~7
  variables).
- **`ch05/5.9`** — a closing "put it all together" step stacked 3 independent accumulator
  patterns (sum, max, count) into one shared loop, which the lesson never does (it teaches
  each pattern in its own isolated loop). Removed.
- **`ch08/8.1-8.2`** — fused two demonstrations the lesson keeps separate (constructor
  overloading, and passing `this` as an argument) into one class plus an entire second
  class (`DashboardLogger`) that was never fully shown. Rewritten to demonstrate
  `this`-as-argument with one static method *inside the same class* instead of a second
  class — the fix generalizes: demonstrating "pass `this` to a method" never actually
  requires a second class.

Reviewed and deliberately left alone (a complexity call that looked like a violation but
wasn't, on inspection):

- **`ch09/9.7`** — builds its whole problem around two parallel `ArrayList`s staying in
  sync during a rotation, which the lesson only mentions conceptually. Kept as-is: `9.1`
  already establishes parallel arrays/lists as a real pattern, and index-based list
  mutation is already used earlier in `9.7` itself, so this synthesizes two
  already-modeled techniques rather than introducing an unfamiliar combination from
  nothing (unlike the `6.1` case above, which invented a whole duplicated algorithm with
  no prior model for it at all).

## Micro-Parsons fragment-count rule

**This is the rule to follow when authoring new Micro-Parsons puzzles** (the version
below is final — earlier drafts during this project's first authoring pass were revised
more than once; don't reuse an intermediate version from git history):

1. **Default: one fragment per physical line**, scrambling a full, complete, runnable
   program (class + `main` + every statement) — matching
   `exercises/ch01-why-java-for-frc/1.2-intro-to-algorithms-programming-and-compilers.md`,
   the canonical template. The template itself does **not** merge its own trailing
   closing-brace pair, and that's the default expectation everywhere.
2. **Only merge forced-adjacent lines when the count would otherwise exceed ~10-12
   fragments** — e.g. two closing braces back to back with nothing valid between them, or
   a genuinely atomic single-statement body. Never merge just because a pair happens to be
   *mergeable*; merging exists to solve an actual overflow problem, not as a style habit.
   Never merge fragments that are the lesson's actual subject matter (e.g. don't merge
   away a constructor's signature/brace/statement just because they're adjacent) — only
   merge pedagogically-inert boilerplate.
3. **If the puzzle still runs well past ~10-12 fragments after that merging** (typically
   loop-heavy or multi-method lessons), hold the outer scaffold (class declaration,
   `main` signature, their braces) fixed and stated explicitly in the Problem text (e.g.
   "Given this class and main method, reorder the fragments below into the method body
   that..."), and only scramble the meaningful inner block. A lesson with two genuinely
   independent reorderable blocks (e.g. a getter and a setter) can use two separately
   labeled fragment sequences rather than forcing them into one.
4. **Regardless of which case applies, the assembled Answer code block must always show
   the complete, runnable program** (scaffold included) — never just the inner fragment
   in isolation.
5. **Always verify the answer key mechanically**, not just by eye: every lettered
   fragment must be used exactly once in the Answer sequence, and reassembling in that
   exact order must reproduce the fenced Java block exactly. Several chapters' answer keys
   were verified by actually compiling and running the reconstructed program (JDK, no
   external dependencies) rather than just diffing text — worth doing whenever a JDK is
   available, since it catches errors text-diffing alone would miss.

Corrections made while converging on this rule (kept here so the *reasoning* survives,
not just the current state):

- **`ch08/8.1-8.2`** — an earlier pass merged the wrong pair: it collapsed the
  constructor's own signature+brace and statement+brace (the actual concept being
  tested) into single fragments, while leaving the pedagogically inert `main`/`println`
  structure fully granular. Reverted the constructor merges, applied the one genuinely
  forced merge instead (trailing `main`-close + class-close). This is the concrete case
  behind rule 2's "never merge the lesson's actual subject matter" clause.
- **`ch07/7.2`** — had been scoped down to only a getter, even though the lesson gives
  getters and setters equal billing. Restored the setter, which pushed the full program
  past budget even after merging — resolved with rule 3's two-labeled-sequence approach
  (class-body reorder + `main`-body reorder as two separate blanks).
- **`ch05/5.5`** — had been simplified to a 2-branch `if`/`else if` with no trailing
  `else`, which is exactly the lesson's own point (a missing trailing `else` makes "do
  nothing" a real, silent outcome). Restored the full 3-tier chain with trailing `else`.
- **`ch02/2.1-2.4`** — briefly merged trailing closing-brace pairs "for consistency" even
  though those files were already comfortably under the fragment ceiling; reverted per
  rule 2 (merging must solve an actual overflow, not just tidy up a technically-mergeable
  pair).
- **`ch09/9.4-9.8`** — an earlier pass presented the Answer as a bare method/loop
  fragment with no class/`main` wrapper, violating rule 4. Fixed by wrapping the Answer
  code block in a full program while keeping the Problem-text framing that the scaffold
  is pre-given.

## Real vs. invented API names

Custom classes representing *the student's own robot code* (e.g. `DriveMotor`, `Shooter`,
`Match`) are expected to be invented — that's normal everywhere in this course. The one
place this doesn't apply: when a class is standing in for **"a library class"** — Ch.3's
entire teaching point is that libraries and their APIs are real, looked-up things, not
invented ones. `exercises/ch03-apis-libraries-and-documentation/3.1-apis-and-libraries.md`
originally used a fictional `ColorSensor`/`calibrate()`/`getProximity()` — replaced with
WPILib's real `Ultrasonic` class (`ping()`, `getRangeInches()`), verified against actual
WPILib source, not just a plausible-sounding guess. Apply this same check to any future
Ch.3-adjacent content that introduces "a library class" as the example.

## Known pre-existing lesson issues (found while authoring, now fixed)

- **`lessons/ch05-control-structures/5.5-nested-if-statements.md`** referenced (via its
  worked example) Java's definite-assignment rule — a local variable only assigned inside
  `if`/`else if` branches won't compile if read afterward without a trailing `else`. This
  rule wasn't taught anywhere in the curriculum. Added as a Common Pitfalls entry in 5.5,
  since that's the lesson whose own trailing-`else` point it actually explains.
- **`lessons/ch05-control-structures/5.9-implementing-selection-and-iteration-algorithms.md`**
  loops over `visionLatencies`/`sensors` (collection types) and calls `.size()`, none of
  which is taught until Ch.9 — with no acknowledgment, unlike `5.10`, which already
  explicitly tells the reader "2D arrays... get their own full chapter — Ch.10." Added an
  equivalent one-line acknowledgment to `5.9` for consistency.
- **`Scanner` isn't taught until `lessons/ch09-storing-data/9.8-using-text-files.md`**, and
  even there only for reading files, never demonstrated for console/`System.in` input
  anywhere in the course. Confirmed by a repo-wide search — not a defect, just a fact
  worth knowing before reaching for it in any Ch.1-8 content: frame "input" as a
  hardcoded value standing in for a sensor/joystick reading instead (as
  `examples/ch02-variables-and-types/2.3-assignment-and-input.md` already does).

## Open items

- The advanced-tier exercise type (text-submit, checked live against Piston) hasn't been
  designed yet — only the beginner-tier MC/Micro-Parsons format above exists so far.
- This convention doc covers Ch.1-9 (the beginner tier). Extend it here, don't start a new
  doc, if/when Ch.10+ worked examples or exercises are authored.
