---
outlineRef: "22 — The Builder Pattern (T5817 30.1)"
pairsWith: "[`lessons/ch22-the-builder-pattern/22-the-builder-pattern.md`](../../lessons/ch22-the-builder-pattern/22-the-builder-pattern.md)"
status: "new — authored exercises (Multiple Choice + Micro-Parsons + Coding)"
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

## Coding

**Mode:** full-program

**Problem:** Write the class `MotorConfig` using the Builder Pattern.

- `MotorConfig` has a **`private` constructor** that takes a `Builder`, and `private final` fields for `kP`, `maxRPM`, `minRPM` and
  `feedforward`. It has getters `double getKP()`, `double getMaxRPM()`, `double getMinRPM()` and `boolean isFeedforward()`.
- It contains a `public static class Builder` with chainable setters `setKP(double)`, `setMaxRPM(double)`, `setMinRPM(double)` and
  `enableFeedforward(boolean)`. Each returns the same builder. Every setting starts at `0` (feedforward starts as `false`).
- `Builder.build()` returns the new `MotorConfig`, **but** if `minRPM` is greater than `maxRPM` it throws an
  `IllegalArgumentException` with the message `min RPM is above max RPM` instead. Equal values are allowed.

`main` reads the settings (the word `yes` turns feedforward on; any other word leaves the default) and prints the result, or `Invalid: ` plus the exception message.

**Starter:**

```java
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        double kP = in.nextDouble();
        double maxRpm = in.nextDouble();
        double minRpm = in.nextDouble();
        String feedforward = in.next();
        try
        {
            MotorConfig.Builder builder = new MotorConfig.Builder()
                .setKP(kP)
                .setMaxRPM(maxRpm)
                .setMinRPM(minRpm);
            if (feedforward.equals("yes"))
            {
                builder.enableFeedforward(true);
            }
            MotorConfig config = builder.build();
            System.out.println("kP: " + config.getKP());
            System.out.println("RPM range: " + config.getMinRPM() + " to " + config.getMaxRPM());
            System.out.println("Feedforward: " + config.isFeedforward());
        }
        catch (IllegalArgumentException e)
        {
            System.out.println("Invalid: " + e.getMessage());
        }
    }
}

// TODO: write the class MotorConfig, with its nested Builder
```

**Scenario 1 (visible):**

**Input:**

```text
0.01 5000.0 1000.0 yes
```

**Expected output:**

```text
kP: 0.01
RPM range: 1000.0 to 5000.0
Feedforward: true
```

**Scenario 2 (visible):**

**Input:**

```text
0.5 300.0 -300.0 no
```

**Expected output:**

```text
kP: 0.5
RPM range: -300.0 to 300.0
Feedforward: false
```

**Scenario 3 (visible):**

**Input:**

```text
0.02 100.0 200.0 no
```

**Expected output:**

```text
Invalid: min RPM is above max RPM
```

**Scenario 4 (hidden):**

**Input:**

```text
0.25 1500.0 1500.0 no
```

**Expected output:**

```text
kP: 0.25
RPM range: 1500.0 to 1500.0
Feedforward: false
```

**Scenario 5 (hidden):**

**Input:**

```text
1.5 6000.0 0.0 yes
```

**Expected output:**

```text
kP: 1.5
RPM range: 0.0 to 6000.0
Feedforward: true
```

**Scenario 6 (hidden):**

**Input:**

```text
0.1 -50.0 -10.0 yes
```

**Expected output:**

```text
Invalid: min RPM is above max RPM
```

**Solution:**

```java
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) // Don't change main
    {
        Scanner in = new Scanner(System.in);
        double kP = in.nextDouble();
        double maxRpm = in.nextDouble();
        double minRpm = in.nextDouble();
        String feedforward = in.next();
        try
        {
            MotorConfig.Builder builder = new MotorConfig.Builder()
                .setKP(kP)
                .setMaxRPM(maxRpm)
                .setMinRPM(minRpm);
            if (feedforward.equals("yes"))
            {
                builder.enableFeedforward(true);
            }
            MotorConfig config = builder.build();
            System.out.println("kP: " + config.getKP());
            System.out.println("RPM range: " + config.getMinRPM() + " to " + config.getMaxRPM());
            System.out.println("Feedforward: " + config.isFeedforward());
        }
        catch (IllegalArgumentException e)
        {
            System.out.println("Invalid: " + e.getMessage());
        }
    }
}

class MotorConfig
{
    private final double kP;
    private final double maxRPM;
    private final double minRPM;
    private final boolean feedforward;

    private MotorConfig(Builder builder)
    {
        this.kP = builder.kP;
        this.maxRPM = builder.maxRPM;
        this.minRPM = builder.minRPM;
        this.feedforward = builder.feedforward;
    }

    public double getKP()
    {
        return kP;
    }

    public double getMaxRPM()
    {
        return maxRPM;
    }

    public double getMinRPM()
    {
        return minRPM;
    }

    public boolean isFeedforward()
    {
        return feedforward;
    }

    public static class Builder
    {
        private double kP = 0;
        private double maxRPM = 0;
        private double minRPM = 0;
        private boolean feedforward = false;

        public Builder setKP(double kP)
        {
            this.kP = kP;
            return this;
        }

        public Builder setMaxRPM(double max)
        {
            this.maxRPM = max;
            return this;
        }

        public Builder setMinRPM(double min)
        {
            this.minRPM = min;
            return this;
        }

        public Builder enableFeedforward(boolean ff)
        {
            this.feedforward = ff;
            return this;
        }

        public MotorConfig build()
        {
            if (minRPM > maxRPM)
            {
                throw new IllegalArgumentException("min RPM is above max RPM");
            }
            return new MotorConfig(this);
        }
    }
}
```

**Why:** Each setter ends with `return this;`, which is what lets `main` chain them, and the target class's constructor is `private` so the only way in is through `build()`. The
`MotorConfig` constructor copies the builder's finished values into `final` fields. Because `build()` is the one place the object is created, it is also the place to validate. The
hidden scenarios catch two common mistakes: no validation at all (the `min > max` case builds a nonsense config), and a `>=` check that wrongly rejects `min == max`.
A builder that forgets to copy a field into the constructor shows up as `0.0` values in the output.
