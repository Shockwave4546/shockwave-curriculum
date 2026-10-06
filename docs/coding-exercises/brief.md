# Coding exercises — authoring brief (Oct 2026)

Binding instructions for the agents adding `## Coding` sections to Ch.10-28 exercise files.
Written 2026-10-06 so it survives session restarts. The lead agent assigns each agent one
group from the table below.

## Goal

Add one `## Coding` section to the **end** of each exercise file in your group, after the
existing `## Multiple Choice` / `## Micro-Parsons` sections. Leave those sections untouched.

`exercises/ch10-2d-arrays/10.3-implementing-2d-array-algorithms.md` is the finished reference
example (harness mode). Copy its layout exactly.

## Read first, in this order

1. `docs/exercise-authoring-conventions.md`, the sections "Coding exercises (advanced tier,
   Piston-checked)" and "2026-09 content audit — conventions now in force". These are binding.
2. The 10.3 exercise file above.
3. For each file you work on: its paired lesson (`lessons/…`, same name) and the existing
   exercise file. The coding exercise tests **that lesson's** concept, using only what that
   lesson and earlier lessons teach.

## Groups

| Group | Chapters | Default mode | Files |
|---|---|---|---|
| A | 10-13, 27-28 | harness | 10.1, 10.2, 11, 12, 13, 27.1, 27.2, 28.1, 28.2, 28.3, 28.4 (10.3 is done) |
| B | 14-18 | full-program | 14, 15, 16, 17.1-17.5, 18.1-18.3 |
| C | 19-24, 26 | full-program | 19, 19.1, 20, 21, 22, 23.1, 24, 26 |
| later | 25 | compile-only | not now: needs WPILib 2027 jars in Piston |

The default mode can be overridden for a lesson whose unit of work is clearly the other shape
(conventions doc, "Grading mode"); say why in your report.

**Skipping a lesson is allowed** when a coding exercise genuinely doesn't fit (e.g. a purely
conceptual lesson like 14 or 27.2). Don't add a section; explain in your report.

## Groups for Ch.5-9 (added 2026-10-06, Java I)

Joe agreed to add Coding exercises to Ch.5-9. Same rules as above, plus the Java I notes below.

| Group | Chapters | Default mode | Files |
|---|---|---|---|
| D | 5 | harness | 5.1-5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 5.10, 5.11, 5.12 |
| E | 6, 9 (except 9.8) | harness | 6.1, 6.2, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7 |
| F | 7, 8, 9.8 | full-program | 7.1, 7.2, 7.3, 7.4, 8.1-8.2, 9.8 |

**Java I notes (students here have only just learned the language):**

- Use **only what that lesson and the lessons before it teach.** Check the lesson order: no
  classes before Ch.7, no `ArrayList` before 9.2, no `switch` before 5.12, no recursion, no lambdas.
  Harness methods in Ch.5-6 and 9 are plain `public static` methods on primitives, `String`s and
  arrays or `ArrayList`s.
- **Difficulty:** easier than 10.3. Solvable in 5-12 lines by a student who just finished the
  lesson. One concept per exercise (a loop, a boolean expression, a `switch`, a string method).
- **Hidden tests should target the lesson's own Common Pitfalls** (off-by-one, `==` on `String`s,
  integer division, empty input, the first/last element), not exotic inputs.
- **Lessons that are theory** (5.11 informal runtime analysis, 5.7 De Morgan as pure logic) can still
  have a small harness method (e.g. returning a count or a boolean); skip with a reason only if
  nothing testable fits.
- **9.8 (text files):** Piston has no input files, so a program must write a file before it reads
  it, or read from `Scanner(System.in)`. If a file exercise can't be done cleanly, skip it and say so.
- **F (classes):** Ch.7-8 are where students first **write their own classes**. `DriveMotor(int
  channel)` with `setThrottle(double)` / `getThrottle()` is the course's invented motor class
  (introduced as a given class in Ch.4); use it as a given class if you need a motor, and let
  students write small classes of their own like `Battery` or `Intake`. The student writes the
  class; the fixed `main` reads input and prints what the class does.

## Rules (on top of the conventions doc)

- **Harness mode:** the method must **return** its result (a `void` method can't be checked).
  If the lesson is about changing an array in place, return the array. Write each Expected
  value as a Java literal of the method's return type: `2` for `int`, `2.0` for `double`,
  `"text"` for `String`, `true`/`false`, `new int[] {1, 2}` for arrays. A type mismatch
  (`2` for a `double`) fails even when the value is right.
- **Avoid answers that depend on floating-point rounding.** Prefer returning an index, count,
  boolean, `int`, or `String`.
- **Visible tests appear in the Problem text** as examples, like 10.3. 2-3 visible, at least 2
  hidden. Hidden tests use the same logic with different values, including the edge cases
  the lesson's own pitfalls warn about.
- **Full-program mode:** the Starter gives a complete, fixed `main` (marked
  `// Don't change main`) that reads stdin with `Scanner`, calls the student's classes and
  prints results. The student writes only the class structure the lesson teaches. Keep `main`
  short and obvious.
- **No real WPILib or vendor classes.** Use the course's invented classes (`DriveMotor` with
  `setThrottle`/`getThrottle`, `RobotPart`, etc.) or define small classes in the exercise. If a
  lesson's exercise would genuinely need real WPILib, skip it and say so.
- **Style:** match the existing files — braces on their own line, 4-space indents, ALL_CAPS
  constants, FRC-flavoured scenarios (but don't force it where it'd be confusing).
- **Difficulty:** a real step up from MC/Micro-Parsons, but solvable in 10-20 lines by a
  student who just finished the lesson. 10.3 is the target level.
