---
outlineRef: "20 — The IO-Layer Pattern (ADVKIT 40.1-11, JDP 50.1)"
pairsWith: "[`lessons/ch20-the-io-layer-pattern/20-the-io-layer-pattern.md`](../../lessons/ch20-the-io-layer-pattern/20-the-io-layer-pattern.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
---

# The IO-Layer Pattern — Exercises

## Multiple Choice

**Question:** A `Shooter` subsystem is built with the IO-Layer Pattern. It stores a `ShooterIO` field, and every one of its methods talks only to that field. Right now the robot code builds it like this:

```java
shooter = new Shooter(new ShooterIOReal());
```

A `ShooterIOSim` class that `implements ShooterIO` already exists. What has to change so the exact same `Shooter` logic runs in simulation?

**Options:**

- A. Only the construction line, so it becomes `new Shooter(new ShooterIOSim())`
- B. Every method inside `Shooter` needs its own `if` check for "real or simulated?" around each hardware call
- C. `Shooter` has to be rewritten to `extends ShooterIOSim` instead of storing a `ShooterIO` field
- D. The `ShooterIO` interface has to be edited so its methods match `ShooterIOSim` instead of `ShooterIOReal`

**Answer:** A

**Why:** `Shooter` only depends on the `ShooterIO` interface, so any object that implements `ShooterIO` can be passed into its constructor. Every call then dispatches polymorphically to whichever implementation was supplied. The choice between real and simulated lives in exactly one place, the line that constructs the subsystem.

- B is wrong. Scattering real-vs-sim checks through the subsystem is exactly the coupling the IO layer exists to remove. `Shooter` never needs to know which implementation it has.
- C is wrong. `Shooter` would then be permanently tied to the simulated class, and it could never run on the real robot. The pattern works because `Shooter` *holds* an interface-typed reference, not because it inherits from a specific implementation.
- D is wrong. The interface is the shared contract that both `ShooterIOReal` and `ShooterIOSim` already honor. Nothing about it is specific to either one, so it doesn't change when you switch implementations.

## Micro-Parsons

**Problem:** You're given everything in the program below except the body of `main`: the `FeederInputs` class, the `FeederIO` interface, its `FeederIOReal` and `FeederIOSim` implementations, the `Feeder` subsystem, and the `FeederDemo` class with `main`'s signature and braces.

```java
public class FeederDemo
{
    public static void main(String[] args)
    {
        // main body goes here
    }
}

class FeederInputs
{
    public boolean noteDetected = false;
}

interface FeederIO
{
    void updateInputs(FeederInputs inputs);
}

class FeederIOReal implements FeederIO
{
    @Override
    public void updateInputs(FeederInputs inputs)
    {
        System.out.println("[real] would read the beam-break sensor here");
    }
}

class FeederIOSim implements FeederIO
{
    @Override
    public void updateInputs(FeederInputs inputs)
    {
        inputs.noteDetected = true; // simulation: pretend a note is always loaded
    }
}

class Feeder
{
    private FeederIO io;
    private FeederInputs inputs = new FeederInputs();

    public Feeder(FeederIO io)
    {
        this.io = io;
    }

    public void periodic()
    {
        io.updateInputs(inputs);
        System.out.println("Note detected: " + inputs.noteDetected);
    }
}
```

(`FeederDemo`, the public class with `main`, comes first in the file — on Java 17, `java File.java` source-launch only runs the first class in the file; Java 25 is more lenient, but leading with the public class works on both.)

Reorder the fragments below into the body of `main`. It should pick the IO implementation once, based on `runningOnRobot` (hardcoded to `false`, as a stand-in for a real robot check), build the `Feeder` with it, and run one cycle. The program prints `Note detected: true`.

Reorder the fragments below to complete it:

- a. `        Feeder feeder = new Feeder(feederIO);`
- b. `        FeederIO feederIO;`
- c. `        feeder.periodic();`
- d. `        if (runningOnRobot)`
- e. `        {`
- f. `            feederIO = new FeederIOReal();`
- g. `        }`
- h. `        else`
- i. `        {`
- j. `            feederIO = new FeederIOSim();`
- k. `        }`
- l. `        boolean runningOnRobot = false;`

**Answer:** l, b, d, e, f, g, h, i, j, k, a, c

**Interchangeable:** (l, b)

```java
public class FeederDemo
{
    public static void main(String[] args)
    {
        boolean runningOnRobot = false;
        FeederIO feederIO;
        if (runningOnRobot)
        {
            feederIO = new FeederIOReal();
        }
        else
        {
            feederIO = new FeederIOSim();
        }
        Feeder feeder = new Feeder(feederIO);
        feeder.periodic();
    }
}

class FeederInputs
{
    public boolean noteDetected = false;
}

interface FeederIO
{
    void updateInputs(FeederInputs inputs);
}

class FeederIOReal implements FeederIO
{
    @Override
    public void updateInputs(FeederInputs inputs)
    {
        System.out.println("[real] would read the beam-break sensor here");
    }
}

class FeederIOSim implements FeederIO
{
    @Override
    public void updateInputs(FeederInputs inputs)
    {
        inputs.noteDetected = true; // simulation: pretend a note is always loaded
    }
}

class Feeder
{
    private FeederIO io;
    private FeederInputs inputs = new FeederInputs();

    public Feeder(FeederIO io)
    {
        this.io = io;
    }

    public void periodic()
    {
        io.updateInputs(inputs);
        System.out.println("Note detected: " + inputs.noteDetected);
    }
}
```

**Why this order:** `runningOnRobot` (`l`) and the declaration of `feederIO` (`b`) both have to exist before the `if` can read one and assign the other. Neither reads the other, so they can go in either order (hence **Interchangeable:** (l, b)). `feederIO` is declared with the *interface* type `FeederIO`, so it can hold either implementation. The braced `if` (`d`, `e`, `f`, `g`) has to come before its matching `else` (`h`, `i`, `j`, `k`) — every `if`/`else` here uses braces (Lesson 5.1) — and between them, `feederIO` is guaranteed to be assigned no matter which branch runs. This is the one place the program decides real vs. simulated. Only after that can the `Feeder` be constructed with the chosen implementation (`a`). `periodic()` (`c`) runs last, since it needs a `feeder` to call. Inside `periodic()`, `Feeder` pulls fresh values into its cached `inputs` and reads from them. It never knows it was handed the simulated version.
