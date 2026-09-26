---
outlineRef: "24 — Optional: Avoiding Null Pointer Exceptions (ORACLE 16.1) — renamed from \"Optional: Maybe a Value\" to disambiguate from optional method parameters; the deck's actual slide heading is unchanged"
pairsWith: "[`lessons/ch24-optional-avoiding-null-pointer-exceptions/24-optional-avoiding-null-pointer-exceptions.md`](../../lessons/ch24-optional-avoiding-null-pointer-exceptions/24-optional-avoiding-null-pointer-exceptions.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Optional: Avoiding Null Pointer Exceptions — Worked Example

## Problem

The robot logs motor temperatures for each mechanism. Write a method that finds the first temperature above a limit. Sometimes nothing is over the limit, so the method's return type should make it obvious that there might be no result. Then use it on two mechanisms: print a warning only for a mechanism that actually has an over-limit reading, and give the dashboard a number to display either way.

## Step 1: Plan It First

1. Write `firstOverLimit`, returning `Optional<Double>` instead of a plain `double`.
2. Inside it, return `Optional.of(...)` when a reading is found, and `Optional.empty()` when none is.
3. Call it for the drivetrain (which has a hot motor) and the intake (which doesn't).
4. Handle the results with `ifPresent` (warn only if there's a value) and `orElse` (always get a number).

## Step 2: Put "Might Be Absent" in the Return Type

```java
public static Optional<Double> firstOverLimit(double[] temps, double limit)
{
    for (double t : temps)
    {
        if (t > limit)
        {
            return Optional.of(t);
        }
    }
    return Optional.empty();
}
```

- The signature says `Optional<Double>`, so anyone calling it knows from the type alone that there might not be an answer.
- The loop is the same "find the first match" traversal from Ch.9. The moment a reading is over the limit, it's wrapped with `Optional.of(t)` and returned. `t` is a real number here, never `null`, so `of` is the right choice.
- If the loop finishes without finding one, the method returns `Optional.empty()`. That means "no value," and it isn't `null`.
- `Optional<Double>` relies on the same autoboxing from Lesson 9.2 to wrap a `double` as a `Double`. Java also has a specialized `OptionalDouble` (plus `OptionalInt` and `OptionalLong`) that skips the boxing — this example sticks with `Optional<Double>` since it composes with `ifPresent`/`orElse` exactly like every other `Optional<T>` in this lesson.

`Optional` lives in `java.util`, so the file needs `import java.util.Optional;`.

## Step 3: Call It for Two Mechanisms

```java
double[] drivetrainTemps = {41.5, 38.0, 72.5, 44.0};
double[] intakeTemps = {35.0, 36.5};

Optional<Double> drivetrainHot = firstOverLimit(drivetrainTemps, 70.0);
Optional<Double> intakeHot = firstOverLimit(intakeTemps, 70.0);
```

`drivetrainHot` holds `72.5`. `intakeHot` is empty, since neither intake reading is over `70.0`.

## Step 4: Handle Both Cases Without `get()`

```java
drivetrainHot.ifPresent(t -> System.out.println("Drivetrain warning: " + t + " C"));
intakeHot.ifPresent(t -> System.out.println("Intake warning: " + t + " C"));

double intakeDashboard = intakeHot.orElse(0.0);
System.out.println("Intake over-limit reading for the dashboard: " + intakeDashboard);
```

- `ifPresent` runs its lambda (Lesson 19.1) only when there's a value. The drivetrain line prints a warning. The intake line does nothing at all, with no `if` and no `null` check.
- The dashboard needs *some* number every time, so `orElse(0.0)` supplies one: the real reading if there is one, otherwise `0.0`.

## Step 5: The Whole Program

```java
import java.util.Optional;

public class MotorTempCheck
{
    public static Optional<Double> firstOverLimit(double[] temps, double limit)
    {
        for (double t : temps)
        {
            if (t > limit)
            {
                return Optional.of(t);
            }
        }
        return Optional.empty();
    }

    public static void main(String[] args)
    {
        double[] drivetrainTemps = {41.5, 38.0, 72.5, 44.0};
        double[] intakeTemps = {35.0, 36.5};

        Optional<Double> drivetrainHot = firstOverLimit(drivetrainTemps, 70.0);
        Optional<Double> intakeHot = firstOverLimit(intakeTemps, 70.0);

        drivetrainHot.ifPresent(t -> System.out.println("Drivetrain warning: " + t + " C"));
        intakeHot.ifPresent(t -> System.out.println("Intake warning: " + t + " C"));

        double intakeDashboard = intakeHot.orElse(0.0);
        System.out.println("Intake over-limit reading for the dashboard: " + intakeDashboard);
    }
}
```

## What It Prints

```
Drivetrain warning: 72.5 C
Intake over-limit reading for the dashboard: 0.0
```

There's only one warning line. The intake's `ifPresent` had nothing to run on, so it printed nothing. The intake's `orElse` fell back to `0.0` because its `Optional` was empty.

## What Calling `get()` Blind Would Look Like

Say the `orElse` line were replaced with:

```java
double intakeDashboard = intakeHot.get();
```

This compiles, but `intakeHot` is empty, so the program prints the drivetrain warning and then crashes with `java.util.NoSuchElementException: No value present`. That's the lesson's warning in action: a blind `get()` brings back the exact crash `Optional` was supposed to prevent, just with a different exception name. `orElse` handles the empty case without ever risking it.

## Recap

- A method that might not have a result can return `Optional<T>`, so the possibility is written into its return type.
- `Optional.of(value)` wraps a real, non-null value. `Optional.empty()` means "no value," instead of returning `null`.
- `ifPresent(lambda)` runs code only when a value is there. On an empty `Optional`, it does nothing.
- `orElse(fallback)` always produces a value: the real one if present, the fallback otherwise.
- Calling `get()` on an empty `Optional` throws `NoSuchElementException`. Use `ifPresent`/`orElse` instead.
