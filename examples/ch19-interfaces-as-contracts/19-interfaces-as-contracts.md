---
outlineRef: "19 — Interfaces as Contracts (ORACLE 15.1-6)"
pairsWith: "[`lessons/ch19-interfaces-as-contracts/19-interfaces-as-contracts.md`](../../lessons/ch19-interfaces-as-contracts/19-interfaces-as-contracts.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Interfaces as Contracts — Worked Example

## Problem

The robot might use either of two different distance sensors to detect the wall: a laser sensor or a sonar sensor. They work completely differently inside, but the code that uses them only needs one thing — "tell me the distance in meters." Write a contract both sensors agree to, a method that works with either one, and then add a "too close?" check to every sensor at once without editing either sensor class.

## Step 1: Write the Contract

The one thing every range finder must be able to do is report a distance. That's a method signature with no body:

```java
interface RangeFinder
{
    double getDistanceMeters();
}
```

This says *what* a `RangeFinder` can do, but nothing about *how*.

## Step 2: Two Classes Sign the Contract

Each sensor class `implements RangeFinder`, which obligates it to provide a real body for `getDistanceMeters()`. Since there's no real hardware here, each one just holds a reading passed in when it's built, standing in for what the sensor would measure:

```java
class LaserRangeFinder implements RangeFinder
{
    private double reading;

    public LaserRangeFinder(double reading)
    {
        this.reading = reading;
    }

    @Override
    public double getDistanceMeters()
    {
        return reading;
    }
}

class SonarRangeFinder implements RangeFinder
{
    private double readingInches;

    public SonarRangeFinder(double readingInches)
    {
        this.readingInches = readingInches;
    }

    @Override
    public double getDistanceMeters()
    {
        return readingInches * 0.0254; // this sensor measures in inches, so convert
    }
}
```

The two bodies are different — the sonar one converts from inches — but both honor the same contract. If either class left `getDistanceMeters()` out, it wouldn't compile.

## Step 3: Code Against the Interface Type

`RangeFinder` is a real type, so a method parameter can be declared as one. The method then works with *any* class that implements it:

```java
public static void checkWall(RangeFinder sensor)
{
    System.out.println("Wall is " + sensor.getDistanceMeters() + " m away");
}
```

`checkWall` never needs to know whether it was handed a laser or a sonar sensor.

## Step 4: Add a Default Method to Every Sensor at Once

Now the team wants a "too close?" check. Adding a plain method signature to `RangeFinder` would break both classes — each would suddenly be missing a required method. A `default` method provides the body right in the interface instead, so both classes inherit it with no edits:

```java
interface RangeFinder
{
    double getDistanceMeters();

    default boolean isTooClose()
    {
        return getDistanceMeters() < 0.5;
    }
}
```

`isTooClose()` calls `getDistanceMeters()`, which every implementing class is guaranteed to have — so the default works for any `RangeFinder`, using that class's own distance.

## Step 5: Put It Together

`checkWall` gets one more line here, printing the new `isTooClose()` check alongside the distance:

```java
interface RangeFinder
{
    double getDistanceMeters();

    default boolean isTooClose()
    {
        return getDistanceMeters() < 0.5;
    }
}

class LaserRangeFinder implements RangeFinder
{
    private double reading;

    public LaserRangeFinder(double reading)
    {
        this.reading = reading;
    }

    @Override
    public double getDistanceMeters()
    {
        return reading;
    }
}

class SonarRangeFinder implements RangeFinder
{
    private double readingInches;

    public SonarRangeFinder(double readingInches)
    {
        this.readingInches = readingInches;
    }

    @Override
    public double getDistanceMeters()
    {
        return readingInches * 0.0254; // this sensor measures in inches, so convert
    }
}

public class WallCheck
{
    public static void checkWall(RangeFinder sensor)
    {
        System.out.println("Wall is " + sensor.getDistanceMeters() + " m away");
        System.out.println("Too close? " + sensor.isTooClose());
    }

    public static void main(String[] args)
    {
        RangeFinder laser = new LaserRangeFinder(1.25);
        RangeFinder sonar = new SonarRangeFinder(10.0);

        checkWall(laser);
        checkWall(sonar);
    }
}
```

## What It Prints

```
Wall is 1.25 m away
Too close? false
Wall is 0.254 m away
Too close? true
```

Both variables are declared as `RangeFinder`, and `checkWall` only ever sees a `RangeFinder` — but each call runs that object's own `getDistanceMeters()`. Neither sensor class mentions `isTooClose()`, yet both have it, inherited from the interface's default.

## Recap

- An interface is a contract: method signatures with no body, saying *what* an implementing class can do, not *how*.
- A class agrees to the contract with `implements`, and must provide a body for every abstract method the interface declares — or it won't compile.
- An interface is a real type: a parameter declared as `RangeFinder` accepts any class that implements it.
- A `default` method has a body inside the interface; every implementing class inherits it automatically, which is how an interface can grow a new method without breaking existing classes.
