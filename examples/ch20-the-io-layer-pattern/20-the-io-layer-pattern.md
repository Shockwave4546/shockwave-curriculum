---
outlineRef: "20 — The IO-Layer Pattern (ADVKIT 40.1-11, JDP 50.1)"
pairsWith: "[`lessons/ch20-the-io-layer-pattern/20-the-io-layer-pattern.md`](../../lessons/ch20-the-io-layer-pattern/20-the-io-layer-pattern.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# The IO-Layer Pattern — Worked Example

## Problem

The robot's climber needs to raise itself until it reaches 0.6 m, then stop. The programming team wants to test that "climb until 0.6 m" logic on a laptop, with no robot attached, and then run exactly the same logic on the real robot later. Structure the climber with an IO layer so the climbing logic never touches hardware directly.

## Step 1: Plan It First

1. Write an inputs class holding every value that comes off the climber's hardware.
2. Write a `ClimberIO` interface: the contract for "report inputs" and "accept a voltage."
3. Write two implementations of that contract: one for the real robot, one simulated.
4. Write the `Climber` subsystem so it only ever talks to `ClimberIO` and only ever reads from its cached inputs.
5. Pick the implementation once, at construction, then run a few loop cycles.

## Step 2: The Inputs Class

Every value the climber's hardware reports goes into one object with public fields:

```java
class ClimberInputs
{
    public double positionMeters = 0.0;
    public double appliedVolts = 0.0;
}
```

This is the object the rest of the subsystem reads from. (In a real AdvantageKit project this class would also get the `toLog`/`fromLog` methods from the lesson, so the framework can save and replay it. This example leaves logging out and focuses on the structure.)

## Step 3: The IO Interface (the "Port")

```java
interface ClimberIO
{
    default void updateInputs(ClimberInputs inputs) {}
    default void setVoltage(double volts) {}
}
```

Just like the lesson's `IntakeIO`, this says *what* a climber can do and nothing about *how*. The empty `default` methods (Lesson 19) mean an implementation only has to override the methods it actually needs.

## Step 4: Two Implementations (the "Adapters")

The real-robot version is where the actual motor controller and encoder calls would go. This laptop has no climber attached, so its bodies just print what they would do:

```java
class ClimberIOReal implements ClimberIO
{
    @Override
    public void updateInputs(ClimberInputs inputs)
    {
        System.out.println("[real] would read the climber encoder here");
    }

    @Override
    public void setVoltage(double volts)
    {
        System.out.println("[real] would send " + volts + " V to the climber motor here");
    }
}
```

The simulated version fakes the physics with simple math. It remembers the last voltage it was given, and every time `updateInputs` runs it moves the climber a little and copies the results into the inputs object:

```java
class ClimberIOSim implements ClimberIO
{
    private double simPosition = 0.0;
    private double simVolts = 0.0;

    @Override
    public void updateInputs(ClimberInputs inputs)
    {
        simPosition = simPosition + simVolts / 32.0; // fake physics: 8 V moves the climber 0.25 m per cycle
        inputs.positionMeters = simPosition;
        inputs.appliedVolts = simVolts;
    }

    @Override
    public void setVoltage(double volts)
    {
        simVolts = volts;
    }
}
```

Both classes `implements ClimberIO`, so anywhere a `ClimberIO` is expected, either one fits.

## Step 5: The Subsystem Only Knows the Interface

```java
class Climber
{
    private ClimberIO io;
    private ClimberInputs inputs = new ClimberInputs();

    public Climber(ClimberIO io)
    {
        this.io = io;
    }

    public void periodic()
    {
        io.updateInputs(inputs); // refresh the cached inputs once, at the start of the cycle

        System.out.println("Position: " + inputs.positionMeters + " m, volts: " + inputs.appliedVolts);

        if (inputs.positionMeters < 0.6)
        {
            io.setVoltage(8.0); // still below the target height: keep climbing
        }
        else
        {
            io.setVoltage(0.0); // reached the target height: stop
        }
    }
}
```

Two things to notice:

- The field `io` has type `ClimberIO`, the interface. Nothing in `Climber` mentions `ClimberIOReal` or `ClimberIOSim`. Each `io.setVoltage(...)` call dispatches polymorphically (Lesson 18.3) to whichever implementation was passed into the constructor.
- `periodic()` calls `io.updateInputs(inputs)` exactly once, first, and then every decision reads from `inputs`, never from `io` directly. That's the lesson's "read from the cached inputs" rule: every line in this cycle sees the same values.

## Step 6: Choose the Implementation Once, at Construction

```java
public class ClimberDemo
{
    public static void main(String[] args)
    {
        boolean runningOnRobot = false; // stand-in for the real "am I on the robot?" check

        Climber climber;
        if (runningOnRobot)
        {
            climber = new Climber(new ClimberIOReal());
        }
        else
        {
            climber = new Climber(new ClimberIOSim());
        }

        for (int cycle = 1; cycle <= 5; cycle++)
        {
            climber.periodic();
        }
    }
}
```

