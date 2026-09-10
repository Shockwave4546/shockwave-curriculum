# Static Factories

**Outline ref:** 21 — Static Factories (T5817 30.2)
**Status:** new — authored lesson (fuller depth than the teaser slide)

## Why Not Just `new`?

A **static factory method** is a `public static` method that returns an object, used *instead of* calling a constructor directly. At first glance this looks like extra ceremony for no reason — but it buys a few concrete things a plain constructor can't:

- **A descriptive name.** `Command.printMessage("Ready")` says exactly what you're getting; `new PrintCommand("Ready")` (or worse, a constructor overload chosen by argument types alone) doesn't communicate intent nearly as clearly.
- **The freedom to not construct a new object at all.** A factory method can return a cached, already-existing instance instead of a fresh one — a constructor, by contrast, always creates something new.
- **The freedom to return a completely different concrete type**, chosen by logic inside the method — the caller only ever sees the return type (often an interface), never which concrete class was actually picked.

```java
public static Command printMessage(String msg)
{
    return new InstantCommand(() -> System.out.println(msg));
}
```

Calling `printMessage("Ready")` reads clearly as "give me a command that prints this message" — the caller never needs to know or care that it's actually an `InstantCommand` wrapping a lambda underneath.

## The Real Payoff: Choosing an Implementation by Condition

The pattern's biggest use in FRC code is picking between real and simulated hardware — deciding *which* concrete class to construct, in exactly one place, based on a condition:

```java
public interface Drivetrain
{
    void drive(double speed, double turn);
}

public class RealDrivetrain implements Drivetrain
{
    public void drive(double speed, double turn) { /* control real Talons/Sparks */ }
}

public class SimDrivetrain implements Drivetrain
{
    public void drive(double speed, double turn) { /* simulate motion via WPILib sim */ }
}

public class DrivetrainFactory
{
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
Drivetrain drivetrain = DrivetrainFactory.createDrivetrain(); // caller never picks the concrete class itself
```

This is a genuine alternative to the constructor-injection style from the IO-Layer Pattern (Ch.20) — instead of the caller deciding which `IntakeIO` to pass in, the factory itself makes that decision, centralizing the real-vs-sim logic in one place instead of duplicating an `if (isReal())` check everywhere a subsystem gets built.

## Factories for More Than Hardware

The same idea works for building the right object out of a whole family of choices — not just two (real/sim), but any number, selected by some other input:

```java
public class AutoFactory
{
    public static Command createAuto(String mode)
    {
        return switch (mode)
        {
            case "Taxi" -> new DriveForwardCommand(3.0);
            case "2 Ball" -> new TwoBallAutoCommand();
            case "Nothing" -> new WaitCommand(0.1);
            default -> new PrintCommand("Unknown Auto Mode");
        };
    }
}
```

```java
Command auto = AutoFactory.createAuto(chooser.getSelected()); // built from whatever the driver station selected
```

## Common Pitfalls

- **Returning a concrete class instead of an interface.** `public static RealDrivetrain createDrivetrain()` locks callers into one specific implementation — return the interface type (`Drivetrain`) so the real choice stays hidden inside the factory.
- **Duplicating the same real-vs-sim `if` check in multiple places.** The whole point of a factory is centralizing that decision in one method — scattering `RobotBase.isReal()` checks throughout the codebase defeats the purpose.
- **Confusing a factory with a constructor.** A factory method is just a regular `static` method — it can validate arguments, return a cached instance, or pick any subtype, none of which a constructor is free to do (a constructor always returns a new instance of its own exact class).

## Key Takeaways

- A static factory method returns an object in place of a direct constructor call, with a descriptive name, the option to return a cached instance, and the freedom to choose the actual concrete type internally.
- Its most common FRC use: centralizing real-vs-simulated (or comp-bot-vs-practice-bot) selection logic in one place, so callers only ever depend on an interface.
- Factories generalize beyond hardware — anything selected by a condition (an autonomous mode, a config option) is a natural fit.
- Always return the interface type from a factory method, not a specific concrete class, so the actual implementation choice stays hidden from callers.

Derived from `other-reference-repo`: `team-5817-training/design-patterns/factory.md` (T5817 30.2)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 7 ("Static Factories")
