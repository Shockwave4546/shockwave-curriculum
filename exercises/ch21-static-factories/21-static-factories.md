---
outlineRef: "21 — Static Factories (T5817 30.2)"
pairsWith: "[`lessons/ch21-static-factories/21-static-factories.md`](../../lessons/ch21-static-factories/21-static-factories.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
---

# Static Factories — Exercises

## Multiple Choice

**Question:** `Arm` is an interface, and `RealArm` and `SimArm` both implement it. A teammate is writing a factory method that returns either a `RealArm` or a `SimArm` depending on whether the code is on the robot. Which method signature best follows this lesson's guidance?

**Options:**

- A. `public static Arm createArm(boolean onRobot)`
- B. `public static RealArm createArm(boolean onRobot)`
- C. `public Arm createArm(boolean onRobot)`
- D. `public static void createArm(boolean onRobot)`

**Answer:** A

**Why:** A static factory is `public static`, so callers can use the class name directly, and it returns the *interface* type. Returning `Arm` lets the method hand back either a `RealArm` or a `SimArm`, and the caller never learns which one it got.

- B is wrong. With `RealArm` as the return type, the method can't return a `SimArm` at all (it won't compile), and every caller is locked into one concrete class. This is the lesson's "returning a concrete class instead of an interface" pitfall.
- C is wrong. Without `static`, the method belongs to an object, so a caller would first need an instance of the factory class just to call it. Static factories are called directly on the class name.
- D is wrong. A factory's whole job is to return the object it built. A `void` method can't hand anything back to the caller.

## Micro-Parsons

**Problem:** You're given everything in the program below except the `GripperFactory` class: the `Gripper` interface, its `RealGripper` and `SimGripper` implementations, and the `GripperDemo` class with `main`.

```java
public class GripperDemo
{
    public static void main(String[] args)
    {
        Gripper gripper = GripperFactory.createGripper(false);
        System.out.println(gripper.status());
    }
}

interface Gripper
{
    String status();
}

class RealGripper implements Gripper
{
    @Override
    public String status()
    {
        return "real gripper: reading the real sensor";
    }
}

class SimGripper implements Gripper
{
    @Override
    public String status()
    {
        return "sim gripper: holding";
    }
}

// GripperFactory class goes here
```

Reorder the fragments below into the `GripperFactory` class. It holds one static factory method that returns a `RealGripper` when `onRobot` is `true` and a `SimGripper` otherwise, with `Gripper` as the return type. `main` calls it with `false`, so the program prints `sim gripper: holding`.

Reorder the fragments below to complete it:

- a.
  ```java
  class GripperFactory
  {
  ```
- b. `    public static Gripper createGripper(boolean onRobot)`
- c. `    {`
- d. `        if (onRobot)`
- e. `        {`
- f. `            return new RealGripper();`
- g. `        }`
- h. `        else`
- i. `        {`
- j. `            return new SimGripper();`
- k. `        }`
- l.
  ```java
      }
  }
  ```

**Answer:** a, b, c, d, e, f, g, h, i, j, k, l

```java
public class GripperDemo
{
    public static void main(String[] args)
    {
        Gripper gripper = GripperFactory.createGripper(false);
        System.out.println(gripper.status());
    }
}

interface Gripper
{
    String status();
}

class RealGripper implements Gripper
{
    @Override
    public String status()
    {
        return "real gripper: reading the real sensor";
    }
}

class SimGripper implements Gripper
{
    @Override
    public String status()
    {
        return "sim gripper: holding";
    }
}

class GripperFactory
{
    public static Gripper createGripper(boolean onRobot)
    {
        if (onRobot)
        {
            return new RealGripper();
        }
        else
        {
            return new SimGripper();
        }
    }
}
```

(`GripperDemo`, the public class with `main`, comes first in the file — on Java 17, `java File.java` source-launch only runs the first class in the file; Java 25 is more lenient, but leading with the public class works on both.)

**Why this order:** The class line and its opening brace (`a`, merged — two lines with nothing valid between them) come first. Then the factory method's signature (`b`), which is `public static` so `main` can call it as `GripperFactory.createGripper(...)` without any `GripperFactory` object, and which returns the interface type `Gripper` so it's free to hand back either implementation. The method's opening brace (`c`) follows. Inside, the braced `if` (`d`, `e`, `f`, `g`) has to come before its matching `else` (`h`, `i`, `j`, `k`) — every `if`/`else` here uses braces (Lesson 5.1). Together they're the one place the real-vs-simulated decision is made. The trailing braces close in reverse, the method's then the class's, merged into one fragment (`l`) since nothing valid can go between two closing braces. `main` only ever sees a `Gripper`, and never mentions `RealGripper` or `SimGripper` itself.

## Coding

**Mode:** full-program

**Problem:** Write two classes that use static factory methods. The interface `Drivetrain` and its three implementations
(`RealDrivetrain`, `PracticeDrivetrain`, `SimDrivetrain`) are given.

