---
outlineRef: "21 — Static Factories (T5817 30.2)"
pairsWith: "[`lessons/ch21-static-factories/21-static-factories.md`](../../lessons/ch21-static-factories/21-static-factories.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
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
