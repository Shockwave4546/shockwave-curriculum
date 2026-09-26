---
outlineRef: "22 — The Builder Pattern (T5817 30.1)"
pairsWith: "[`lessons/ch22-the-builder-pattern/22-the-builder-pattern.md`](../../lessons/ch22-the-builder-pattern/22-the-builder-pattern.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# The Builder Pattern — Worked Example

## Problem

An elevator's configuration has four settings: a maximum height in meters, a gear ratio, whether the motor uses brake mode, and whether the motor direction is inverted. Most elevators use the usual values (1.0 m max, 10:1 gear ratio, brake mode on, not inverted), so callers should only have to mention the settings they're changing. The finished configuration should never change once it's built.

With a plain constructor this would be `new ElevatorConfig(1.4, 10.0, true, true)`: two `double`s and two `boolean`s in a row, where swapping either pair compiles fine and silently misconfigures the elevator. Build it with the Builder Pattern instead.

## Step 1: Plan It First

1. Write the target class, `ElevatorConfig`, with four `final` fields and a `private` constructor that copies them from a builder.
2. Write a nested `public static class Builder` that holds the same four settings, starting at their usual values.
3. Give the builder one chainable method per setting (each ending in `return this;`), plus a `build()` method.
4. In `main`, build a configuration that changes only two of the four settings.

## Step 2: The Target Class's Fields and Private Constructor

```java
class ElevatorConfig
{
    private final double maxHeightMeters;
    private final double gearRatio;
    private final boolean brakeMode;
    private final boolean inverted;

    private ElevatorConfig(Builder builder)
    {
        this.maxHeightMeters = builder.maxHeightMeters;
        this.gearRatio = builder.gearRatio;
        this.brakeMode = builder.brakeMode;
        this.inverted = builder.inverted;
    }
}
```

- Every field is `final`, so each is assigned exactly once, in the constructor, and can never change afterward. The finished `ElevatorConfig` is immutable.
- The constructor is `private`, so code outside `ElevatorConfig` can't call `new ElevatorConfig(...)`. The only way to get one is through the builder.
- The constructor takes the finished `Builder` and copies its four values across. It can read `builder.maxHeightMeters` even though that field is `private`, because `Builder` is nested inside `ElevatorConfig`. Java lets the outer class and its nested class reach each other's private members.

## Step 3: The Nested Builder

```java
public static class Builder
{
    private double maxHeightMeters = 1.0;
    private double gearRatio = 10.0;
    private boolean brakeMode = true;
    private boolean inverted = false;

    public Builder setMaxHeightMeters(double max) { this.maxHeightMeters = max; return this; }
    public Builder setGearRatio(double ratio) { this.gearRatio = ratio; return this; }
    public Builder setBrakeMode(boolean brake) { this.brakeMode = brake; return this; }
    public Builder setInverted(boolean inverted) { this.inverted = inverted; return this; }

    public ElevatorConfig build() { return new ElevatorConfig(this); }
}
```

- The builder's fields start at the usual values. A setting nobody changes just keeps its starting value, with no extra constructor overload needed.
- Each setter's return type is `Builder`, and it ends in `return this;`, handing back the same builder it was called on. That's what lets the next call chain straight on.
- `build()` passes `this` (the finished builder) to the private constructor from Step 2. It can call that constructor because `Builder` lives inside `ElevatorConfig`.

This whole `Builder` class goes inside `ElevatorConfig`'s braces, after the constructor. A `describe()` method is also added to `ElevatorConfig` so the program can print the result.

## Step 4: Build One in `main`

```java
ElevatorConfig compBot = new ElevatorConfig.Builder()
    .setMaxHeightMeters(1.4)
    .setInverted(true)
    .build();
```

Read it top to bottom. `new ElevatorConfig.Builder()` creates a builder with the usual values. `.setMaxHeightMeters(1.4)` and `.setInverted(true)` each change one setting and return the same builder. `.build()` ends the chain and produces the real `ElevatorConfig`. Gear ratio and brake mode are never mentioned, so they keep their starting values. Every argument sits right next to its name, so there's no way to mix up which `double` or which `boolean` is which.

