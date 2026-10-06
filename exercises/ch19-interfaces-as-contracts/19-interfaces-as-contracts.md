---
outlineRef: "19 — Interfaces as Contracts (ORACLE 15.1-6)"
pairsWith: "[`lessons/ch19-interfaces-as-contracts/19-interfaces-as-contracts.md`](../../lessons/ch19-interfaces-as-contracts/19-interfaces-as-contracts.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
---

# Interfaces as Contracts — Exercises

## Multiple Choice

**Question:** Given these two interfaces and one class:

```java
interface Aimable
{
    void aimAt(double degrees);
}

interface Reportable
{
    String getReport();

    default void printReport()
    {
        System.out.println(getReport());
    }
}

class Turret implements Aimable, Reportable
{
    private double angle;

    @Override
    public void aimAt(double degrees)
    {
        angle = degrees;
    }

    @Override
    public String getReport()
    {
        return "Turret at " + angle + " degrees";
    }
}
```

`Turret` never writes a `printReport()` method. What happens?

**Options:**

- A. It doesn't compile — `Turret` is missing `printReport()`, which `Reportable` declares
- B. It doesn't compile — a class can only implement one interface
- C. It compiles, and `Turret` inherits `printReport()` from `Reportable`'s default method
- D. It compiles, but calling `printReport()` on a `Turret` crashes at runtime because `Turret` never wrote it

**Answer:** C

**Why:** `Turret` implements both interfaces, and it provides a body for every abstract method they declare: `aimAt(double)` from `Aimable` and `getReport()` from `Reportable`. `printReport()` isn't abstract — it's a `default` method with its own body inside `Reportable` — so `Turret` inherits it automatically and doesn't have to write it.

- A is wrong — only abstract (no-body) methods are required. A `default` method already has a body, so implementing classes get it for free.
- B is wrong — that's the rule for `extends` (exactly one superclass). A class can `implements` as many interfaces as it needs, comma-separated.
- D is wrong — the inherited default is a real method with a real body. Calling it on a `Turret` would print that turret's report, e.g. `Turret at 30.0 degrees` after `aimAt(30.0)`.

## Micro-Parsons

**Problem:** Given this `Scorer` interface and `main` method, reorder the fragments below into the `SpeakerShot` class that goes where the comment is. `SpeakerShot` must implement the `Scorer` contract, returning `2` points, so the program prints `Points: 2`.

```java
public class ScoreTest
{
    public static void main(String[] args)
    {
        Scorer shot = new SpeakerShot();
        System.out.println("Points: " + shot.getPoints());
    }
}

interface Scorer
{
    int getPoints();
}

// SpeakerShot class goes here
```

(`ScoreTest`, the public class with `main`, comes first in the file — on Java 17, `java File.java` source-launch only runs the first class in the file; Java 25 is more lenient, but leading with the public class works on both.)

Reorder the fragments below to complete it:

- a. `    {`
- b. `class SpeakerShot implements Scorer`
- c. `    }`
- d. `        return 2;`
- e. `}`
- f. `    public int getPoints()`
- g. `{`
- h. `    @Override`

**Answer:** b, g, h, f, a, d, c, e

```java
public class ScoreTest
{
    public static void main(String[] args)
    {
        Scorer shot = new SpeakerShot();
        System.out.println("Points: " + shot.getPoints());
    }
}

interface Scorer
{
    int getPoints();
}

class SpeakerShot implements Scorer
{
    @Override
    public int getPoints()
    {
        return 2;
    }
}
```

**Why this order:** The class declaration (`b`) comes first — `implements Scorer` is what signs the contract, and it's also what lets `main` store a `SpeakerShot` in a `Scorer`-typed variable. The class's opening brace (`g`) follows. `@Override` (`h`) goes directly above the method signature (`f`), which has to match the interface's `int getPoints()` — without this method, `SpeakerShot` would be missing a required part of the contract and wouldn't compile. The method's opening brace (`a`), its `return` statement (`d`), and its closing brace (`c`) follow, and the class's closing brace (`e`) comes last. `ScoreTest` and the `Scorer` interface are the given scaffold, with `SpeakerShot` inserted where the comment was.

## Coding

**Mode:** full-program

**Problem:** The intake's hardware layer is a contract. Write the interface `IntakeIO` and the class `SimIntakeIO` that
implements it, so the fixed `main` below works.

`IntakeIO` must declare:

