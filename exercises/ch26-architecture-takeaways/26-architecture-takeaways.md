---
outlineRef: "26 — Architecture Takeaways (DRY/YAGNI/SOLID) (no citation — deck-original content; neither WPILib nor T5817 teach these as named general principles)"
pairsWith: "[`lessons/ch26-architecture-takeaways/26-architecture-takeaways.md`](../../lessons/ch26-architecture-takeaways/26-architecture-takeaways.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
---

# Architecture Takeaways — Exercises

## Multiple Choice

**Question:** A team's `Elevator` mechanism class moves the elevator motor to a target height — and it also reads the driver's joystick buttons and decides which autonomous routine to run at the start of a match. Which SOLID principle does this design most directly violate?

**Options:**

- A. Single Responsibility
- B. Open/Closed
- C. Liskov Substitution
- D. Dependency Inversion

**Answer:** A

**Why:** Single Responsibility says a class should have one, and only one, reason to change. This `Elevator` has at least three: a change to the elevator hardware, a change to the button layout, and a change to the autonomous plan would all force edits to the same class. A mechanism's only job should be its own piece of hardware.

- B is wrong — Open/Closed is about adding new behavior without editing code that already works (like adding a new IO implementation without touching the mechanism). Nothing here describes extending the class; the problem is how many unrelated jobs it already has.
- C is wrong — Liskov Substitution is about a subclass being usable anywhere its superclass is expected. No subclass or substitution is involved in this description at all.
- D is wrong — Dependency Inversion is about depending on interfaces rather than concrete implementations. The description doesn't say anything about what types `Elevator` depends on; its problem is doing too many different jobs.

## Micro-Parsons

**Problem:** These lines, once correctly ordered, form a complete program that prints the controller rumble strength for the driver first, then for the operator — with the strength defined once, as a single named constant, instead of repeating the same number in both places. Declare the constant field before `main`.

Reorder the fragments below into a working program:

- a. `        System.out.println("Operator rumble: " + RUMBLE_STRENGTH);`
- b. `    {`
- c. `public class RumbleAlert`
- d. `}`
- e. `    public static final double RUMBLE_STRENGTH = 0.7;`
- f. `        System.out.println("Driver rumble: " + RUMBLE_STRENGTH);`
- g. `{`
- h. `    public static void main(String[] args)`
- i. `    }`

**Answer:** c, g, e, h, b, f, a, i, d

```java
public class RumbleAlert
{
    public static final double RUMBLE_STRENGTH = 0.7;

    public static void main(String[] args)
    {
        System.out.println("Driver rumble: " + RUMBLE_STRENGTH);
        System.out.println("Operator rumble: " + RUMBLE_STRENGTH);
    }
}
```

**Why this order:** The class line (`c`) comes first, with its opening brace (`g`) right after. The constant (`e`) is declared at the class level, not inside `main` — a `public static final` field belongs to the class itself, and that's what makes it the single source of truth both `println` lines can read. `main` (`h`) and its opening brace (`b`) come next. The driver's line (`f`) goes before the operator's line (`a`) because the Problem asks for the driver's value to print first — both read the same `RUMBLE_STRENGTH`, so changing the strength later means editing only `e`, never either `println`. Then the braces close in reverse order: `main`'s body (`i`), then the class's body (`d`).
