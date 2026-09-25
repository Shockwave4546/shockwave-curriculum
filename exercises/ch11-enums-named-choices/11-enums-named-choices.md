---
outlineRef: "11 — Enums: Named Choices (ORACLE 10.1)"
pairsWith: "[`lessons/ch11-enums-named-choices/11-enums-named-choices.md`](../../lessons/ch11-enums-named-choices/11-enums-named-choices.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
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
