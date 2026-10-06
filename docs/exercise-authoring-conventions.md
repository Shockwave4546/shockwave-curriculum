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
6. **If two or more fragments are genuinely order-independent relative to each other**
   (e.g. two unrelated variable declarations, neither reading the other), declare it
   explicitly with a `**Interchangeable:** (letter, letter, ...)` line right after
   `**Answer:**` — e.g. `**Interchangeable:** (a, i)`. Multiple independent groups can each
   get their own parenthesized set on the same line. This isn't optional cosmetic
   detail — the interactive academy app grades a student's own ordering against the
   Answer sequence exactly, position by position; an order-independent pair left
   undeclared gets marked wrong for a legitimately correct answer the moment a student
   picks the other valid order. Only declare a group when swapping those specific
   fragments truly doesn't change program behavior — don't declare one just because a
   fragment's exact position "feels" flexible; verify it the same mechanical way as the
   Answer sequence itself (reassemble with the swap applied and confirm it still compiles
   and behaves identically).

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
originally used a fictional `ColorSensor`/`calibrate()`/`getProximity()`, later replaced with
WPILib's `Ultrasonic` class — which turned out to be removed in WPILib 2027 (the "verified"
check had been done against a pre-2027 tree). It now uses WPILib 2027's real
`org.wpilib.hardware.rotation.Encoder` (`Encoder(int, int)`, `reset()`, `double getDistance()`),
verified in `wpilibj/src/main/java/org/wpilib/hardware/rotation/Encoder.java` on allwpilib `main`
at commit `5072e8cd5dec7f46da2eee5a219ff72cf2d01926` (2026-09-25). The rest of Ch.3's library
classes were checked at the same commit: `org.wpilib.hardware.discrete.DigitalInput`
(`DigitalInput(int)`, `boolean get()`), `org.wpilib.hardware.discrete.DigitalOutput`
(`DigitalOutput(int)`, `void set(boolean)`), and `org.wpilib.system.Timer` (`Timer()`, `start()`,
`double get()`). Apply this same check — against the current allwpilib `main`, recording the
commit — to any future Ch.3-adjacent content that introduces "a library class" as the example.
FRC only: never use FTC-only classes (`org.wpilib.hardware.expansionhub.*`).

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

## Coding exercises (advanced tier, Piston-checked)

Designed 2026-09-22. First exercise authored 2026-10-05 (10.3); not yet wired into the app —
see "What's still open" below. Applies to Ch.10+ `exercises/chNN-*/N.N-*.md` files as an optional
third `## Coding` section alongside the existing `## Multiple Choice` and
`## Micro-Parsons` sections — not a separate file or tree. Present only for lessons that
get this tier; MC/Micro-Parsons keep existing independently (per the Academy app's
already-locked plan, all three sub-types can coexist on one lesson's Exercises step).

### Grading mode: pick per-lesson, not by chapter number

Two shapes, chosen by what the **lesson's own unit of work** is — never by simple
"early vs. late chapter" chronology. Checked against how established practice platforms
actually do this (CodingBat's own [authoring guide](https://codingbat.com/authoring.html),
LeetCode, Exercism): full-program stdin/stdout grading is mostly an online-judge
(competitive-programming) pattern, not what skill-building platforms use — they default to
a fixed method signature with hidden test cases. That's the default here too, but only
where it fits the lesson:

- **Harness (method-signature, hidden test cases)** — default for Ch.10-13 (2D arrays,
  enums, exceptions, gotchas) and Ch.27-28 (algorithms): every one of these lessons' own
  unit of work is one method. Student is given a fixed signature and writes only the body;
  hidden test cases call it and check the return value. Isolates the one concept being
  tested without unrelated I/O ceremony — the same principle as this doc's own
  worked-example complexity rubric (don't stack more moving parts than the lesson itself
  demonstrates). Note Ch.27-28 land late but are still harness-shaped — the split is by
  lesson content, not position in the book.
- **Full-program/full-class (compile+run, or compile-only)** — default for Ch.14-26's
  design-pattern chapters (inheritance, polymorphism, interfaces, builder, encapsulation,
  Optional, command-based, etc.): these lessons' own unit of work is a class's structure,
  not one method's return value. Student submits a complete program/class, matching the
  "always show a full program" convention already used everywhere else in this course (MC/
  Micro-Parsons Answer keys).

A lesson can override its chapter's default if its own content clearly calls for the other
shape — an author judgment call per lesson, not a rigid table.

### Compile-only vs. compile+run

- **Compile-only** (original plan, never needed as its own mode): for exercises whose class
  genuinely needs real WPILib API surface (verified against actual library source — same rule
  as the "Real vs. invented API names" section above) where hardware/simulation isn't
  available under Piston. Ch.25 (Command-Based Programming) is the one such case. **Ch.25 was
  authored as `full-program` instead (2026-10-06): see "Ch.25: construct and inspect" below.**
- **Compile+run**: everything else — full execution, real pass/fail against test cases.
- Custom classes standing in for the student's own robot code (`DriveMotor`, `Shooter`,
  etc.) don't need real WPILib jars just because the scenario is robot-flavored — only
  genuine library API usage does, per the existing convention above.

