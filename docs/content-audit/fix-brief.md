# Content audit — Phase 2 brief (FIX)

Repo: /home/cjoe/dev/shockwave-curriculum. Phase 1 logged 533 issues in
`docs/content-audit/tracker.md`. Your job: fix every issue assigned to you, in the repo, and verify
the fixes. Read first: this brief, the tracker's "Content targets" and "Decisions needed" sections
and **your group's section** (each row has the issue, proposed fix and Phase-1 evidence), and
`docs/exercise-authoring-conventions.md`. Ch.25 only: also `docs/content-audit/ch25-v3-outline.md`.

## Your assignment = (a) every row in your group's tracker section + (b) every G13 row whose File
is in your chapters + (c) the extra items listed in your prompt. G13 = curriculum-wide coverage
gaps; the "Coverage placement" list below says which gaps land in which lesson.

## Decisions (binding — the tracker's Decisions table has the full text)
- **Java 25** is the target; add a brief "On Java 17, …" note wherever 17 differs. Multi-class
  single-file programs: put the **public main class FIRST** (works on 17 and 25 — verified).
- **WPILib 2027 / SystemCore**, `org.wpilib.*` packages, `setThrottle` (not `set`), etc. Verify
  every real WPILib name against allwpilib `main` source (read-only fetch). **FRC only: never use
  FTC-only classes** (`org.wpilib.hardware.expansionhub.*` — ExpansionHubMotor/Servo). Any Phase-1
  proposed fix naming them is invalid — pick another.
- **No vendor classes** (CTRE/REV/AdvantageKit). Motors: the invented class
  **`DriveMotor(int channel)` with `setThrottle(double)` / `getThrottle()`** (defined in Ch.4 —
  match it; say "assume it exists" or define it where a program must run). WPILib's generic
  `MotorController` interface (`org.wpilib.hardware.motor`, `setThrottle`) only where a lesson is
  about interfaces/polymorphism. Ch.3 uses real non-motor WPILib classes (`Encoder`,
  `DigitalInput`, `DigitalOutput`, `Timer`). Say "PWM channel"/"port", not "CAN ID".
- **Commands v3** (Ch.25 rewrite; elsewhere drop v2 names like `SubsystemBase`,
  `CommandScheduler`, `Commands.*`, `schedule()`).
- **Invented base class in Ch.17–18 is `RobotPart`** (was `Subsystem`), one canonical definition in
  17.1. Invented `Mechanism` classes are renamed (e.g. `Actuator`) so they can't be confused with
  WPILib v3's `Mechanism` interface. Rename other invented-`Subsystem` uses similarly.