This `if`/`else` plays the same role as the lesson's `RobotContainer`: it's the one and only place that decides real vs. simulated. `runningOnRobot` is hardcoded to `false` here as a stand-in for a real robot check. The `for` loop stands in for the robot calling `periodic()` once per loop cycle.

## Step 7: The Whole Program

All five pieces go in one file. Only `ClimberDemo` is `public`, since it holds `main`:

```java
class ClimberInputs
{
    public double positionMeters = 0.0;
    public double appliedVolts = 0.0;
}

interface ClimberIO
{
    default void updateInputs(ClimberInputs inputs) {}
    default void setVoltage(double volts) {}
}

class ClimberIOReal implements ClimberIO
{
    @Override
    public void updateInputs(ClimberInputs inputs)
    {
        System.out.println("[real] would read the climber encoder here");
    }

    @Override
    public void setVoltage(double volts)
    {
        System.out.println("[real] would send " + volts + " V to the climber motor here");
    }
}

class ClimberIOSim implements ClimberIO
{
    private double simPosition = 0.0;
    private double simVolts = 0.0;

    @Override
    public void updateInputs(ClimberInputs inputs)
    {
        simPosition = simPosition + simVolts / 32.0; // fake physics: 8 V moves the climber 0.25 m per cycle
        inputs.positionMeters = simPosition;
        inputs.appliedVolts = simVolts;
    }

    @Override
    public void setVoltage(double volts)
    {
        simVolts = volts;
    }
}

class Climber
{
    private ClimberIO io;
    private ClimberInputs inputs = new ClimberInputs();

    public Climber(ClimberIO io)
    {
        this.io = io;
    }

    public void periodic()
    {
        io.updateInputs(inputs); // refresh the cached inputs once, at the start of the cycle

        System.out.println("Position: " + inputs.positionMeters + " m, volts: " + inputs.appliedVolts);

        if (inputs.positionMeters < 0.6)
        {
            io.setVoltage(8.0); // still below the target height: keep climbing
        }
        else
        {
            io.setVoltage(0.0); // reached the target height: stop
        }
    }
}

public class ClimberDemo
{
    public static void main(String[] args)
    {
        boolean runningOnRobot = false; // stand-in for the real "am I on the robot?" check

        Climber climber;
        if (runningOnRobot)
        {
            climber = new Climber(new ClimberIOReal());
        }
        else
        {
            climber = new Climber(new ClimberIOSim());
        }

        for (int cycle = 1; cycle <= 5; cycle++)
        {
            climber.periodic();
        }
    }
}
```

## What It Prints

```
Position: 0.0 m, volts: 0.0
Position: 0.25 m, volts: 8.0
Position: 0.5 m, volts: 8.0
Position: 0.75 m, volts: 8.0
Position: 0.75 m, volts: 0.0
```

Trace it cycle by cycle:

- **Cycle 1:** the sim starts at 0 V, so the position is `0.0`. That's below 0.6, so `Climber` commands 8 V.
- **Cycles 2-3:** each update moves the sim 0.25 m (8 / 32), so the position reads `0.25`, then `0.5`. Both are still below 0.6, so it keeps commanding 8 V.
- **Cycle 4:** the position reads `0.75`, which has passed 0.6, so `Climber` commands 0 V.
- **Cycle 5:** the sim got 0 V, so it doesn't move. It stays at `0.75` and reports `0.0` volts.

The printed volts always show the voltage from the *previous* cycle's command. That's because each cycle prints from the cached `inputs`, which were filled in at the start of the cycle, before this cycle's new `setVoltage` call. This is exactly the "one consistent snapshot per cycle" behavior the lesson describes.

## Switching to the Real Robot

Changing `runningOnRobot` to `true` is the only edit needed to run on the real robot. `main` then builds `new Climber(new ClimberIOReal())` instead, and not one line of `Climber` changes. (On this laptop, `ClimberIOReal`'s placeholder bodies would just print their `[real] would ...` lines instead of moving anything.)

## Recap

- The IO layer is an interface (`ClimberIO`) that says what the hardware can do. The real and simulated classes both implement it.
- The subsystem (`Climber`) stores a `ClimberIO` and never names a specific implementation. Every call dispatches polymorphically to whichever one it was built with.
- Real vs. simulated is decided in exactly one place, when the subsystem is constructed.
- Each cycle calls `updateInputs` once, first, and then reads only from the cached inputs object. Every decision in that cycle sees the same snapshot.
- This is Ports and Adapters in miniature. `ClimberIO` is the port, `ClimberIOReal` and `ClimberIOSim` are adapters, and `Climber`'s logic depends only on the port.
