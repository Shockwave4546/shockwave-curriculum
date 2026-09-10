# Enums: Named Choices

**Outline ref:** 11 — Enums: Named Choices (ORACLE 10.1)
**Status:** new — authored lesson (fuller depth than the teaser slide)

## Why Enums Exist

An **enum** ("enumerated type") is a type with a fixed, predefined set of named values — a variable of that type can only ever be one of those values, nothing else. Before enums, code often used plain integers or strings to represent a fixed set of states (`int armState = 2;`), which lets any number in — including ones that mean nothing. An enum makes invalid states impossible to even compile:

```java
public enum ArmPosition
{
    STOWED, INTAKE, SCORE
}

ArmPosition target = ArmPosition.INTAKE; // legal
ArmPosition target = ArmPosition.CLIMB;  // compile error — CLIMB was never defined
```

By convention, enum constants are written in `SCREAMING_SNAKE_CASE`, the same naming style used for other constants (Lesson 1.2).

## Switching Over an Enum

A `switch` over an enum reads close to plain English, and (with modern arrow-style `case`) needs no `break`:

```java
switch (target)
{
    case STOWED -> arm.setAngle(0);
    case INTAKE -> arm.setAngle(35);
    case SCORE  -> arm.setAngle(110);
}
```

Notice the case labels are just `STOWED`, not `ArmPosition.STOWED` — inside a switch over an enum, Java already knows the type, so the prefix would be redundant (and doesn't compile).

## An Enum Is Really a Class

An enum isn't just a fancier set of named integers — it's a full class. Its body can declare fields, a constructor, and methods, letting each constant carry its own data:

```java
public enum ArmPosition
{
    STOWED(0), INTAKE(35), SCORE(110); // constants, WITH constructor arguments

    private final double angleDegrees;

    ArmPosition(double angleDegrees)
    {
        this.angleDegrees = angleDegrees;
    }

    public double getAngleDegrees()
    {
        return angleDegrees;
    }
}
```

Two rules this pattern depends on: the list of constants must come **first** in the enum body, and once there are fields or methods after it, that constant list must end with a semicolon. Each constant listed (`STOWED(0)`, `INTAKE(35)`, `SCORE(110)`) calls the constructor with its own arguments — an enum's constructor is implicitly `private`, since you're never allowed to write `new ArmPosition(...)` yourself; the only `ArmPosition` objects that will ever exist are the ones listed in the enum body.

With this version, the earlier switch could be simplified — every position now carries its own target angle:

```java
arm.setAngle(target.getAngleDegrees());
```

## Iterating Every Value: `values()`

Every enum automatically gets a static `values()` method, returning an array of all its constants in declared order — handy for looping over every possibility:

```java
for (ArmPosition position : ArmPosition.values())
{
    System.out.println(position + " -> " + position.getAngleDegrees() + " degrees");
}
```

## What Enums Can't Do

Every enum implicitly extends `java.lang.Enum` behind the scenes. Since Java only allows extending one parent class, an enum can never `extends` anything else of its own — though it can still `implement` interfaces.

## Looking Ahead

This chapter's ideas — a fixed set of named states, plus a `switch` that reacts to whichever one is currently active — are exactly the foundation the **State Machine** pattern (Java II) builds on, where a subsystem tracks "which named state am I in right now" and transitions between them over time.

## Common Pitfalls

- **Writing the enum type prefix inside a `switch`.** `case ArmPosition.INTAKE ->` doesn't compile inside a switch over an `ArmPosition` — just `case INTAKE ->`.
- **Forgetting the semicolon after the constant list once fields/methods follow.** `STOWED(0), INTAKE(35), SCORE(110)` with no trailing `;` before `private final double angleDegrees;` fails to compile.
- **Trying to `new` an enum constant.** `new ArmPosition(...)` is illegal — the only instances that will ever exist are the constants declared in the enum body itself.

## Key Takeaways

- An enum defines a fixed, named set of legal values for a type — the compiler rejects anything not in that list.
- Enum constant names use `SCREAMING_SNAKE_CASE`; a `switch` over an enum omits the type prefix on each `case`.
- An enum is a real class — it can have its own fields, a constructor, and methods, letting each constant carry its own data.
- `EnumType.values()` returns every constant, in order, for looping.
- An enum implicitly extends `java.lang.Enum`, so it can't extend any other class (interfaces are still fine).

Derived from `other-reference-repo`: `oracle-java-tutorials/enums/enum-types.md` (ORACLE 10.1)
**Deck context:** mechacoder-test/src/lessons/java-1.js, slide 9 ("Enums: Named Choices")
