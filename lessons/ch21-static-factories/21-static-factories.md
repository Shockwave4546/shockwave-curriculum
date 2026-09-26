---
outlineRef: "21 — Static Factories (T5817 30.2)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# Static Factories

## Why Not Just `new`?

A **static factory method** is a `public static` method that returns an object, used *instead of* calling a constructor directly. At first glance this looks like extra ceremony for no reason — but it buys a few concrete things a plain constructor can't:

- **A descriptive name.** `MyCommands.print("Ready")` says exactly what you're getting; a constructor overload chosen by argument types alone doesn't communicate intent nearly as clearly.
- **The freedom to not construct a new object at all.** A factory method can return a cached, already-existing instance instead of a fresh one — a constructor, by contrast, always creates something new.
- **The freedom to return a completely different concrete type**, chosen by logic inside the method — the caller only ever sees the return type (often an interface), never which concrete class was actually picked.

```java
public class MyCommands
{
    public static Command print(String msg)
    {
        return Command.noRequirements(coroutine -> System.out.println(msg))
            .named("Print " + msg);
    }
}
```

Calling `MyCommands.print("Ready")` reads clearly as "give me a command that prints this message" — the caller never needs to know or care that it's built from `Command.noRequirements` (Lesson 25.2) underneath.

## A Concrete Example: Returning a Cached Instance

The "freedom to not construct a new object" isn't just theoretical — here it is in practice. A factory method can hand back the *same* object every time instead of building a fresh one:

```java
public class SensorLog
{
    private static final SensorLog INSTANCE = new SensorLog();

    public static SensorLog getInstance()
    {
        return INSTANCE; // the same object every call — never a fresh one
    }
}
```

Every call to `SensorLog.getInstance()` returns the exact same `SensorLog` object. A constructor could never do this — `new SensorLog()` always builds a new one.

## The Real Payoff: Choosing an Implementation by Condition

The pattern's biggest use in FRC code is picking between real and simulated hardware — deciding *which* concrete class to construct, in exactly one place, based on a condition. A factory class like this exists purely to hold `static` members, so it also gets a `private` constructor — nothing outside the class ever needs, or is allowed, to write `new DrivetrainFactory()` (each class below is in its own file):

```java
public interface Drivetrain
{
    void drive(double speed, double turn);
}

public class RealDrivetrain implements Drivetrain
{
    @Override
    public void drive(double speed, double turn)
    {
        // control the real motor controllers
    }
}

public class SimDrivetrain implements Drivetrain
{
    @Override
    public void drive(double speed, double turn)
    {
        // simulate motion via WPILib sim
    }
}

public class DrivetrainFactory
{
    private DrivetrainFactory() {} // never instantiated — only static members

    public static Drivetrain createDrivetrain()
    {
        if (RobotBase.isReal())
        {
            return new RealDrivetrain();
        }
        else
        {
            return new SimDrivetrain();
        }
    }
}
```

```java
// caller never picks the concrete class itself
Drivetrain drivetrain = DrivetrainFactory.createDrivetrain();
```

This is a genuine alternative to the constructor-injection style from the IO-Layer Pattern (Ch.20) — **constructor injection** means the caller decides which implementation to use and passes ("injects") it in through a constructor parameter, the way Ch.20's `Robot` constructor builds `new Intake(new IntakeIOReal())` itself. A factory flips that: instead of the caller deciding, the factory itself makes the real-vs-sim decision, centralizing that one `if (RobotBase.isReal())` check inside `createDrivetrain()` rather than repeating it at every construction site. WPILib's own API uses this pattern too — `Rotation2d.fromDegrees(90)` (Lesson 4.5) is a real static factory, more descriptive than calling `Rotation2d`'s constructor with radians directly.

## Factories for More Than Hardware

The same idea works for building the right object out of a whole family of choices — not just two (real/sim), but any number, selected by some other input. This is a `switch` **expression** (Lesson 5.12) over a `String`:

```java
public class AutoFactory
{
    public static Command createAuto(String mode)
    {
        return switch (mode)
        {
            case "Taxi" -> MyCommands.driveForward(3.0);
            case "2 Ball" -> MyCommands.twoBallAuto();
            case "Nothing" -> Command.waitFor(Seconds.of(0.1)).named("Do Nothing");
            case null, default -> MyCommands.print("Unknown Auto Mode");
        };
    }
}
```

```java
// org.wpilib.tunable — the 2027 driver-station chooser
Selectable<String> chooser = new Selectable<>();
chooser.addDefault("Taxi", "Taxi");

// built from whatever the driver station selected
Command auto = AutoFactory.createAuto(chooser.getSelected());
```

`chooser.getSelected()` can return `null` if nothing was ever selected *and* no default was set with `addDefault(...)` — a plain `default` case doesn't catch `null`, and switching on a `null` String otherwise throws a `NullPointerException`. `case null, default ->` (Java 21+ pattern matching for switch) explicitly routes a `null` mode to the same fallback as any other unrecognized one.

## Common Pitfalls

- **Returning a concrete class instead of an interface.** `public static RealDrivetrain createDrivetrain()` locks callers into one specific implementation — return the interface type (`Drivetrain`) so the real choice stays hidden inside the factory.
- **Duplicating the same real-vs-sim `if` check in multiple places.** The whole point of a factory is centralizing that decision in one method — scattering `RobotBase.isReal()` checks throughout the codebase (instead of injecting once, as Ch.20's `Robot` constructor does, or factoring it into one method here) defeats the purpose.
- **Confusing a factory with a constructor.** A factory method is just a regular `static` method — it can return a cached instance or pick any subtype, neither of which a constructor is free to do (a constructor always returns a new instance of its own exact class). A factory method *can* validate its arguments, but so can a constructor (Lesson 12) — that part isn't a difference between them.

## Key Takeaways

- A static factory method returns an object in place of a direct constructor call, with a descriptive name, the option to return a cached instance (`SensorLog.getInstance()`), and the freedom to choose the actual concrete type internally.
- Its most common FRC use: centralizing real-vs-simulated (or comp-bot-vs-practice-bot) selection logic in one place, so callers only ever depend on an interface. This is an alternative to constructor injection (Ch.20) — the factory decides, instead of the caller.
- Factories generalize beyond hardware — anything selected by a condition (an autonomous mode, a config option) is a natural fit; a `switch` expression choosing between commands needs `case null, default ->` if the input could be `null`.
- Always return the interface type from a factory method, not a specific concrete class, so the actual implementation choice stays hidden from callers. A factory-only class gets a `private` constructor, since nothing should ever build one with `new`.

Derived from `other-reference-repo`: `team-5817-training/design-patterns/factory.md` (T5817 30.2); updated for Commands v3 from allwpilib `main` (`commandsv3/…/command3/Command.java`)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 7 ("Static Factories")
