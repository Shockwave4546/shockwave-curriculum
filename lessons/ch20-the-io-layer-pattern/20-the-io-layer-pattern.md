# The IO-Layer Pattern

**Outline ref:** 20 — The IO-Layer Pattern (ADVKIT 40.1-11, JDP 50.1)
**Status:** new — authored lesson (fuller depth than the teaser slide)

Everything Ch.17-19 built — inheritance, polymorphism, and especially interfaces as contracts — comes together here in a real, widely-used FRC architecture pattern: keeping hardware access completely separate from the logic that uses it.

## The Problem: Hardware Everywhere Makes Testing (and Logging) Hard

A subsystem that talks directly to real motor controllers and sensors is genuinely hard to reason about: it can't run at all without the physical robot present, and there's no clean seam where you could intercept its data. Team 6328's own AdvantageKit logging framework is built around a stronger idea than typical FRC logging — instead of just logging a handful of chosen values, it logs *every* input flowing into the robot code, every loop cycle. Since every input is captured, a match can later be **replayed** in a simulator with the exact same inputs, running the exact same logic — turning logging from "a tool for checking specific values" into a genuine safety net for verifying how any part of the code actually behaved.

That capability only works if hardware access is structured so all input data flows through one well-defined seam. This is what the **IO layer** is for.

## Three Layers of a Subsystem

Traditionally, an FRC subsystem mixes three concerns in one class: its **public interface** (methods the rest of the robot calls), its **control logic** (deciding what to do with sensor data), and its **hardware interface** (actually reading sensors, actually commanding motors). The IO-Layer Pattern pulls that third piece out into its own object:

```java
public interface IntakeIO
{
    default void updateInputs(IntakeInputs inputs) {}
    default void setVoltage(double volts) {}
}
```

`IntakeIO` is exactly the kind of contract from Lesson 19 — it says *what* an intake can do (report its inputs, accept a voltage command), without saying *how*. Two real implementations honor that same contract:

```java
public class IntakeIOSparkMax implements IntakeIO
{
    // uses real CAN IDs and hardware APIs to move physical rollers
}

public class IntakeIOSim implements IntakeIO
{
    // uses physics math (moment of inertia) to "fake" the robot in code
}
```

The subsystem class itself only ever talks to the `IntakeIO` interface — it never knows, and never needs to know, which concrete implementation is actually running underneath.

## Choosing the Implementation Once, at Construction

The whole point is decided in exactly one place — typically `RobotContainer`, at startup — by simply constructing the subsystem with a different `IntakeIO` implementation depending on whether the code is running on the real robot or in simulation:

```java
public RobotContainer()
{
    if (isReal())
    {
        intake = new Intake(new IntakeIOSparkMax());
    }
    else
    {
        intake = new Intake(new IntakeIOSim());
    }
}
```

`Intake` (the subsystem) accepts an `IntakeIO` in its constructor and stores it — every call from then on goes through that reference, polymorphically (Lesson 18.3) dispatching to whichever implementation was actually supplied.

## Inputs Flow Through a Loggable Object

Outputs (commands like `setVoltage`) are simple, one-way method calls. Inputs are handled more carefully, since they need to be logged *and* later replayable: each IO interface defines an accompanying inputs class holding public fields for every value that comes off the hardware, plus methods (`toLog`/`fromLog`) for saving and restoring that data from a log file:

```java
io.updateInputs(inputs);                         // pull fresh data from the IO layer into `inputs`
Logger.processInputs("Intake", inputs);          // send it to the logging framework (or restore it, during replay)
```

The rest of the subsystem then reads from the `inputs` object — never straight from the IO layer — for a critical reason: every piece of code within one loop cycle sees the exact same cached values, so a replay from the log looks byte-for-byte identical to what really happened on the field.

## The General Pattern Behind This: Ports and Adapters

This isn't an FRC-specific trick — it's a specific application of a broader, well-known software architecture idea called **Hexagonal Architecture** (or **Ports and Adapters**): keep core logic decoupled from whatever external system it happens to talk to (a database, a UI, real hardware), by defining a **port** (the interface — `IntakeIO`) that any number of **adapters** (`IntakeIOSparkMax`, `IntakeIOSim`) can plug into. The core logic only ever depends on the port, never on any specific adapter — exactly mirroring `Intake` only ever depending on `IntakeIO`. The tradeoff is real: it's more abstraction and more files than talking to hardware directly, which is overkill for a one-off script — but it pays for itself the moment testability, simulation, or swappable hardware actually matter, which for a competition robot, they do.

## Common Pitfalls

- **Letting the subsystem read hardware directly, bypassing the IO layer.** That reintroduces exactly the coupling the pattern exists to remove — no sim support, no clean replay.
- **Reading straight from the IO layer instead of the cached inputs object.** Values read directly from `io` could change mid-cycle in ways a replayed log never could — always read from `inputs`.
- **Treating the IO layer as optional overhead on a small subsystem.** It's genuinely more files and more ceremony — but the payoff (simulation, replay, decoupled testing) is exactly why competitive FRC codebases use it anyway.

## Key Takeaways

- The IO-Layer Pattern separates a subsystem's hardware access into its own interface (the "IO" layer), so the subsystem's own logic never touches real hardware APIs directly.
- One interface, multiple implementations (real hardware vs. simulated), chosen once at construction — everything else dispatches polymorphically through the shared interface.
- Inputs flow through a dedicated, loggable object (`updateInputs` + `toLog`/`fromLog`), so a match's exact inputs can be replayed later with identical results.
- This is FRC's specific application of the general Hexagonal Architecture (Ports and Adapters) pattern: core logic depends only on a port (interface), never on a specific adapter (implementation).

Derived from `other-reference-repo`: `advantagekit/getting-started/01-what-is-advantagekit.md` (ADVKIT 40.1), `advantagekit/data-flow/08-io-interfaces.md` (ADVKIT 40.8), `java-design-patterns/hexagonal-architecture.md` (JDP 50.1)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 7 ("The IO-Layer Pattern") — IntakeIOSparkMax/IntakeIOSim example