### Java version

Pin every Coding exercise to **Java 25.0.1** (2027 season — the team's near-term target
per "Piston local dev environment" below, chosen over 17.0.16/2026 since that season has
already run). Not configurable per-exercise; a version bump is a curriculum-wide decision.

### Harness-mode authoring format

Add to the `## Coding` section:

- **Method signature** — exact, e.g. `public static int sumEvens(int[] values)`. Fixed;
  the student can't change it, since the harness calls it by this exact name/signature.
- **Starter scaffold** — the class + method stub shown to the student, e.g.:
  ```java
  public class Solution {
      public static int sumEvens(int[] values) {
          // TODO
      }
  }
  ```
- **Test cases** — `args`, `expected`, and a `visible` flag per case. Follow CodingBat's
  own rule (confirmed from their authoring guide): show 2-3 example cases in the Problem
  text so the student can reason about expected behavior, then add at least 2 **hidden**
  cases — same logic, different values. Hidden cases exist specifically to stop a student
  from special-casing against the visible inputs instead of solving the real problem;
  never introduce new logic only in a hidden case.

**Concrete layout (first used in `exercises/ch10-2d-arrays/10.3-…md`, 2026-10-05):**
`**Mode:** harness`, `**Problem:**` (with the visible examples), `**Signature:**`,
`**Starter:**` (```java block), `**Tests:**` as a markdown table
`| Visible | Arguments | Expected |` with `yes`/`no` in the first column, then `**Solution:**`
(```java model answer) and `**Why:**`, mirroring the MC/Micro-Parsons Answer/Why.

- **Arguments and Expected are written as Java source** (`new double[][] { {5.0, 1.0} }`,
  `2`, `"text"`), not JSON. The test runner pastes them straight into
  `check(n, Solution.method(<Arguments>), <Expected>)` and compares with
  `java.util.Objects.deepEquals`, so no per-type conversion code is needed. Write `double`
  values with a decimal point, and avoid expected values that depend on floating-point
  rounding (prefer exercises that return an index, count, or boolean).
- **Hidden tests aren't secret.** The app reads exercise files through Nuxt Content, which
  ships them to the browser. That's accepted: exercises are self-check practice, not tests,
  and grading runs in the browser (decided 2026-10-05).
- Verify every new Coding exercise against real Piston before committing: the model solution
  must pass every test, and at least one realistic wrong solution must fail a hidden test.

### Full-program-mode authoring format

Add to the `## Coding` section:

- **Problem statement**, same as harness mode.
- **Scenario(s)** — one or more named `{stdin, expected stdout}` pairs, same visible/
  hidden split and rationale as harness mode.
- Compare expected stdout after trimming trailing whitespace/newlines only — don't require
  exact byte-for-byte formatting beyond that; minor `println` formatting differences aren't
  the concept being tested.

**Concrete layout (pinned 2026-10-06):** `**Mode:** full-program`, `**Problem:**`,
`**Starter:**` (```java block), then one block per scenario —
`**Scenario 1 (visible):**`, `**Scenario 3 (hidden):**`, … — each with an optional
`**Input:**` ```text block (stdin) and a required `**Expected output:**` ```text block, then
`**Solution:**` (```java, the complete program) and `**Why:**`. 2-3 visible scenarios, at least
2 hidden. Each scenario is one separate Piston run with its own stdin.

- **Give the student a fixed `main` that reads the input.** Scenarios only differ if the
  program reads input, but `Scanner` on `System.in` isn't taught as a skill of its own. So the
  Starter contains the complete `main` (reading stdin with `Scanner`, calling the student's
  classes, printing results) marked `// Don't change main`, plus the class(es) the student
  writes as stubs. The student's work is the class structure the lesson teaches.
- The public class with `main` comes first in the file (runs on Java 17 and 25). The whole
  program is one file; Piston runs it with the single-file source launcher, so the file name
  doesn't need to match the class name.

### What's still open (deferred, not part of this design)

- **Runtime design (decided 2026-10-05, not built yet):** the app grades in the browser. It
  builds a `Main` test runner from the Tests table, sends `Main` + the student's
  `Solution.java` to Piston, and reads one `PASS n …`/`FAIL n …` line per test from stdout.
  Request path: browser → back end (checks the login session) → a small Python gateway
  (shared secret, 2-3 concurrent jobs, per-student rate limit) → Piston. The gateway forwards
  any code — it must not restrict submissions to exercise-shaped programs, because an open
  "playground" at the end of each section is planned.
