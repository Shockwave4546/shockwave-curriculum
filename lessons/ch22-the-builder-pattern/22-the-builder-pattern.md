---
outlineRef: "22 — The Builder Pattern (T5817 30.1)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# The Builder Pattern

## The Problem: "Constructor Hell"

A constructor with many parameters — especially several of the same type, or several optional ones — becomes genuinely hard to read and easy to get wrong:

```java
Shooter shooter = new Shooter(0.01, 0.0, 0.02, true, 5000.0, 1000.0);
```

What does each number actually mean? Swap two arguments of the same type by mistake, and the compiler won't catch it — it'll just silently misconfigure the shooter. This is sometimes called "constructor hell," and it gets worse the more optional settings a class has, since a constructor either forces every caller to specify every parameter, or multiplies into a pile of overloads trying to cover every combination.

## The Builder Pattern: Construct Step by Step

The **Builder Pattern** separates *building* an object from *using* it — a separate `Builder` object collects settings one at a time, through named, chainable methods, then produces the final object only once, via a `build()` call:

```java
Shooter shooter = new Shooter.Builder()
    .setKP(0.01)
    .setKI(0.0)
    .setKD(0.02)
    .enableFeedforward(true)
    .setMaxRPM(5000.0)
    .setMinRPM(1000.0)
    .build();
```

Every call is now self-documenting — `.setKP(0.01)` says exactly what `0.01` means, in a way a bare constructor argument never could.

## Implementing a Builder

The target class (`Shooter`) gets a `private` constructor — callers can no longer construct it directly, only through the builder — plus a `public static` nested `Builder` class that collects the settings:

```java
public class Shooter
{
    private final double kP, kI, kD;
    private final boolean feedforward;
    private final double maxRPM, minRPM;

    private Shooter(Builder builder)
    {
        this.kP = builder.kP;
        this.kI = builder.kI;
        this.kD = builder.kD;
        this.feedforward = builder.feedforward;
        this.maxRPM = builder.maxRPM;
        this.minRPM = builder.minRPM;
    }

    public static class Builder
    {
        private double kP = 0, kI = 0, kD = 0;
        private boolean feedforward = false;
        private double maxRPM = 0, minRPM = 0;

        public Builder setKP(double kP) { this.kP = kP; return this; }
        public Builder setKI(double kI) { this.kI = kI; return this; }
        public Builder setKD(double kD) { this.kD = kD; return this; }
        public Builder enableFeedforward(boolean ff) { feedforward = ff; return this; }
        public Builder setMaxRPM(double max) { this.maxRPM = max; return this; }
        public Builder setMinRPM(double min) { this.minRPM = min; return this; }

        public Shooter build() { return new Shooter(this); }
    }
}
```

`private final double kP, kI, kD;` declares three fields of the same type in one statement, separated by commas (Lesson 2.1). Every field here is also `final` — Lesson 23.1 covers `final` fields, methods, and classes in full.

## Classes Inside Classes: Static Nested Classes

`Builder` is written as `public static class Builder`, declared entirely inside `Shooter`'s own braces — that's a **static nested class**. Its full name is `Shooter.Builder`, which is exactly why building one starts with `new Shooter.Builder()`. The `static` here means what it always means: a `Shooter.Builder` can be created without an existing `Shooter` object around, the same way a `static` method can be called without an existing object.

Nesting one class inside another also grants both classes a special privilege: `Shooter` and `Shooter.Builder` can reach each other's `private` members directly, something no other class could do. That's how the `Shooter` constructor above can read `builder.kP` even though `kP` is `private` inside `Builder` — and how `Builder.build()` can call `Shooter`'s `private` constructor. Code outside both classes still can't touch either one's `private` fields.

(Java also has *non-static* nested classes, called **inner classes**, where every instance is tied to one specific instance of the outer class — the Builder Pattern only ever needs the `static` kind shown here, so that's the only kind this course covers.)

## The Fluent Chain: Why `return this;` Matters

Every `Builder` method ends with `return this;` — returning the same builder object it was just called on. That's exactly what makes chaining possible: each call's result is another `Builder`, ready for the next call in the chain, all the way until `.build()` finally produces the real `Shooter`. This style (a method call chain, each step returning the object it was called on) is called a **fluent interface**.

## Why the Result Is Safer, Not Just Prettier

- Every setting has a readable name at the call site, instead of an anonymous position in an argument list.
- Optional settings simply aren't called, rather than needing a separate constructor overload for every combination.
- The final object (`Shooter`) is typically built as immutable — every field is `final` and set exactly once, inside the private constructor, from the builder's already-finished values.
- `build()` can also validate before constructing the final object — for example, throwing an `IllegalArgumentException` (Ch.12) if `minRPM` ended up greater than `maxRPM` — instead of quietly handing back a nonsensical configuration.

## Real Patterns This Mirrors in WPILib

Several real WPILib classes already use builder-like chaining, even without a nested `Builder` class:

```java
TrajectoryConfig config = new TrajectoryConfig(maxVelocity, maxAccel)
    .setKinematics(driveKinematics)
    .addConstraint(voltageConstraint);
```

Commands v3 (Ch.25) leans on the same idea even harder — building a `Command` is itself a staged builder chain, where each stage only offers the methods legal to call next: `Command.sequence(intake, shoot).named("Auto")` builds a bigger command out of smaller ones, and `Command.requiring(drive, arm).executing(coroutine -> ...).named("Reach and Drive")` is a builder whose required mechanisms are locked in before you can even call `.executing(...)`.

## When Not to Reach for a Builder

A builder is genuine overhead — a whole extra nested class — that only pays for itself once a constructor's parameter list gets long or has several optional pieces. For a class with 2-3 simple, always-required parameters, a plain constructor (or, per Ch.21, a static factory method) is simpler and should be preferred.

## Common Pitfalls

- **Forgetting `return this;` in a builder method.** If the method still returns `Builder`, dropping `return this;` gives a `missing return statement` compile error right there. If its return type was also changed to `void`, the error shows up one call later instead: the next call in the chain fails with `void cannot be dereferenced`, since there's nothing to call it on.
- **Making the target class's constructor `public` alongside the builder.** That defeats the pattern's purpose — callers should only ever construct the object through the builder, which is why the real constructor stays `private`.
- **Reaching for a builder on a simple, 2-3-parameter class.** That's exactly the case the pattern isn't meant for — the extra ceremony isn't worth it there.

## Key Takeaways

- The Builder Pattern separates step-by-step construction from a class's actual usage, avoiding "constructor hell" (many same-typed or optional parameters).
- A builder is a nested `static` class collecting settings via named, chainable methods (each returning `this` — a fluent interface), finishing with `build()`.
- The target class's real constructor is `private`, taking the finished builder and copying its values into `final` fields — producing an immutable, safely-configured result.
- Real WPILib classes (`TrajectoryConfig`) and Commands v3's staged builders (Ch.25) already use this same chaining idea.
- Skip the builder for simple classes with few, always-required parameters — a constructor or static factory (Ch.21) is simpler there.

Derived from `other-reference-repo`: `team-5817-training/design-patterns/builder.md` (T5817 30.1)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 8 ("The Builder Pattern") — MotorConfig fluent-builder example