- **Frontmatter:** change `status` to end with `+ Coding)`, like 10.3.
- **Out of scope:** don't edit lessons, worked examples, narration, `review/` pages, other
  sections, or any file outside your group. Don't commit.

## Verify every exercise (required)

Piston must be running (`curl -s localhost:2000/api/v2/runtimes` lists java 25.0.1). If it
isn't, stop and report it — don't skip verification.

1. `python3 tools/verify_coding_exercises.py <file>` must print `OK` (the model solution
   passes every test, and the visible/hidden counts are right).
2. Write at least one **realistic wrong solution** — the mistake a student would actually
   make, ideally the one the lesson's Common Pitfalls warn about — in a temp directory
   (`mktemp -d`, never inside the repo), then run
   `python3 tools/verify_coding_exercises.py <file> --solution-file <wrong.java>`.
   It must **fail at least one hidden test**. If it only fails visible tests, add a hidden
   test that catches it.
3. Re-read the finished section once as a student would: is the Problem unambiguous (ties,
   empty input, what to return)?

## Report back (one block per file)

- File, mode (and why, if not the default) — or "skipped" and why
- Method signature or the classes the student writes
- Visible/hidden test counts and the checker result
- The wrong solution(s) tried, and which tests caught them
- Anything you were unsure about

## Outcome (2026-10-06)

Groups A, B and C ran as three Sonnet/medium agents; the lead re-ran the checker on every file
and reviewed the results.

- **28 exercise files now have a `## Coding` section** (including 10.3): 10 harness (Ch.10-13,
  28) and 18 full-program (Ch.15-24, 26). All pass `tools/verify_coding_exercises.py`, and no
  Starter passes on its own.
- **Skipped as conceptual, no code to write:** 14 (why design patterns), 27.1 (abstraction and
  program design), 27.2 (ethics and licensing, MC-only). Ch.25 is later (needs WPILib 2027 jars).
- **App support:** harness and full-program exercises are both interactive (full-program screen
  added 2026-10-06; every one of the 28 was run through the app's own parser and runner with its
  model solution and its untouched Starter).
- **Known weak spots** (a wrong solution can still pass these checks):
  - 17.1: nothing stops `Robot extends Intake` instead of "has an Intake".
  - 17.5: a non-abstract `RobotPart` with an empty `stop()` passes; abstractness isn't checked.
  - 28.2 and 28.3: "write it by hand / recursively" isn't enforced (a student could call
    `Arrays.sort` or use a loop).
  - 28.1 uses `int[][]` rather than the lesson's `double[][]` with a tolerance, so the
    tolerance pitfall isn't tested.
  - 26 (architecture takeaways): the DRY rule (one shared constant) isn't tested.
  - 11 and 12 ask for slightly more than 10.3 (a nested enum; two methods).

## Ch.25 (added 2026-10-06)

Authored by the lead agent, not the subagents (it needs real WPILib API knowledge). Six
`full-program` exercises, 25.2-25.7; **25.1 skipped** (conceptual). 25.2, 25.3, 25.5, 25.6 and 25.7
run the **real Commands v3 scheduler** headlessly; design and quirks are in "Ch.25: the real
Commands v3 scheduler, headless" in `docs/exercise-authoring-conventions.md`. Needs the Piston
install from `tools/piston/install-wpilib-jars.sh`. All six pass the checker and the app's own
runner, and every wrong solution tried fails a test (e.g. `noRequirements`, parallel instead of
sequence, a pause of the wrong length, a missing `yield()`, a missing `LOWEST_PRIORITY`, a
hardcoded or negated priority, a state machine that cascades transitions, `onTrue` for
`whileTrue`, `toggleOnTrue` for `onTrue`).

Known weak spots:
- Real controllers (`CommandXboxController`) can't be created without WPILib's native library, so
  25.6 uses triggers built from flags.
- 25.4 is plain-Java logic, so it only checks the machine's behaviour, not any Commands v3 API.
- The headless setup depends on an alpha (WPILib `2027.0.0-alpha-7`): re-run the checker on all of
  Ch.25 when the jars are bumped.

## Outcome: Ch.5-9 (2026-10-06)

Groups D, E and F ran as three Sonnet/medium agents; the lead agent re-ran the checker on all 60
coding exercises, checked every untouched Starter, and ran all 60 through the app's own parser and
runner.

- **26 files, none skipped:** D = all 11 Ch.5 files (harness); E = 6.1, 6.2 and 9.1-9.7 (harness);
  F = 7.1-7.4, 8.1-8.2 and 9.8 (full-program). **60 coding exercises in total now** (Ch.5-13, 15-26, 28).
  Not covered: Ch.1-4 (MC and Micro-Parsons only), 14, 27.1, 27.2 (conceptual), 25.1.
- **Fixed by the lead:** 9.8's Starter returned `"none"`, which already passed the no-match scenarios;
  it now returns `null`.

Known weak spots:
- 5.7 (no `!`), 5.11 (no loops), 7.1 (`private` fields) and 8.1-8.2 (`this(...)` delegation) can't be
  enforced by output alone: a student who ignores that instruction can still pass.
- 5.6 uses `% 0` and `ArithmeticException` as its short-circuit hazard; 5.9 uses a computed sequence
  (`t*t - 6*t`) rather than a collection; 5.3, 5.4 and 5.6 are very small.
- 9.3 (optional HashMap) is a small exercise. 9.8's fixed `main` uses `PrintWriter`, which the
  lesson doesn't teach (a comment explains it).
- In E's test tables, lists are written as `new java.util.ArrayList<>(java.util.List.of(...))` so the
  runner can paste them in; the app rewrites them as `[5, 7]` for display, so students never see that.