- **Piston file-name quirk:** the Java package's `run` script renames the *first* file by
  appending `.java`, then runs it with the source launcher. Send the runner as `Main` (no
  extension) first and the student's class as `Solution.java`; Java 25's multi-file source
  launch finds `Solution.java` in the same directory. Sending `Main.java` produces
  `Main.java.java` and a compile error.
- First Coding exercise authored: 10.3 `getPeakSampleIndex` (verified on Piston: model
  solution 7/7; a row-sum bug and a tie-handling bug each fail hidden tests).
- **App support (built 2026-10-05, local only):** `shockwave-programming-academy` parses the
  `## Coding` section (`app/utils/parseExercise.ts`), builds and runs the test runner
  (`app/utils/codingRunner.ts`), and shows a code box with per-test results
  (`app/components/InteractiveCoding.vue`). Harness mode only so far. In `nuxt dev`,
  `/piston/execute` is proxied to the local Piston container; no deployed host serves that
  path yet.
- **Next (Joe, 2026-10-05):** author the remaining Coding exercises across the curriculum
  before choosing the final host, since exercises are content and don't depend on it.
  Scope: Ch.10-28 (Ch.25 done 2026-10-06); whether Ch.5-9 also get
  Coding exercises is still to be discussed. Authoring brief: `docs/coding-exercises/brief.md`.
- **Checker:** `tools/verify_coding_exercises.py` runs every file's model solution (or a
  `--solution-file`) against Piston, for harness and full-program modes. Its harness runner
  must stay identical in behaviour to the app's `codingRunner.ts`.
- **The app shows harness and full-program modes** (full-program screen built 2026-10-06).
  Full-program runs the student's whole program once per scenario, each with its own stdin,
  one run after another, and shows expected vs actual output for visible scenarios. Compile-only
  sections are skipped (hidden) by the app's parser until their UI is built; the rest of the
  file stays interactive.
- **Piston limits to raise before deployment:** Piston kills a run that writes more than its
  output limit (default **1024 bytes**) to stdout or stderr, reporting status `OL`/`EL` with
  signal SIGKILL. A long compiler error list hits this, and so would a program that prints a
  lot. The app already tells these apart from a timeout (status `TO`), but the deployed Piston
  should raise `PISTON_OUTPUT_MAX_SIZE` (e.g. 65536) so students see complete error messages.
- **WPILib 2027 jars are installed in Piston's Java 25 package** (2026-10-06, version
  `2027.0.0-alpha-7`, 8 jars, plus `quickbuf-runtime-1.4`, our headless test helper, and the JVM
  flags the scheduler needs) by `tools/piston/install-wpilib-jars.sh`; run it again on any new
  Piston host (the Azure VM). The jars are on the package's `CLASSPATH` for every Java run, so
  Java I/II exercises see them too (harmless). Piston must be restarted after installing. No
  vendor jars (REVLib etc.) are needed: Java I/II use no vendor classes. The jars are an alpha:
  re-check the exercises when the WPILib version is bumped.

### Ch.25: the real Commands v3 scheduler, headless

The six Ch.25 exercises (25.2-25.7; 25.1 is conceptual and has none) are `full-program`
exercises that build real Commands v3 objects and **run the real `Scheduler`** (on a fake clock),
printing what happened. 25.4 is plain Java (an enum state machine); the rest use WPILib:

| Exercise | What the fixed `main` does |
|---|---|
| 25.2 | prints a command's name and requirements, runs it until a limit flag trips, then runs a sequence on a simulated clock (checks the 2 s pause) |
| 25.3 | runs two priority warnings against a default `Glow` command and prints what runs on the mechanism |
| 25.5 | installs the state machine as the default command, feeds inputs, and fires a manual eject command that pauses it |
| 25.6 | binds commands to `Trigger`s built from flags and prints what ran each loop (`onTrue`, `onFalse`, `whileTrue`) |
| 25.7 | runs `driveThenShoot` second by second (timeout, then shoot) and checks the constants class by reflection |

How it works:

- **Setup in `main`:** `TestSupport.init();` (from `org.wpilib.command3`, our own helper, see
  below) replaces the two things that need WPILib's native hardware library, the Driver Station
  opmode lookup and the robot clock. `TestSupport.advance(seconds)` moves the fake clock, so timing
  is deterministic. Use `Scheduler.getDefault()` (mechanisms register their default commands there).
- **What can't be done:** `CommandXboxController` and other real controllers (they need the native
  library), so triggers are built from plain flags (`new Trigger(scheduler, () -> flag)`) and the
  student's method takes `Trigger`s.