- Rename `IntakeIOSparkMax` → `IntakeIOReal` (Ch.20, 21, 26 and anywhere else).
- Constants: **ALL_CAPS** (`MAX_SPEED`), not `kName`.
- Lesson 9.3 is **required** (drop "Optional" from title/text; keep the file name).
- 9.8: don't claim students used keyboard `Scanner`; no console-input lesson is added.
- Micro-Parsons: identical-text fragments must be declared `**Interchangeable:**` together;
  fragments differing only by indentation are distinct (the app shows indentation) — no action.
  Where Java allows whole-block reordering, pin the order in the Problem text. Other
  order-independent fragments must be declared Interchangeable (verify by swapping + running).
  Fixed-scaffold puzzles: show the scaffold as a ```java block in the Problem text (the app reads
  the Answer program from the code block AFTER **Answer:**). The app cannot parse a two-sequence
  ("Blank 1 / Blank 2") Answer — convert to one sequence.
- Java 25 compact `void main()` — one short note in 1.2 and 4.2 only.
- 27.2's "Mechanical Advantage lesson deck" sentence: leave unchanged (owner to confirm).
- Ch.27–28: keep placement; fix only "closing chapter"/"between Java I and II" wording.
- Chapter order is unchanged. Where Ch.15–16 use later concepts, add short preview notes.
- `review/chNN.html` exercise tabs are already removed — do not re-add exercises there.

## Already done by other groups (point to these; don't duplicate)
- Ch.3–5 fixed (committed). New lesson **5.12 "switch Statements and Expressions"**
  (`lessons/ch05-control-structures/5.12-switch-statements-and-expressions.md`); ternary in 5.5;
  do-while and break/continue in 5.8; `Double.MIN_VALUE` fix in 5.9.
- Ch.4 defines `DriveMotor`. Ch.3 uses Encoder/DigitalInput/DigitalOutput/Timer.
- Ch.17–18 fixed (uncommitted): `RobotPart` in 17.1; new lesson **17.5 "Abstract Classes and
  Methods"**; `protected` + custom exceptions in 17.2; hashCode + `instanceof` in 17.4;
  "Casting Back Down" in 18.3; `final` methods in 18.1.

## Coverage placement (where G13 gaps land) — new content goes ONLY where listed
- 2.2: joining text with `+` (and `"a"+1+2` vs `1+2+"a"`), escape sequences. 2.4: widening vs
  narrowing, `0.1+0.2`, **tolerance comparison** (5.4 points here), `Math.round` pointer, negative
  rounding caveat. 2.5: compound-assignment hidden cast; prefix vs postfix (one line). 2.1:
  several declarations in one statement (one line); optional `var` aside.
- 6.1: `charAt`/`char` vs String, everyday methods table (equalsIgnoreCase, compareTo, contains,
  startsWith/endsWith, isEmpty/isBlank, trim/strip, replace, split), `null` + `"lit".equals(x)`,
  `String.format`/`printf`. 6.2: `StringBuilder`/`replace` "in real code" note.
- 7.2: **"Where Variables Live"** (scope + lifetime: local / parameter / instance; shadowing
  pointer to Ch.8). 7.3: one-public-class-per-file + launcher note (main class first). 7.4:
  class-name static access; Constants-class pattern.
- 8: `this(...)` chaining (+ Java 25 JEP 513 note); `void` constructor pitfall; shadowing points
  back to 7.2.
- 9.2: Wrapper Classes subsection (table, autoboxing, unboxing `null` NPE, `Integer ==` cache,
  `parseInt`/`parseDouble`, `remove(int)` vs `remove(Object)`), diamond `<>`, remove/contains/
  indexOf/isEmpty. 9.3: containsKey/getOrDefault/remove/size; fix the get()-null claim.
  9.1: `Arrays.toString` one line.
- 11: built-in enum methods (name/ordinal/valueOf/toString), `==` on enums, pointer to 5.12 for
  switch, `null` enum variable. 10.3 may keep the ternary with a pointer to 5.5.
- 12: try-with-resources, multi-catch, catch order, `getMessage()` + reading a stack trace,
  `Error` in the unchecked definition; custom exceptions point to 17.2.
- 13: `double ==`, `Integer ==` cache, ignored String return value, enum `==`, switch fall-through.
- 15: "List is the interface behind ArrayList"; `List.of`/`Set.of`/`Map.of`; preview note that
  Set/Queue/Map are interfaces (Ch.19); equals+hashCode pitfall (points to 17.4); sorted
  collections need comparable elements (points to Ch.19); Deque stack methods / prefer ArrayDeque.
- 16: preview note on `Object`/`Number` as parent types (Ch.17); "what generics can't do".
- 19: static interface method example; interface-vs-abstract-class comparison (17.5 points here);
  implicit `public`; Comparable/Comparator (short). 19.1: anonymous classes (short, before the
  lambda comparison); functional interfaces table (Supplier/Consumer/Function/Predicate,
  java.util.function, @FunctionalInterface); 4 method-reference kinds; effectively-final pitfall.
- 22: static nested classes section (Outer.Nested, mutual private access, inner vs static).
- 23.1: refocus on **access modifiers (4-level table incl. protected, package-private) + `final`
  (vars/fields/params, final methods & classes, blank-final rule, effectively final)** +
  encapsulation leak / defensive copy + **records** + immutability checklist. Point back to 7.2
  "Where Variables Live" for scope. Keep the file name/URL.
- 24: method-ref kinds pointer (19.1); `orElseThrow()`/`ifPresentOrElse`/`orElseGet`.
- 28.2: "in real code" `Arrays.sort`/`Collections.sort`/`Comparator`.

## Keep every derived copy in sync with the lesson (same pass)
For every lesson change: the worked example / exercise if affected, the narration script
(`narrated-lessons/_build/chNN/lesson_*.py` — screen code must stay verbatim with the lesson per
`tools/check_script_code.py`; speak text accurate; Kokoro pitfalls per docs/kokoro-tts-process.md;
code lines on screen ≤ ~90 chars — move long trailing comments onto their own line in BOTH the
lesson and the script), and `review/chNN.html` (body/pitfalls/takeaways/prov).
Do NOT synthesize audio or run build_kokoro_batch.py / kokoro_builder.py / builder.py — the lead
rebuilds narration afterwards. To run check_script_code.py, assemble a throwaway HTML in your
scratch dir from BEATS exactly as kokoro_builder does (no audio).

## Verify (every file you touch)
- `java File.java` (JDK 25; javac not installed) on every full program in lessons/examples/
  exercises you touched; output matches the text. Snippets framed as partial are fine.
- Micro-Parsons: every fragment once, reassembly matches, Interchangeable swaps run identically.
- MC: exactly one correct answer, Why covers each wrong option.
- `python3 tools/check_lesson_review_consistency.py <ch>` → 0 issues; plus a prose containment
  check (lesson paragraphs/bullets present in the review page).
- check_script_code.py on your assembled throwaway HTML → OK.

## Rules
- Edit only files in your chapters (lessons/examples/exercises/_build/chNN/review/chNN) plus
  anything explicitly listed in your prompt. No git commits (the lead commits). No installs, no
  jar downloads; network only for read-only WPILib/Java docs. Scratch work in your own session
  scratchpad directory.
- Some rows may already be fixed by another group's work — check the current file first.
- If a row is wrong, already fixed, or a fix would contradict a decision, don't force it: mark it
  `Won't fix` / `Already fixed` with a one-line reason. Genuine new ambiguity → don't guess; report.

## Final reply (the lead updates the tracker from it)
1. A status line per tracker ID you own: `G05-012: Fixed — <≤12 words>` / `Won't fix — <reason>` /
   `Blocked — <question>`.
2. Files changed/created. 3. Verification summary. 4. New issues found (if any).
