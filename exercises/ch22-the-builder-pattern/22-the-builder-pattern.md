---
outlineRef: "22 — The Builder Pattern (T5817 30.1)"
pairsWith: "[`lessons/ch22-the-builder-pattern/22-the-builder-pattern.md`](../../lessons/ch22-the-builder-pattern/22-the-builder-pattern.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons)"
---

# The Builder Pattern — Exercises

## Multiple Choice

**Question:** An `IntakeConfig.Builder` has this method:

```java
public void setRollerSpeed(double speed) { this.rollerSpeed = speed; }
```

Every other builder method correctly returns `Builder` and ends in `return this;`. What happens with this code?

```java
IntakeConfig config = new IntakeConfig.Builder()
    .setRollerSpeed(0.8)
    .setReversed(true)
    .build();
```

**Options:**

- A. It doesn't compile, because `.setReversed(true)` is being called on the result of a `void` method
- B. It compiles and runs, but `rollerSpeed` keeps its default value
- C. It compiles and runs, but `setReversed(true)` is silently skipped
- D. It compiles, but throws a `NullPointerException` when it runs

**Answer:** A

**Why:** A fluent chain only works because each call returns an object for the next call to be made on. `setRollerSpeed` returns `void`, so there's nothing for `.setReversed(true)` to be called on, and the compiler rejects the chain.

- B is wrong. The problem isn't the value being assigned (`this.rollerSpeed = speed;` is fine). The program never compiles, so nothing runs at all.
- C is wrong. Java never silently skips a call in a chain. A call on `void` is a compile error, not a no-op.
- D is wrong. This is caught at compile time, before the program can run. A `void` return isn't a `null` reference that fails later.

## Micro-Parsons

**Problem:** You're given everything in the program below except the body of `main`: the `ArmSetup` class (with `main`'s signature and braces, placed first so the file also runs correctly on Java 17 — the class holding `main` has to come first in a multi-class file), and the `ArmConfig` class, with its `private` constructor and nested `Builder`. Reorder the fragments below into the body of `main`. It should use the builder to set the arm's maximum angle to `110.0`, turn brake mode on, and set the gear ratio to `50.0`, then print the finished configuration: `max 110.0 deg, brake true, ratio 50.0:1`.

Reorder the fragments below to complete it:

- a. `            .setGearRatio(50.0)`
- b. `        System.out.println(config.describe());`
- c. `        ArmConfig config = new ArmConfig.Builder()`
- d. `            .build();`
- e. `            .setMaxAngle(110.0)`
- f. `            .setBrakeMode(true)`

**Answer:** c, e, f, a, d, b

**Interchangeable:** (e, f, a)

```java
public class ArmSetup
{
    public static void main(String[] args)
    {
        ArmConfig config = new ArmConfig.Builder()
            .setMaxAngle(110.0)
            .setBrakeMode(true)
            .setGearRatio(50.0)
            .build();
        System.out.println(config.describe());
    }
}

class ArmConfig
{
    private final double maxAngle;
    private final boolean brakeMode;
    private final double gearRatio;

    private ArmConfig(Builder builder)
    {
        this.maxAngle = builder.maxAngle;
        this.brakeMode = builder.brakeMode;
        this.gearRatio = builder.gearRatio;
    }

    public String describe()
    {
        return "max " + maxAngle + " deg, brake " + brakeMode + ", ratio " + gearRatio + ":1";
    }

    public static class Builder
    {
        private double maxAngle = 90.0;
        private boolean brakeMode = false;
        private double gearRatio = 1.0;

        public Builder setMaxAngle(double maxAngle) { this.maxAngle = maxAngle; return this; }
        public Builder setBrakeMode(boolean brakeMode) { this.brakeMode = brakeMode; return this; }
        public Builder setGearRatio(double gearRatio) { this.gearRatio = gearRatio; return this; }

        public ArmConfig build() { return new ArmConfig(this); }
    }
}
```

**Why this order:** The chain has to start with the line that creates the builder (`c`). Every other call in the chain is made on the object it produces. The three setters (`e`, `f`, `a`) each set a different, independent field and each return the same builder, so they can go in any order (hence **Interchangeable:** (e, f, a)). `.build();` (`d`) has to come last in the chain. It's the call that turns the builder into the real `ArmConfig`, and it's the only fragment with the semicolon that ends the statement. After it, nothing else can chain on as a builder call. `println` (`b`) comes last, since `config` only exists once the whole chain has finished.