- **Quirks of this alpha, found while authoring:** a trigger whose condition is `false` at its
  first poll fires `onFalse` once, so `main` runs one idle loop first. A command that needs the
  same mechanism as a running one replaces it when its priority is equal or higher, so give
  one-shot commands that must not interfere their own mechanism. When a command ends, a default
  command is re-queued on the **next** loop, so there is one loop with nothing running.
  `withTimeout` cancels the wrapped command in the same loop it starts the next step.
- **Naming:** `withAutomaticName()` makes a composition's name expose its structure (`A -> B`
  sequence, `(A & B)` parallel, `[2.0 Second timeout]`).
- **Piston setup:** see the "WPILib 2027 jars" note above and `tools/piston/install-wpilib-jars.sh`.
  Besides the 8 WPILib jars it installs `quickbuf-runtime-1.4` (approved 2026-10-06), our
  `command3-test-support.jar` (source in `tools/piston/command3-test-support/`), and adds two
  `--add-opens` flags to the Java package's `run` script. Restart Piston afterwards.
- Classes the student writes live in the same single file (`Main` first). Mechanism stand-ins
  such as `DriveMotor(int channel)` are given and marked `// Don't change`.

## 2026-09 content audit — conventions now in force (Ch.1-28)

Ch.10-28 worked examples and exercises were authored, then every chapter was audited and fixed
(tracker: `docs/content-audit/tracker.md`; brief: `docs/content-audit/fix-brief.md`). These rules
apply to all new or edited content:

- **Java 25** is the target; add a brief "On Java 17, …" note wherever 17 behaves differently.
  Multi-class single-file programs put the **public class with `main` first** (runs on 17 and 25).
- **WPILib 2027 / SystemCore** (`org.wpilib.*`, `setThrottle`, etc.) and **Commands v3**; verify
  every real WPILib name against allwpilib `main`. **FRC only** — never FTC-only classes
  (`org.wpilib.hardware.expansionhub.*`).
- **No vendor classes** in Java I/II. Motors use the invented `DriveMotor(int channel)` with
  `setThrottle(double)` / `getThrottle()` (defined in Ch.4); WPILib's `MotorController` interface
  only for interface/polymorphism lessons. The invented robot base class is `RobotPart` (Ch.17.1).
- Constants are ALL_CAPS. Say "PWM channel", not "CAN ID".
- **Micro-Parsons:** fragments with identical text must be declared together in
  `**Interchangeable:**` (the app grades by letter position); fragments differing only by
  indentation are distinct. Where Java allows whole-block reordering, pin the order in the
  Problem text. Fixed-scaffold puzzles show the scaffold as a ```java block in the Problem text
  (the app takes the Answer program from the code block after `**Answer:**`). Use one Answer
  sequence only — the app cannot parse "Blank 1 / Blank 2".
- MC-only exercise files (no Micro-Parsons section) are supported; a lesson with
  `noWorkedExample: true` in its frontmatter hides the Example step (Ch.14, 27.2).
- Keep derived copies in sync in the same pass: narration script (`narrated-lessons/_build/`),
  `review/chNN.html` (checked by `tools/check_lesson_review_consistency.py`).

## Piston local dev environment (set up 2026-09-20, not yet wired into any exercise)

A working self-hosted Piston instance already exists on Joe's dev machine — nothing here
is designed or wired into exercises yet, but the execution backend the advanced tier will
need is running and verified:

- Rootful Podman (`sudo podman run --privileged`), not rootless — required for Piston's
  isolate-based sandboxing to get real host capabilities. Confirmed working with actual
  code execution, not just theory.
- Container name `piston_api`, data volume at `~/piston-data`, API on `localhost:2000`.
- Custom Java packages installed (Piston's stock repo only ships Java 15.0.2, far short of
  what WPILib needs): **17.0.16** (2026 season, Temurin) and **25.0.1** (2027 season,
  Temurin — the team's actual near-term target since 2026 already ran). Both verified with
  real `execute` calls (`"language":"java","version":"17.0.16"` or `"25.0.1"`).
- Package build source lives in `~/dev/piston-src` (a clone of upstream
  `engineer-man/piston`, local commit only, not pushed). Ready-to-deploy built package
  binaries + install instructions are in `~/dev/piston-packages/README.md` — reuse these
  directly on the eventual Azure VM instead of rebuilding.
- Scope: full compile+run (Piston's native behavior) for plain-Java exercises; Ch.25 builds
  and inspects real WPILib 2027 Commands v3 objects without running them (see "Ch.25: construct
  and inspect"). The WPILib jars are installed in the Java 25 package; no vendor jars
  (REVLib/AdvantageKit) are used.
- The `25.0.1` package actually reports `java.version` = `25.0.4.1` (its `build.sh` pulls
  Temurin's latest 25 release), so the label is a pinned name, not the exact patch.
- VM sizing is in Joe's Azure planning session. Entra ID gating there is superseded: sign-in
  is now accounts in MySQL (see the academy repo's `docs/dreamhost-deployment.md`).
