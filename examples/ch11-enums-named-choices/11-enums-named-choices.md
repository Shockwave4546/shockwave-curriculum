---
outlineRef: "11 — Enums: Named Choices (ORACLE 10.1)"
pairsWith: "[`lessons/ch11-enums-named-choices/11-enums-named-choices.md`](../../lessons/ch11-enums-named-choices/11-enums-named-choices.md)"
status: "new — authored worked example (fully solved, walked step by step — not a problem to attempt)"
---

# Enums: Named Choices — Worked Example

## Problem

The intake on this year's robot only ever does one of three things: it's off, it's pulling a game piece in, or it's spitting one back out. Represent those three modes so that no other mode can ever be typed by mistake, print a message for whichever mode is active, then give each mode its own motor power and print every mode's power in a list.

## Step 1: Plan It First

1. Define a type whose only legal values are the three intake modes.
2. React to the current mode with a `switch`.
3. Let each mode carry its own motor power (a field, a constructor, and a getter).
4. Loop over every mode with `values()` to print them all.

## Step 2: Define the Enum

Using an `int` (`0` = off, `1` = intake, `2` = eject) would let any number in, including `7`, which means nothing. An enum only allows the values it lists. It goes in its own file, `IntakeMode.java`:

```java
public enum IntakeMode
{
    OFF, INTAKE, EJECT
}
```

Any other name is rejected before the program ever runs:

```java
IntakeMode mode = IntakeMode.EJECT; // legal
IntakeMode mode2 = IntakeMode.SHOOT; // compile error — SHOOT was never defined
```

The constants are written in `SCREAMING_SNAKE_CASE`, the same style as other constants.

## Step 3: React to the Current Mode With a `switch`

In a separate file, `IntakeDemo.java` (both files in the same folder; `java IntakeDemo.java` runs multi-file source directly on JDK 22+ — on Java 17, compile both with `javac IntakeDemo.java IntakeMode.java` first, then `java IntakeDemo`):

```java
public class IntakeDemo
{
    public static void main(String[] args)
    {
        IntakeMode mode = IntakeMode.EJECT;

        switch (mode)
        {
            case OFF    -> System.out.println("Rollers stopped");
            case INTAKE -> System.out.println("Pulling a game piece in");
            case EJECT  -> System.out.println("Spitting a game piece out");
        }
    }
}
```

Output:

```
Spitting a game piece out
```

Each `case` label is the bare constant name (`EJECT`), with no `IntakeMode.` in front: the switch already knows it's switching over an `IntakeMode`. The arrow-style `case` needs no `break`, and only the matching case runs.

## Step 4: Give Each Mode Its Own Motor Power

Every mode needs a motor power: `0.0` for off, `0.8` to pull in, `-0.5` to push out. An enum is a real class, so it can hold that number itself. Here's `IntakeMode.java` rewritten:

```java
public enum IntakeMode
{
    OFF(0.0), INTAKE(0.8), EJECT(-0.5);

    private final double motorPower;

    IntakeMode(double motorPower)
    {
        this.motorPower = motorPower;
    }

    public double getMotorPower()
    {
        return motorPower;
    }
}
```

Three things to check against the lesson's rules:

- The constant list comes **first** in the body.
- Because a field and methods follow it, the list ends with a **semicolon** after `EJECT(-0.5)`.
- Each constant's parentheses (`INTAKE(0.8)`) call the constructor with that constant's own value. The constructor is implicitly `private`, so nobody can write `new IntakeMode(...)`. `OFF`, `INTAKE`, and `EJECT` are the only three `IntakeMode` objects that will ever exist.

Code that used to need a `switch` to pick a power can now just ask the mode:

```java
IntakeMode mode = IntakeMode.EJECT;
System.out.println("Setting intake power to " + mode.getMotorPower());
```

```
Setting intake power to -0.5
```

## Step 5: Print Every Mode With `values()`

`IntakeMode.values()` returns an array of all three constants in the order they were declared, so a for-each loop covers every mode without listing them by hand:

```java
for (IntakeMode m : IntakeMode.values())
{
    System.out.println(m + " -> " + m.getMotorPower() + " power");
}
```

```
OFF -> 0.0 power
INTAKE -> 0.8 power
EJECT -> -0.5 power
```

Printing `m` on its own gives the constant's name (`OFF`, `INTAKE`, `EJECT`). If a fourth mode gets added to the enum later, this loop picks it up with no changes.

## Recap

- An enum lists every legal value of a type. Anything else fails to compile.
- A `switch` over an enum uses bare constant names in each `case`.
- An enum is a class: constants can pass arguments to a constructor, which stores them in fields that methods then return.
- Once fields or methods follow the constant list, the list must end with `;`.
- `EnumType.values()` returns every constant in declared order, which makes looping over all of them easy.