**`DrivetrainFactory`** is a factory-only class: it has a `private` constructor and one method,
`public static Drivetrain create(String mode)`. It uses a `switch` **expression** on `mode`:
`"real"` gives a `RealDrivetrain`, `"practice"` gives a `PracticeDrivetrain`, and anything else, **including `null`** (nothing selected),
gives a `SimDrivetrain`. The return type is the interface, not a concrete class.

**`SensorLog`** is a cached instance. Its constructor is `private`; `public static SensorLog getInstance()` always returns the
**same** object. `void record(String entry)` adds one to a counter and `int getCount()` returns it (the entry text itself isn't stored).

`main` reads a count, then that many modes (the word `none` is turned into `null`).

**Starter:**

```java
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        int count = in.nextInt();
        for (int i = 0; i < count; i++)
        {
            String mode = in.next();
            if (mode.equals("none"))
            {
                mode = null; // nothing was selected
            }
            Drivetrain drivetrain = DrivetrainFactory.create(mode);
            System.out.println(mode + " -> " + drivetrain.describe());
            SensorLog.getInstance().record(mode);
        }
        SensorLog first = SensorLog.getInstance();
        SensorLog second = SensorLog.getInstance();
        System.out.println("Same log: " + (first == second));
        System.out.println("Entries: " + first.getCount());
    }
}

interface Drivetrain
{
    String describe();
}

class RealDrivetrain implements Drivetrain
{
    public String describe()
    {
        return "real motors";
    }
}

class PracticeDrivetrain implements Drivetrain
{
    public String describe()
    {
        return "practice bot";
    }
}

class SimDrivetrain implements Drivetrain
{
    public String describe()
    {
        return "simulation";
    }
}

// TODO: write the class DrivetrainFactory

// TODO: write the class SensorLog
```

**Scenario 1 (visible):**

**Input:**

```text
3
real
sim
practice
```

**Expected output:**

```text
real -> real motors
sim -> simulation
practice -> practice bot
Same log: true
Entries: 3
```

**Scenario 2 (visible):**

**Input:**

```text
2
real
real
```

**Expected output:**

```text
real -> real motors
real -> real motors
Same log: true
Entries: 2
```

**Scenario 3 (visible):**

**Input:**

```text
1
tank
```

**Expected output:**

```text
tank -> simulation
Same log: true
Entries: 1
```

**Scenario 4 (hidden):**

**Input:**

```text
3
none
real
none
```

**Expected output:**

```text
null -> simulation
real -> real motors
null -> simulation
Same log: true
Entries: 3
```

**Scenario 5 (hidden):**

**Input:**

```text
2
REAL
practice
```

**Expected output:**

```text
REAL -> simulation
practice -> practice bot
Same log: true
Entries: 2
```

**Scenario 6 (hidden):**

**Input:**

```text
1
none
```

**Expected output:**

```text
null -> simulation
Same log: true
Entries: 1
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
        for (int i = 0; i < count; i++)
        {
            String mode = in.next();
            if (mode.equals("none"))
            {
                mode = null; // nothing was selected
            }
            Drivetrain drivetrain = DrivetrainFactory.create(mode);
            System.out.println(mode + " -> " + drivetrain.describe());
            SensorLog.getInstance().record(mode);
        }
        SensorLog first = SensorLog.getInstance();
        SensorLog second = SensorLog.getInstance();
        System.out.println("Same log: " + (first == second));
        System.out.println("Entries: " + first.getCount());
    }
}

interface Drivetrain
{
    String describe();
}

class RealDrivetrain implements Drivetrain
{
    public String describe()
    {
        return "real motors";
    }
}

class PracticeDrivetrain implements Drivetrain
{
    public String describe()
    {
        return "practice bot";
    }
}

class SimDrivetrain implements Drivetrain
{
    public String describe()
    {
        return "simulation";
    }
}

class DrivetrainFactory
{
    private DrivetrainFactory() {}

    public static Drivetrain create(String mode)
    {
        return switch (mode)
        {
            case "real" -> new RealDrivetrain();
            case "practice" -> new PracticeDrivetrain();
            case null, default -> new SimDrivetrain();
        };
    }
}

class SensorLog
{
    private static final SensorLog INSTANCE = new SensorLog();
    private int count = 0;

    private SensorLog() {}

    public static SensorLog getInstance()
    {
        return INSTANCE;
    }

    public void record(String entry)
    {
        count++;
    }

    public int getCount()
    {
        return count;
    }
}
```

**Why:** `DrivetrainFactory` is the lesson's "choose an implementation by condition" factory: the caller never names a concrete class, and the return type is the interface.
A plain `default` doesn't catch `null`, and switching on a `null` string throws `NullPointerException`, so `case null, default ->` is what makes the `none` scenarios work.
`SensorLog` shows the other payoff of a factory: it returns the *same* cached object every call. A `getInstance()` that writes `return new SensorLog();` still compiles, but
`Same log` prints `false` and `Entries` prints `0`. Writing only `default ->` (no `case null`) crashes on the hidden scenarios that select nothing.
