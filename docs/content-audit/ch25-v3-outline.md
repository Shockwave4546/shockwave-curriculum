# Ch.25 — Commands v3 rewrite outline

From the Phase-1 audit of Ch.25 (group G11), checked against allwpilib `main` @ `5072e8cd5dec`
(2026-09-25). Source paths: `commandsv3/src/main/java/org/wpilib/command3/` (package
`org.wpilib.command3`), `wpilibjExamples/src/main/java/org/wpilib/examples/hatchbotcmdv3/`,
`wpilibjExamples/src/main/java/org/wpilib/templates/commandv3/`, `design-docs/commands-v3.md`
(partly stale — **source wins**).

Keep the arc: why → commands → scheduler → state (enum) → transitions (switch) → triggers →
project structure. Java fundamentals are unchanged; only the framework layer changes.

## Owner decisions (2026-09-25)
- Per-loop state logic: the mechanism's **default command** —
  `runRepeatedly(() -> { switch (state) { … } }).withPriority(LOWEST_PRIORITY).named(..)`.
- 25.7 layout: the official **2027 v3 template** (`Robot extends OpModeRobot` + `@Autonomous` /
  `@Teleop` `OpMode` classes taking `Robot`, `mechanisms/`, `constants/`), plus a labelled
  "Reading Commands v2 code (2026 and earlier)" section (recognize, don't write).
- Arrow-form `switch`, pointing to lesson 5.12. `StateMachine` class: alpha sidebar only.
- `CommandXboxController` (a/b/x/y); note `CommandGamepad` exists. Constants ALL_CAPS.
- 25.4–25.5 teach the **State Machine design pattern** thoroughly (states, transitions, guards,
  entry actions, diagram, leaving the start state); later subsystem chapters build on it.

## Lesson plan
**25.1 What Is Command-Based (v3)** — imperative vs declarative with `mech.run(...).named(...)`;
three abstractions: Mechanism (an interface), Command, Scheduler (`Scheduler.getDefault()`);
v3's idea: commands are normal methods with loops + `coroutine.yield()`; v2 still exists as
`org.wpilib.command2`; requirements + "priority decides". Gone: CommandScheduler, SubsystemBase,
`Commands.*`.

**25.2 Commands & Compositions (v3)** — one coroutine body (mapping table from v2's four
lifecycle methods); forced naming via staged builders (missing `.named` is a compile error — tie
to Ch.22); factories: `run`, `runRepeatedly`, `idle`/`idleFor`, `Command.noRequirements`,
`Command.requiring(..).executing(..)`, `Command.waitFor(Time)`, `Command.waitUntil`; coroutine
helpers `yield`, `wait`, `waitUntil`, `park`; cleanup `whenExited`/`whenCanceled` (alpha);
compositions `Command.sequence`/`parallel`/`race`, `andThen`/`alongWith`/`raceWith`/`until`,
`withTimeout(Time)` (builders → `.named`/`.withAutomaticName()`); `co.await`/`awaitAll`/
`awaitAny`/`fork` own a mechanism only while in use. Pitfalls: missing `yield` hangs the robot;
`yield` must be called as `coroutine.yield()` (contextual keyword); don't use a captured coroutine.
Units intro (`Seconds.of`). v2 callout. Gone: lifecycle methods, `addRequirements`,
`FunctionalCommand`.

**25.3 The Scheduler (v3)** — `Scheduler.getDefault().run()`; simplified cycle: clean up scopes →
disabled safety → side jobs (`addPeriodic`, data only) → poll triggers → queue defaults → promote
queued (evicting conflicts) → run each command to its next yield. Scheduling is queued; last
conflicting command queued wins; children start immediately. **Default commands + priorities**
(`withPriority`, `DEFAULT_PRIORITY`, `LOWEST_/HIGHEST_PRIORITY`; equal or higher interrupts,
lower is rejected) replace `CANCEL_SELF`/`CANCEL_INCOMING`. Scopes (auto commands cancelled when
autonomous ends — alpha). v2 callout. Gone: subsystem `periodic()`, `initialize`-on-schedule,
`end(bool)` (→ `onCancel`/`onExit`).

**25.4 State Logic (enum)** — State pattern: states as an enum, one state at a time, a state
diagram; Java content unchanged; terminology "mechanism".

**25.5 Transitions (switch)** — arrow-form switch (5.12); guards, entry actions, how the machine
leaves its start state (request method / driver input); runs as the default command at lowest
priority; optional alpha sidebar on `StateMachine` (added 2026-05-08, changed 2026-09-13).

**25.6 Triggers (v3)** — core binding API unchanged (`onTrue`/`onFalse`/`whileTrue`/…);
`debounce(Time[, DebounceType])` — default debounces only the rising edge; controllers in
`org.wpilib.command3.button`; new: command-scoped bindings, `retryWhileTrue`,
`risingEdge`/`fallingEdge`, `multiPress`, `ifTrue` (alpha).

**25.7 Project Structure (v3)** — `OpModeRobot` template layout; thin Robot, grouped constants,
instance / static / `implements Command` rule (e.g. `requiring(..).executing(co -> await..)`);
note the template's package-private fields vs Ch.23; section "Reading Commands v2 code (2026 and
earlier)": annotated v2 snippet + v2→v3 table (SubsystemBase→Mechanism interface;
initialize/execute/isFinished/end→one coroutine body; CommandScheduler.getInstance()→
Scheduler.getDefault(); RobotContainer→OpModeRobot/OpModes; addRequirements→builder
requirements; InterruptionBehavior→priority; Commands.runOnce→mech.run(...).named(...);
withTimeout(double)→withTimeout(Time)). Gone: RobotContainer, the teleop-cancel pitfall (v3
auto-cancels auto commands via scopes).

## Other 2027 renames seen in Ch.25
`DoubleSolenoid.Value.kForward/kReverse/kOff` → `FORWARD/REVERSE/OFF`; `MotorController.set` →
`setThrottle`; v2 `kCancelSelf` → `CANCEL_SELF`; `Sendable`/`SendableChooser` removed (use
`org.wpilib.tunable.Selectable<V>`).

## Alpha-unstable — re-check before publishing
StateMachine (#8297, #9207, #9428); scopes (#9271, #9401, #9310); `onExit`/`whenExited` (#9402);
disabled-safety cancel (#9417); `ifTrue` (#9403); `multiPress` (#8901); Mechanism became an
interface (#8303); gamepad renames (#8896, #8921). **Suspend/resume is in the design doc but not
implemented — don't teach it.** Design doc vs source: `getInstance()` vs `getDefault()`,
`whenCancelled` vs `whenCanceled`. v3 needs Java 21+ (JDK-internal continuations) — keep examples
single-threaded.
