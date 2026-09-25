---
outlineRef: "21 — Static Factories (T5817 30.2)"
pairsWith: "[`lessons/ch21-static-factories/21-static-factories.md`](../../lessons/ch21-static-factories/21-static-factories.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Static Factories — Worked Example

## Problem

The robot's LED strip should show the team's alliance color: solid red on the red alliance, solid blue on the blue alliance, and blinking yellow as a warning when the alliance isn't known yet. Several parts of the robot code need "the right pattern for this alliance." Write one static factory method that makes that choice, so no caller ever has to pick the concrete pattern class itself.

## Step 1: Plan It First

1. Define an interface, `LedPattern`, as the one type every caller works with.
2. Write the concrete pattern classes that implement it.
3. Write a static factory method that takes the alliance name and returns the right `LedPattern`.
4. Call the factory from `main` for a known alliance and an unknown one.

## Step 2: The Interface Every Caller Uses

```java
interface LedPattern
{
    String describe();
}
```

A real LED pattern would drive the strip. `describe()` stands in for that here, so the program can print which pattern it got.

## Step 3: The Concrete Patterns

```java
class SolidColor implements LedPattern
{
    private String color;

    public SolidColor(String color)
    {
        this.color = color;
    }

    @Override
    public String describe()
    {
        return "solid " + color;
    }
}

class BlinkingYellow implements LedPattern
{
    @Override
    public String describe()
    {
        return "blinking yellow";
    }
}
```

There are two different concrete classes, and both honor the same `LedPattern` contract.

## Step 4: The Factory Method

```java
class LedPatterns
{
    public static LedPattern forAlliance(String alliance)
    {
        if (alliance.equals("Red"))
        {
            return new SolidColor("red");
        }
        else if (alliance.equals("Blue"))
        {
            return new SolidColor("blue");
        }
        else
        {
            return new BlinkingYellow(); // alliance not known yet: warn the drive team
        }
    }
}
```

Three things make this a proper static factory, all straight from the lesson:

- **It's `public static`.** Callers use the class name, `LedPatterns.forAlliance(...)`. They don't need an `LedPatterns` object first.
- **It has a descriptive name.** `LedPatterns.forAlliance("Red")` says what you're getting. Compare that with `new SolidColor("red")`, which makes the caller already know which class and which color string to use.
- **It returns the interface type, `LedPattern`.** Inside, it picks between two completely different concrete classes. The caller only ever sees `LedPattern`, so the choice stays hidden in this one method.

The alliance names are compared with `.equals()` (Ch.6), not `==`, since they're `String`s.

## Step 5: Call It From `main`

```java
public class LedDemo
{
    public static void main(String[] args)
    {
        LedPattern blueLights = LedPatterns.forAlliance("Blue");
        LedPattern unknownLights = LedPatterns.forAlliance("");

        System.out.println("Blue alliance: " + blueLights.describe());
        System.out.println("No alliance yet: " + unknownLights.describe());
    }
}
```

Neither line in `main` says `new`, and neither mentions `SolidColor` or `BlinkingYellow`. Both variables are declared as `LedPattern`, and each `describe()` call dispatches to whichever concrete class the factory picked.

## Step 6: The Whole Program

```java
interface LedPattern
{
    String describe();
}

class SolidColor implements LedPattern
{
    private String color;

    public SolidColor(String color)
    {
        this.color = color;
    }

    @Override
    public String describe()
    {
        return "solid " + color;
    }
}

class BlinkingYellow implements LedPattern
{
    @Override
    public String describe()
    {
        return "blinking yellow";
    }
}

class LedPatterns
{
    public static LedPattern forAlliance(String alliance)
    {
        if (alliance.equals("Red"))
        {
            return new SolidColor("red");
        }
        else if (alliance.equals("Blue"))
        {
            return new SolidColor("blue");
        }
        else
        {
            return new BlinkingYellow(); // alliance not known yet: warn the drive team
        }
    }
}

public class LedDemo
{
    public static void main(String[] args)
    {
        LedPattern blueLights = LedPatterns.forAlliance("Blue");
        LedPattern unknownLights = LedPatterns.forAlliance("");

        System.out.println("Blue alliance: " + blueLights.describe());
        System.out.println("No alliance yet: " + unknownLights.describe());
    }
}
```

## What It Prints

```
Blue alliance: solid blue
No alliance yet: blinking yellow
```

`"Blue"` matches the `else if`, so the factory builds a `SolidColor("blue")`. The empty string `""` matches neither name and falls through to the `else`, so it builds a `BlinkingYellow`.

## What Returning the Concrete Type Would Look Like

The lesson warns against a factory whose return type is a specific class instead of the interface. Say the signature were changed to:

```java
public static SolidColor forAlliance(String alliance)
```

This version doesn't compile at all. The compiler rejects `return new BlinkingYellow();` with `incompatible types: BlinkingYellow cannot be converted to SolidColor`. A factory locked to one concrete return type loses the freedom to choose between implementations, which is the main reason to write one. Declaring the return type as `LedPattern` is what keeps that choice open.

## Recap

- A static factory method is a `public static` method that returns an object, called in place of `new`.
- Its name describes what the caller is getting (`forAlliance`), and its logic decides which concrete class to build.
- It returns the interface type (`LedPattern`), so callers depend only on the interface and never learn which class was picked.
- The decision lives in exactly one method, so every part of the code that needs an LED pattern gets the same logic without repeating it.
