---
outlineRef: "12 — Exceptions & try/catch (ORACLE 11.1-16)"
pairsWith: "[`lessons/ch12-exceptions-and-try-catch/12-exceptions-and-try-catch.md`](../../lessons/ch12-exceptions-and-try-catch/12-exceptions-and-try-catch.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Exceptions & try/catch — Worked Example

## Problem

The pit crew can type a climber speed into the dashboard before a match. Motor speeds only make sense between `-1.0` and `1.0`, so a method that sets the climber speed should refuse anything outside that range. The code that reads the dashboard value should recover when the number is bad instead of crashing, and it should always log that the request was handled, whether or not the speed was accepted.

## Step 1: Plan It First

1. Write `setClimberSpeed`, which **throws** an exception when the speed is out of range.
2. Call it with a bad value and see what happens when nothing catches the exception.
3. Wrap the call in `try`/`catch` so a bad value is rejected cleanly.
4. Add a `finally` block for the "request handled" log line that must always print.

## Step 2: Throw When the Speed Is Out of Range

```java
public static void setClimberSpeed(double speed)
{
    if (speed < -1.0 || speed > 1.0)
    {
        throw new IllegalArgumentException("Climber speed out of range: " + speed);
    }
    System.out.println("Climber running at " + speed);
}
```

`throw` creates an `IllegalArgumentException` object that describes the problem and hands it to the Java runtime. The method stops right there, so the `println` below it never runs for a bad speed. `IllegalArgumentException` is unchecked (a `RuntimeException`), so the method doesn't need a `throws` clause.

## Step 3: Call It Without Any Handler

```java
public class ClimberControl
{
    public static void setClimberSpeed(double speed)
    {
        if (speed < -1.0 || speed > 1.0)
        {
            throw new IllegalArgumentException("Climber speed out of range: " + speed);
        }
        System.out.println("Climber running at " + speed);
    }

    public static void main(String[] args)
    {
        double requestedSpeed = 1.5; // stand-in for a value typed into the dashboard
        setClimberSpeed(requestedSpeed);
        System.out.println("Climb command sent");
    }
}
```

Output:

```
Exception in thread "main" java.lang.IllegalArgumentException: Climber speed out of range: 1.5
	at ClimberControl.setClimberSpeed(ClimberControl.java:7)
	at ClimberControl.main(ClimberControl.java:15)
```

The runtime searched back up the call stack, first `setClimberSpeed` and then `main`, and found no handler, so it ended the program. `"Climb command sent"` never printed. On a robot, this is the kind of crash that turns the "Robot Code" indicator red.

## Step 4: Catch It and Recover

A speed typed into the dashboard can be wrong, and the robot can recover from that by leaving the climber stopped. So `main` wraps the call in `try`/`catch`:

```java
public static void main(String[] args)
{
    double requestedSpeed = 1.5; // stand-in for a value typed into the dashboard
    try
    {
        setClimberSpeed(requestedSpeed);
        System.out.println("Climb command sent");
    }
    catch (IllegalArgumentException e)
    {
        System.out.println("Rejected dashboard speed - climber stays stopped");
    }
}
```

Output:

```
Rejected dashboard speed - climber stays stopped
```

When `setClimberSpeed` throws, execution jumps straight into the matching `catch` block, and the rest of the `try` block (`"Climb command sent"`) is skipped. The `catch` block doesn't stay silent, either: it reports what happened, so the problem isn't swallowed.

## Step 5: Always Log That the Request Was Handled

The "request handled" line has to print on both paths, accepted and rejected. Rather than writing it once at the end of `try` and again at the end of `catch`, it goes in `finally`:

```java
public class ClimberControl
{
    public static void setClimberSpeed(double speed)
    {
        if (speed < -1.0 || speed > 1.0)
        {
            throw new IllegalArgumentException("Climber speed out of range: " + speed);
        }
        System.out.println("Climber running at " + speed);
    }

    public static void main(String[] args)
    {
        double requestedSpeed = 1.5; // stand-in for a value typed into the dashboard
        try
        {
            setClimberSpeed(requestedSpeed);
            System.out.println("Climb command sent");
        }
        catch (IllegalArgumentException e)
        {
            System.out.println("Rejected dashboard speed - climber stays stopped");
        }
        finally
        {
            System.out.println("Climb request handled");
        }
    }
}
```

Output with `requestedSpeed = 1.5`:

```
Rejected dashboard speed - climber stays stopped
Climb request handled
```

## Step 6: Check the Other Path

Changing the dashboard value to a legal speed, `requestedSpeed = 0.6`, and running again:

```
Climber running at 0.6
Climb command sent
Climb request handled
```

Nothing is thrown, so the whole `try` block runs and the `catch` block is skipped entirely. `finally` still runs, which is the whole point of putting the log line there.

## Recap

- `throw new SomeException(...)` stops the method and hands an exception object to the runtime.
- If nothing up the call stack catches it, the program ends, and any code after the throw never runs.
- A `catch` block for the matching type lets the caller recover. The rest of the `try` block is skipped when an exception jumps to it.
- `finally` runs whether or not an exception happened, so code that must always run belongs there.
- `IllegalArgumentException` is unchecked, so neither a `throws` clause nor a `try`/`catch` is required by the compiler. The `catch` here is a choice, made because a bad dashboard value is a situation the robot can reasonably recover from.
