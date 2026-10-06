---
outlineRef: "11 — Enums: Named Choices (ORACLE 10.1)"
pairsWith: "[`lessons/ch11-enums-named-choices/11-enums-named-choices.md`](../../lessons/ch11-enums-named-choices/11-enums-named-choices.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
---

# Enums: Named Choices — Exercises

## Multiple Choice

**Question:** This enum is meant to store how far the climber extends for each position, but it doesn't compile. Why?

```java
public enum ClimberHeight
{
    RETRACTED(0.0), LOW_RUNG(18.0), HIGH_RUNG(31.5)

    private final double inches;

    ClimberHeight(double inches)
    {
        this.inches = inches;
    }

    public double getInches()
    {
        return inches;
    }
}
```

**Options:**

- A. The constant list needs a semicolon after `HIGH_RUNG(31.5)`, because a field and methods follow it
- B. Enum constant names have to be lowercase, like `lowRung`
- C. An enum can't have a constructor. Only regular classes can
- D. The constructor needs the `public` keyword so the constants can call it

**Answer:** A

**Why:** Once an enum body has fields or methods after its constant list, the list has to end with `;`. Without it, the compiler reads `private final double inches;` as if it were still part of the constant list and fails. Adding the semicolon (`HIGH_RUNG(31.5);`) fixes it.

- B is wrong. `SCREAMING_SNAKE_CASE` is the naming convention for enum constants, and lowercase names would still compile. Either way, the names aren't what breaks this code.
- C is wrong. An enum is a full class, so it can have fields, a constructor, and methods. That's exactly how each constant carries its own height here.
- D is wrong. An enum's constructor is implicitly `private`, because only the constants listed in the enum body are ever allowed to call it. Writing `public` on it actually causes a compile error of its own.

## Micro-Parsons

**Problem:** These lines, once correctly ordered, form a complete program. It defines a `DriveMode` enum with two modes, `PRECISION` and `TURBO`, and uses a `switch` to print the top speed for the current mode. To keep it to one runnable file, `main` goes inside the enum itself. That's legal because an enum is a class. Note that `main` counts as a method here, so the semicolon rule for the constant list applies.

Reorder the fragments below into a working program:

- a. `        DriveMode mode = DriveMode.PRECISION;`
- b. `public enum DriveMode`
- c. `        }`
- d. `            case PRECISION -> System.out.println("Max speed: 30%");`
- e. `    public static void main(String[] args)`
- f. `}`
- g. `        switch (mode)`
- h. `{`
- i. `            case TURBO     -> System.out.println("Max speed: 100%");`
- j. `    {`
- k. `    PRECISION, TURBO;`
- l. `    }`
- m. `        {`

**Answer:** b, h, k, e, j, a, g, m, d, i, c, l, f

**Interchangeable:** (d, i)

```java
public enum DriveMode
{
    PRECISION, TURBO;

    public static void main(String[] args)
    {
        DriveMode mode = DriveMode.PRECISION;
        switch (mode)
        {
            case PRECISION -> System.out.println("Max speed: 30%");
            case TURBO     -> System.out.println("Max speed: 100%");
        }
    }
}
```

Output: `Max speed: 30%`

**Why this order:** The enum's name (`b`) and opening brace (`h`) come first. The constant list (`k`) must be the first thing in the enum body, and it ends with `;` because a method (`main`) follows it. `main`'s signature (`e`) and opening brace (`j`) come next. Inside `main`, the variable (`a`) has to exist before the `switch` (`g`) can check it. The switch's opening brace (`m`) comes next, then its two `case` lines (`d`, `i`). Those two can go in either order: an arrow-style `case` never falls through, so only the matching case runs no matter where it sits. The case labels are bare names (`PRECISION`, not `DriveMode.PRECISION`). The braces then close in the reverse order they opened: the switch (`c`), then `main` (`l`), then the enum (`f`).

## Coding

**Mode:** harness

**Problem:** The arm's named positions are an enum whose constants each carry a target angle in
degrees. The starter lists the constants with their angles, but the enum is missing the pieces that
make those arguments legal. Finish the `ArmPosition` enum, then write `totalTravel`, which takes the
**names** of the positions the arm visits, in order, and returns the total number of degrees the arm
moves. The arm always starts at `STOWED`. Each move costs the **absolute difference** between the
two angles. An empty route costs `0`. Every name in the route is a valid `ArmPosition` name.

Add to the enum a `private final int` field for the angle, a constructor that sets it, and a getter
(for example `getAngleDegrees()`).

Examples (angles: `STOWED` 0, `INTAKE` 35, `SCORE` 110, `CLIMB` 60):

- `totalTravel(new String[] {"INTAKE", "SCORE"})` returns `110` (`0 -> 35 -> 110` is `35 + 75`)
- `totalTravel(new String[] {"INTAKE"})` returns `35`
- `totalTravel(new String[] {})` returns `0`

**Signature:** `public static int totalTravel(String[] route)`

**Starter:**

```java
public class Solution
{
    public enum ArmPosition
    {
        STOWED(0), INTAKE(35), SCORE(110), CLIMB(60);

        // TODO: add the field, constructor, and getter
    }

    public static int totalTravel(String[] route)
    {
        // TODO: turn each name into an ArmPosition and add up the moves
    }
}
```

**Tests:**

| Visible | Arguments | Expected |
|---|---|---|
| yes | `new String[] {"INTAKE", "SCORE"}` | `110` |
| yes | `new String[] {"INTAKE"}` | `35` |
| yes | `new String[] {}` | `0` |
| no | `new String[] {"SCORE", "STOWED"}` | `220` |
| no | `new String[] {"CLIMB", "INTAKE", "CLIMB"}` | `110` |
| no | `new String[] {"STOWED", "STOWED"}` | `0` |
| no | `new String[] {"SCORE", "INTAKE", "STOWED"}` | `220` |

**Solution:**

```java
public class Solution
{
    public enum ArmPosition
    {
        STOWED(0), INTAKE(35), SCORE(110), CLIMB(60);

        private final int angleDegrees;

        ArmPosition(int angleDegrees)
        {
            this.angleDegrees = angleDegrees;
        }

        public int getAngleDegrees()
        {
            return angleDegrees;
        }
    }

    public static int totalTravel(String[] route)
    {
        int total = 0;
        ArmPosition current = ArmPosition.STOWED;
        for (String name : route)
        {
            ArmPosition next = ArmPosition.valueOf(name);
            total = total + Math.abs(next.getAngleDegrees() - current.getAngleDegrees());
            current = next;
        }
        return total;
    }
}
```

**Why:** An enum is a real class: once the constants carry arguments, the body needs a field, a
constructor that stores it (no `public`, since an enum constructor is implicitly private), and a
getter. `valueOf(String)` turns each name into the matching constant. The loop remembers where the
arm currently is, starting at `STOWED`, and adds the distance to the next position. Without
`Math.abs`, a move down (like `SCORE` to `STOWED`) would subtract instead of add, which is why the
hidden tests include routes that go back down.
