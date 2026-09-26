---
outlineRef: "11 — Enums: Named Choices (ORACLE 10.1)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# Enums: Named Choices

## Why Enums Exist

An **enum** ("enumerated type") is a type with a fixed, predefined set of named values — a variable of that type can only ever be one of those values, nothing else. Before enums, code often used plain integers or strings to represent a fixed set of states (`int armState = 2;`), which lets any number in — including ones that mean nothing. An enum makes invalid states impossible to even compile:

```java
public enum ArmPosition
{
    STOWED, INTAKE, SCORE
}

ArmPosition target = ArmPosition.INTAKE; // legal
ArmPosition target2 = ArmPosition.CLIMB; // compile error — CLIMB was never defined
```

By convention, enum constants are written in `SCREAMING_SNAKE_CASE`, the same naming style used for other constants (Lesson 1.2).

## Switching Over an Enum

Lesson 5.12 covers `switch` itself — arrow form, colon form, `break`, and switch expressions. Enums are where `switch` is most at home, because the compiler already knows every possible value:

```java
switch (target)
{
    case STOWED -> arm.setAngle(0);
    case INTAKE -> arm.setAngle(35);
    case SCORE  -> arm.setAngle(110);
}
```

Notice the case labels are just `STOWED`, not `ArmPosition.STOWED` — inside a switch over an `ArmPosition`, Java already knows the type, so the prefix is optional and redundant; leave it off. (On Java 17–20, writing the qualified `ArmPosition.STOWED` form is a compile error; Java 21+ allows it but this course still leaves it off for readability.)

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

Two rules this pattern depends on: the list of constants must come **first** in the enum body, and once there are fields or methods after it, that constant list must end with a semicolon. Each constant listed (`STOWED(0)`, `INTAKE(35)`, `SCORE(110)`) calls the constructor with its own arguments — an enum's constructor is implicitly `private`, since you're never allowed to write `new ArmPosition(...)` yourself; the only `ArmPosition` objects that will ever exist are the ones listed in the enum body. Writing `public` (or `protected`) on an enum constructor is a compile error ("modifier public not allowed here") — leave the modifier off entirely.

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

## Built-In Methods Every Enum Gets

Besides `values()`, every enum constant automatically has a few more methods, inherited from `java.lang.Enum` (inheritance and `extends` are covered in Ch.17; interfaces and `implements` in Ch.19 — you don't need those chapters to use these methods):

```java
ArmPosition p = ArmPosition.INTAKE;
System.out.println(p.name());     // "INTAKE" — the constant's exact declared name
System.out.println(p.ordinal());  // 1 — its position in the declared order, 0-indexed
System.out.println(p);            // "INTAKE" — toString() defaults to name()
// text -> constant; throws IllegalArgumentException if no match
ArmPosition parsed = ArmPosition.valueOf("SCORE");
```

Comparing two enum values with `==` is safe and preferred (unlike `String`, where `==` is a pitfall) — there is only ever one object per constant, so `==` and `.equals()` always agree. An enum variable can still be `null` (it's a reference type), so a `switch` or `==` check on an unassigned enum variable can still throw or misbehave like any other `null` reference.

## What Enums Can't Do

Every enum implicitly extends `java.lang.Enum` behind the scenes. Since Java only allows extending one parent class, an enum can never `extends` anything else of its own (Ch.17 covers `extends` in full) — though it can still `implement` interfaces (Ch.19).

## Looking Ahead

This chapter's ideas — a fixed set of named states, plus a `switch` that reacts to whichever one is currently active — are exactly the foundation the **State Machine** pattern (Java II) builds on, where a subsystem tracks "which named state am I in right now" and transitions between them over time.

## Common Pitfalls

- **Writing the enum type prefix inside a `switch`.** `case ArmPosition.INTAKE ->` is optional and redundant — just `case INTAKE ->`. (On Java 17–20 the qualified form is a compile error.)
- **Forgetting the semicolon after the constant list once fields/methods follow.** `STOWED(0), INTAKE(35), SCORE(110)` with no trailing `;` before `private final double angleDegrees;` fails to compile.
- **Trying to `new` an enum constant.** `new ArmPosition(...)` is illegal — the only instances that will ever exist are the constants declared in the enum body itself.

## Key Takeaways

- An enum defines a fixed, named set of legal values for a type — the compiler rejects anything not in that list.
- Enum constant names use `SCREAMING_SNAKE_CASE`; a `switch` over an enum omits the type prefix on each `case`.
- An enum is a real class — it can have its own fields, a constructor, and methods, letting each constant carry its own data.
- `EnumType.values()` returns every constant, in order, for looping; `name()`, `ordinal()`, `toString()`, and `valueOf(String)` are also built in.
- `==` is safe (and preferred) for comparing enum values — unlike `String`. An enum variable can still be `null`.
- An enum implicitly extends `java.lang.Enum`, so it can't extend any other class (interfaces are still fine).

Derived from `other-reference-repo`: `oracle-java-tutorials/enums/enum-types.md` (ORACLE 10.1)
**Deck context:** mechacoder-test/src/lessons/java-1.js, slide 9 ("Enums: Named Choices")
