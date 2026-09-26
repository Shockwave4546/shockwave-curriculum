---
outlineRef: "19 — Interfaces as Contracts (ORACLE 15.1-6)"
pairsWith: "[`lessons/ch19-interfaces-as-contracts/19-interfaces-as-contracts.md`](../../lessons/ch19-interfaces-as-contracts/19-interfaces-as-contracts.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
---

# Interfaces as Contracts — Exercises

## Multiple Choice

**Question:** Given these two interfaces and one class:

```java
interface Aimable
{
    void aimAt(double degrees);
}

interface Reportable
{
    String getReport();

    default void printReport()
    {
        System.out.println(getReport());
    }
}

class Turret implements Aimable, Reportable
{
    private double angle;

    @Override
    public void aimAt(double degrees)
    {
        angle = degrees;
    }

    @Override
    public String getReport()
    {
        return "Turret at " + angle + " degrees";
    }
}
```

`Turret` never writes a `printReport()` method. What happens?

**Options:**

- A. It doesn't compile — `Turret` is missing `printReport()`, which `Reportable` declares
- B. It doesn't compile — a class can only implement one interface
- C. It compiles, and `Turret` inherits `printReport()` from `Reportable`'s default method
- D. It compiles, but calling `printReport()` on a `Turret` crashes at runtime because `Turret` never wrote it

**Answer:** C

**Why:** `Turret` implements both interfaces, and it provides a body for every abstract method they declare: `aimAt(double)` from `Aimable` and `getReport()` from `Reportable`. `printReport()` isn't abstract — it's a `default` method with its own body inside `Reportable` — so `Turret` inherits it automatically and doesn't have to write it.

- A is wrong — only abstract (no-body) methods are required. A `default` method already has a body, so implementing classes get it for free.
- B is wrong — that's the rule for `extends` (exactly one superclass). A class can `implements` as many interfaces as it needs, comma-separated.
- D is wrong — the inherited default is a real method with a real body. Calling it on a `Turret` would print that turret's report, e.g. `Turret at 30.0 degrees` after `aimAt(30.0)`.

## Micro-Parsons

**Problem:** Given this `Scorer` interface and `main` method, reorder the fragments below into the `SpeakerShot` class that goes where the comment is. `SpeakerShot` must implement the `Scorer` contract, returning `2` points, so the program prints `Points: 2`.

```java
public class ScoreTest
{
    public static void main(String[] args)
    {
        Scorer shot = new SpeakerShot();
        System.out.println("Points: " + shot.getPoints());
    }
}

interface Scorer
{
    int getPoints();
}

// SpeakerShot class goes here
```

(`ScoreTest`, the public class with `main`, comes first in the file — on Java 17, `java File.java` source-launch only runs the first class in the file; Java 25 is more lenient, but leading with the public class works on both.)

Reorder the fragments below to complete it:

- a. `    {`
- b. `class SpeakerShot implements Scorer`
- c. `    }`
- d. `        return 2;`
- e. `}`
- f. `    public int getPoints()`
- g. `{`
- h. `    @Override`

**Answer:** b, g, h, f, a, d, c, e

```java
public class ScoreTest
{
    public static void main(String[] args)
    {
        Scorer shot = new SpeakerShot();
        System.out.println("Points: " + shot.getPoints());
    }
}

interface Scorer
{
    int getPoints();
}

class SpeakerShot implements Scorer
{
    @Override
    public int getPoints()
    {
        return 2;
    }
}
```

**Why this order:** The class declaration (`b`) comes first — `implements Scorer` is what signs the contract, and it's also what lets `main` store a `SpeakerShot` in a `Scorer`-typed variable. The class's opening brace (`g`) follows. `@Override` (`h`) goes directly above the method signature (`f`), which has to match the interface's `int getPoints()` — without this method, `SpeakerShot` would be missing a required part of the contract and wouldn't compile. The method's opening brace (`a`), its `return` statement (`d`), and its closing brace (`c`) follow, and the class's closing brace (`e`) comes last. `ScoreTest` and the `Scorer` interface are the given scaffold, with `SpeakerShot` inserted where the comment was.