## Step 5: The Whole Program

To run this as one file, both classes go in `ElevatorSetup.java`. Java allows only one `public` class per file — the one whose name matches the file — so `ElevatorConfig` is written without `public`. The class holding `main` goes first: on Java 17, running a file with `java ElevatorSetup.java` starts the *first* class in the file, so `main` must live there. Java 25 is more forgiving (it also finds the class named after the file), but main-class-first works on both, so every multi-class program in this course uses it.

```java
public class ElevatorSetup
{
    public static void main(String[] args)
    {
        ElevatorConfig compBot = new ElevatorConfig.Builder()
            .setMaxHeightMeters(1.4)
            .setInverted(true)
            .build();

        System.out.println("Comp bot elevator: " + compBot.describe());
    }
}

class ElevatorConfig
{
    private final double maxHeightMeters;
    private final double gearRatio;
    private final boolean brakeMode;
    private final boolean inverted;

    private ElevatorConfig(Builder builder)
    {
        this.maxHeightMeters = builder.maxHeightMeters;
        this.gearRatio = builder.gearRatio;
        this.brakeMode = builder.brakeMode;
        this.inverted = builder.inverted;
    }

    public String describe()
    {
        return "max height " + maxHeightMeters + " m, gear ratio " + gearRatio
            + ":1, brake mode " + brakeMode + ", inverted " + inverted;
    }

    public static class Builder
    {
        private double maxHeightMeters = 1.0;
        private double gearRatio = 10.0;
        private boolean brakeMode = true;
        private boolean inverted = false;

        public Builder setMaxHeightMeters(double max) { this.maxHeightMeters = max; return this; }
        public Builder setGearRatio(double ratio) { this.gearRatio = ratio; return this; }
        public Builder setBrakeMode(boolean brake) { this.brakeMode = brake; return this; }
        public Builder setInverted(boolean inverted) { this.inverted = inverted; return this; }

        public ElevatorConfig build() { return new ElevatorConfig(this); }
    }
}
```

## What It Prints

```
Comp bot elevator: max height 1.4 m, gear ratio 10.0:1, brake mode true, inverted true
```

`max height` and `inverted` show the two values that were set in the chain. `gear ratio` and `brake mode` show the builder's starting values (`10.0` and `true`), because the chain never touched them.

## What the Private Constructor Blocks

Because `main` lives in a different class (`ElevatorSetup`), trying to skip the builder fails to compile:

```java
ElevatorConfig compBot = new ElevatorConfig(new ElevatorConfig.Builder()); // compile error
```

The compiler reports `ElevatorConfig(Builder) has private access in ElevatorConfig`. That's the point of the `private` constructor: callers can only get an `ElevatorConfig` by finishing a builder chain with `.build()`.

## What Forgetting `return this;` Would Look Like

If one setter were written as `void` without `return this;`:

```java
public void setMaxHeightMeters(double max) { this.maxHeightMeters = max; }
```

then the chain in `main` breaks at the very next call. `.setMaxHeightMeters(1.4)` now returns nothing, so there's no object for `.setInverted(true)` to be called on. The compiler reports `void cannot be dereferenced` on the `.setInverted(true)` line. Each `return this;` is what gives the next call in the chain something to call.

## Recap

- The target class has `final` fields and a `private` constructor that takes a finished `Builder`, so the object can only be made through the builder and never changes once built.
- The nested `public static class Builder` holds each setting with a sensible starting value, so callers only mention the settings they change.
- Every builder method returns `Builder` and ends in `return this;`, which makes the fluent chain possible.
- `build()` ends the chain by passing the finished builder to the private constructor.
- Named calls like `.setInverted(true)` replace anonymous positional arguments, so two same-typed settings can't be silently swapped.