- a constant `MAX_VOLTS` equal to `12.0`
- one abstract method `void setVoltage(double volts)`
- a **default** method `void stop()` that is built on `setVoltage` (it commands `0.0` volts)
- a **static** method `double clampVolts(double v)` that limits `v` to the range `-MAX_VOLTS` to `MAX_VOLTS`
  (so `14.0` becomes `12.0` and `-20.0` becomes `-12.0`; values already in range come back unchanged)

`SimIntakeIO implements IntakeIO`. It remembers the most recent voltage it was given
(`double getLastVolts()`, which is `0.0` before any command) and counts how many times `setVoltage` has been
called (`int getCommandCount()`). It must **not** write its own `stop()`; it inherits the default one, so
the `stop()` call in `main` counts as one more command.

`main` reads a count, then that many voltages.

**Starter:**

```java
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        SimIntakeIO sim = new SimIntakeIO();
        IntakeIO io = sim; // main only sees the contract
        for (int i = 0; i < count; i++)
        {
            double requested = in.nextDouble();
            double applied = IntakeIO.clampVolts(requested);
            io.setVoltage(applied);
            System.out.println("Applied: " + sim.getLastVolts());
        }
        io.stop();
        System.out.println("After stop: " + sim.getLastVolts());
        System.out.println("Commands: " + sim.getCommandCount());
        System.out.println("Limit: " + IntakeIO.MAX_VOLTS);
    }
}

// TODO: write the interface IntakeIO

// TODO: write the class SimIntakeIO
```

**Scenario 1 (visible):**

**Input:**

```text
3
6.5 14.0 3.0
```

**Expected output:**

```text
Applied: 6.5
Applied: 12.0
Applied: 3.0
After stop: 0.0
Commands: 4
Limit: 12.0
```

**Scenario 2 (visible):**

**Input:**

```text
2
-4.0 0.0
```

**Expected output:**

```text
Applied: -4.0
Applied: 0.0
After stop: 0.0
Commands: 3
Limit: 12.0
```

**Scenario 3 (visible):**

**Input:**

```text
1
12.0
```

**Expected output:**

```text
Applied: 12.0
After stop: 0.0
Commands: 2
Limit: 12.0
```

**Scenario 4 (hidden):**

**Input:**

```text
3
-20.0 20.0 -12.0
```

**Expected output:**

```text
Applied: -12.0
Applied: 12.0
Applied: -12.0
After stop: 0.0
Commands: 4
Limit: 12.0
```

**Scenario 5 (hidden):**

**Input:**

```text
1
-13.5
```

**Expected output:**

```text
Applied: -12.0
After stop: 0.0
Commands: 2
Limit: 12.0
```

**Scenario 6 (hidden):**

**Input:**

```text
0
```

**Expected output:**

```text
After stop: 0.0
Commands: 1
Limit: 12.0
```

**Solution:**

```java
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        SimIntakeIO sim = new SimIntakeIO();
        IntakeIO io = sim; // main only sees the contract
        for (int i = 0; i < count; i++)
        {
            double requested = in.nextDouble();
            double applied = IntakeIO.clampVolts(requested);
            io.setVoltage(applied);
            System.out.println("Applied: " + sim.getLastVolts());
        }
        io.stop();
        System.out.println("After stop: " + sim.getLastVolts());
        System.out.println("Commands: " + sim.getCommandCount());
        System.out.println("Limit: " + IntakeIO.MAX_VOLTS);
    }
}

interface IntakeIO
{
    double MAX_VOLTS = 12.0;

    void setVoltage(double volts);

    default void stop()
    {
        setVoltage(0.0);
    }

    static double clampVolts(double v)
    {
        return Math.max(-MAX_VOLTS, Math.min(MAX_VOLTS, v));
    }
}

class SimIntakeIO implements IntakeIO
{
    private double lastVolts = 0.0;
    private int commandCount = 0;

    @Override
    public void setVoltage(double volts)
    {
        lastVolts = volts;
        commandCount++;
    }

    public double getLastVolts()
    {
        return lastVolts;
    }

    public int getCommandCount()
    {
        return commandCount;
    }
}
```

**Why:** The interface holds all four kinds of member Lesson 19 covers: an implicitly `public static final` constant, an abstract
method every implementer must supply, a `default` method that builds on that abstract method, and a `static` method called on
the interface name. `SimIntakeIO` must write `setVoltage` as `public` (interface methods are implicitly public) and gets `stop()` for free,
which calls *its own* `setVoltage`, so the command count goes up. Typical mistakes: a `stop()` that doesn't call `setVoltage` (the last voltage and the
command count come out wrong), and a `clampVolts` that only limits the top end, which fails on a large negative voltage.
