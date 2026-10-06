---
outlineRef: "26 — Architecture Takeaways (DRY/YAGNI/SOLID) (no citation — deck-original content; neither WPILib nor T5817 teach these as named general principles)"
pairsWith: "[`lessons/ch26-architecture-takeaways/26-architecture-takeaways.md`](../../lessons/ch26-architecture-takeaways/26-architecture-takeaways.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
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

## Coding

**Mode:** full-program

**Problem:** Apply three principles from the lesson (DRY, Interface Segregation, Dependency Inversion) to one small intake design. `Roller` and `Feeder` are given;
they implement an interface called `Throttled` that **you** write. You also write the remaining pieces:

- `IntakeConstants` holds one constant, `public static final double ROLLER_SPEED = 0.8` (**DRY**: the number lives in one place).
- `Throttled` declares `void setThrottle(double speed)` and `double getThrottle()`.
- `Rotatable` is a **separate** small interface declaring `void setAngle(double degrees)` and `double getAngle()`
  (**Interface Segregation**: `Roller` and `Feeder` can't rotate, so they must not be forced to implement it).
- `Pivot` can do both: it implements `Throttled` **and** `Rotatable`, keeping its own throttle and angle (both start at `0.0`).
- `IntakeController` gets its device through its constructor as a `Throttled`, never a concrete class (**Dependency Inversion**).
  `run()` sets the device's throttle to `IntakeConstants.ROLLER_SPEED`; `stop()` sets it to `0.0`.

`main` reads a device name (`roller`, `feeder`, or anything else for a pivot) and an angle.

**Starter:**

```java
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        String kind = in.next();
        double angle = in.nextDouble();

        Throttled device;
        if (kind.equals("roller"))
        {
            device = new Roller();
        }
        else if (kind.equals("feeder"))
        {
            device = new Feeder();
        }
        else
        {
            device = new Pivot();
        }

        IntakeController controller = new IntakeController(device);
        controller.run();
        System.out.println(kind + " throttle: " + device.getThrottle());
        controller.stop();
        System.out.println(kind + " after stop: " + device.getThrottle());

        if (device instanceof Rotatable rotatable)
        {
            rotatable.setAngle(angle);
            System.out.println(kind + " angle: " + rotatable.getAngle());
        }
        else
        {
            System.out.println(kind + " can't rotate");
        }
        System.out.println("Roller speed constant: " + IntakeConstants.ROLLER_SPEED);
    }
}

class Roller implements Throttled
{
    private double throttle = 0.0;

    public void setThrottle(double speed)
    {
        throttle = speed;
    }

    public double getThrottle()
    {
        return throttle;
    }
}

class Feeder implements Throttled
{
    private double throttle = 0.0;

    public void setThrottle(double speed)
    {
        throttle = speed;
    }

    public double getThrottle()
    {
        return throttle;
    }
}

// TODO: write IntakeConstants

// TODO: write the interfaces Throttled and Rotatable

// TODO: write the class Pivot

// TODO: write the class IntakeController
```

**Scenario 1 (visible):**

**Input:**

```text
roller 30.0
```

**Expected output:**

```text
roller throttle: 0.8
roller after stop: 0.0
roller can't rotate
Roller speed constant: 0.8
```

**Scenario 2 (visible):**

**Input:**

```text
pivot 45.5
```

**Expected output:**

```text
pivot throttle: 0.8
pivot after stop: 0.0
pivot angle: 45.5
Roller speed constant: 0.8
```

**Scenario 3 (visible):**

**Input:**

```text
feeder 0.0
```

**Expected output:**

```text
feeder throttle: 0.8
feeder after stop: 0.0
feeder can't rotate
Roller speed constant: 0.8
```

**Scenario 4 (hidden):**

**Input:**

```text
pivot -90.0
```

**Expected output:**

```text
pivot throttle: 0.8
pivot after stop: 0.0
pivot angle: -90.0
Roller speed constant: 0.8
```

**Scenario 5 (hidden):**

**Input:**

```text
turret 180.0
```

**Expected output:**

```text
turret throttle: 0.8
turret after stop: 0.0
turret angle: 180.0
Roller speed constant: 0.8
```

**Scenario 6 (hidden):**

**Input:**

```text
feeder 12.0
```

**Expected output:**

```text
feeder throttle: 0.8
feeder after stop: 0.0
feeder can't rotate
Roller speed constant: 0.8
```

**Solution:**

```java
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        String kind = in.next();
        double angle = in.nextDouble();

        Throttled device;
        if (kind.equals("roller"))
        {
            device = new Roller();
        }
        else if (kind.equals("feeder"))
        {
            device = new Feeder();
        }
        else
        {
            device = new Pivot();
        }

        IntakeController controller = new IntakeController(device);
        controller.run();
        System.out.println(kind + " throttle: " + device.getThrottle());
        controller.stop();
        System.out.println(kind + " after stop: " + device.getThrottle());

        if (device instanceof Rotatable rotatable)
        {
            rotatable.setAngle(angle);
            System.out.println(kind + " angle: " + rotatable.getAngle());
        }
        else
        {
            System.out.println(kind + " can't rotate");
        }
        System.out.println("Roller speed constant: " + IntakeConstants.ROLLER_SPEED);
    }
}

class Roller implements Throttled
{
    private double throttle = 0.0;

    public void setThrottle(double speed)
    {
        throttle = speed;
    }

    public double getThrottle()
    {
        return throttle;
    }
}

class Feeder implements Throttled
{
    private double throttle = 0.0;

    public void setThrottle(double speed)
    {
        throttle = speed;
    }

    public double getThrottle()
    {
        return throttle;
    }
}

class IntakeConstants
{
    public static final double ROLLER_SPEED = 0.8;
}

interface Throttled
{
    void setThrottle(double speed);

    double getThrottle();
}

interface Rotatable
{
    void setAngle(double degrees);

    double getAngle();
}

class Pivot implements Throttled, Rotatable
{
    private double throttle = 0.0;
    private double angle = 0.0;

    public void setThrottle(double speed)
    {
        throttle = speed;
    }

    public double getThrottle()
    {
        return throttle;
    }

    public void setAngle(double degrees)
    {
        angle = degrees;
    }

    public double getAngle()
    {
        return angle;
    }
}

class IntakeController
{
    private final Throttled device;

    public IntakeController(Throttled device)
    {
        this.device = device;
    }

    public void run()
    {
        device.setThrottle(IntakeConstants.ROLLER_SPEED);
    }

    public void stop()
    {
        device.setThrottle(0.0);
    }
}
```

**Why:** Because `main` gives the controller a `Roller`, a `Feeder` or a `Pivot`, `IntakeController` has to accept the interface `Throttled`; a controller that declares `Roller` (or builds its own with `new Roller()`) can't
drive the others and stops matching the scenarios. `Throttled` and `Rotatable` are kept apart so a `Roller` only promises what it can do. If `Rotatable`'s methods were squeezed into `Throttled`, `Roller` and `Feeder` would
have to supply a fake `setAngle`, and `main`'s `instanceof Rotatable` check would no longer tell a pivot from a roller. The `0.8` appears exactly once, in `IntakeConstants`, which is what DRY asks for.
