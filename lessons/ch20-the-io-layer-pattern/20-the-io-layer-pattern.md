---
outlineRef: "20 — The IO-Layer Pattern (ADVKIT 40.1-11, JDP 50.1)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# The IO-Layer Pattern

Everything Ch.17-19 built — inheritance, polymorphism, and especially interfaces as contracts — comes together here in a real, widely-used FRC architecture pattern: keeping hardware access completely separate from the logic that uses it.

## The Problem: Hardware Everywhere Makes Testing (and Logging) Hard

A subsystem that talks directly to real motor controllers and sensors is genuinely hard to reason about: it can't run at all without the physical robot present, and there's no clean seam where you could intercept its data. A stronger idea than typical FRC logging solves this: instead of just logging a handful of chosen values, log *every* input flowing into the robot code, every loop cycle. Since every input is captured, a match can later be **replayed** off the robot with the exact same inputs, running the exact same logic — turning logging from "a tool for checking specific values" into a genuine safety net for verifying how any part of the code actually behaved. A logging framework (Ch.33) can record and replay data structured this way.

That capability only works if hardware access is structured so all input data flows through one well-defined seam. This is what the **IO layer** is for.

## Three Layers of a Subsystem

Traditionally, an FRC subsystem mixes three concerns in one class: its **public interface** (methods the rest of the robot calls), its **control logic** (deciding what to do with sensor data), and its **hardware interface** (actually reading sensors, actually commanding motors). The IO-Layer Pattern pulls that third piece out into its own object. (Commands v3, Ch.25, calls this kind of class a `Mechanism` — this chapter keeps calling it a "subsystem," the term used across the pattern's whole history.)

```java
public interface IntakeIO
{
    void updateInputs(IntakeInputs inputs);
    void setVoltage(double volts);
}
```

`IntakeIO` is exactly the kind of contract from Lesson 19 — it says *what* an intake can do (report its inputs, accept a voltage command), without saying *how*. Both methods are abstract, since neither one has a sensible default: two real implementations honor this same contract, and each one genuinely needs its own body (each class below is in its own file):

```java
public class IntakeIOReal implements IntakeIO
{
    // uses real hardware APIs to move physical rollers
}

public class IntakeIOSim implements IntakeIO
{
    // uses physics math (moment of inertia) to "fake" the robot in code
}
```

The subsystem class itself only ever talks to the `IntakeIO` interface — it never knows, and never needs to know, which concrete implementation is actually running underneath.

## Choosing the Implementation Once, at Construction

The whole point is decided in exactly one place — typically the `Robot` constructor, at startup — by simply constructing the subsystem with a different `IntakeIO` implementation depending on whether the code is running on the real robot or in simulation:

```java
public Robot()
{
    if (RobotBase.isReal())
    {
        intake = new Intake(new IntakeIOReal());
    }
    else
    {
        intake = new Intake(new IntakeIOSim());
    }
}
```

`RobotBase.isReal()` (from `org.wpilib.framework`) is the actual check that's true only when the code is running on real SystemCore hardware. `Intake` (the subsystem) accepts an `IntakeIO` in its constructor and stores it — every call from then on goes through that reference, polymorphically (Lesson 18.3) dispatching to whichever implementation was actually supplied.

## Inputs Flow Through a Shared Object

Outputs (commands like `setVoltage`) are simple, one-way method calls. Inputs are handled more carefully, since they need to be read consistently *and* stay replayable later: each IO interface has an accompanying inputs class holding **public** fields for every value that comes off the hardware — a plain data holder with no logic of its own, so it's an intentional exception to the private-field style taught since Ch.7 (Lesson 7.1):

```java
// pull fresh data from the IO layer into `inputs`, once per cycle
io.updateInputs(inputs);
```

The rest of the subsystem then reads from the `inputs` object — never straight from the IO layer — for a critical reason: every piece of code within one loop cycle sees the exact same cached values, so the logic feeds off exactly the same numbers a replay later would see, instead of whatever the hardware happens to report at the exact instant each line runs.

## The General Pattern Behind This: Ports and Adapters

This isn't an FRC-specific trick — it's a specific application of a broader, well-known software architecture idea called **Hexagonal Architecture** (or **Ports and Adapters**): keep core logic decoupled from whatever external system it happens to talk to (a database, a UI, real hardware), by defining a **port** (the interface — `IntakeIO`) that any number of **adapters** (`IntakeIOReal`, `IntakeIOSim`) can plug into. The core logic only ever depends on the port, never on any specific adapter — exactly mirroring `Intake` only ever depending on `IntakeIO`. The tradeoff is real: it's more abstraction and more files than talking to hardware directly, which is overkill for a one-off script — but it pays for itself the moment testability, simulation, or swappable hardware actually matter, which for a competition robot, they do.

## Common Pitfalls

- **Letting the subsystem read hardware directly, bypassing the IO layer.** That reintroduces exactly the coupling the pattern exists to remove — no sim support, no clean replay.
- **Adding getters to the IO interface and calling them from the subsystem's logic, instead of reading the cached inputs object.** `IntakeIO` itself has nothing to read — but as soon as an implementation grows one, reaching for it directly instead of `inputs` reintroduces values that can change mid-cycle in ways a replayed log never could — always read from `inputs`.
- **Treating the IO layer as optional overhead on a small subsystem.** It's genuinely more files and more ceremony — but the payoff (simulation, replay, decoupled testing) is exactly why competitive FRC codebases use it anyway.

## Key Takeaways

- The IO-Layer Pattern separates a subsystem's hardware access into its own interface (the "IO" layer), so the subsystem's own logic never touches real hardware APIs directly.
- One interface, multiple implementations (real hardware vs. simulated), chosen once at construction — everything else dispatches polymorphically through the shared interface.
- Inputs flow through a dedicated, shared object (`updateInputs`, called once per cycle), so every piece of logic in that cycle reads the exact same snapshot — the structure a logging framework (Ch.33) needs to record and replay a match later.
- This is FRC's specific application of the general Hexagonal Architecture (Ports and Adapters) pattern: core logic depends only on a port (interface), never on a specific adapter (implementation).

Derived from `other-reference-repo`: `java-design-patterns/hexagonal-architecture.md` (JDP 50.1)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 7 ("The IO-Layer Pattern") — IntakeIOReal/IntakeIOSim example
