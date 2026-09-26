---
outlineRef: "19 — Interfaces as Contracts (ORACLE 15.1-6)"
status: "new — authored lesson (fuller depth than the teaser slide)"
---

# Interfaces as Contracts

## What vs. How

An **interface** defines *what* an object can do, without specifying *how* it does it. It's a "contract" — a set of method signatures any implementing class agrees to provide, with no implementation of its own for those methods (every one of those methods is **abstract**, Lesson 17.5's term for a signature with no body). This matters enormously in real engineering: it lets two groups write code against a shared agreement without either needing to know the other's internals — a hardware vendor and an application team can each build against the same interface independently, as long as both honor it.

```java
public interface IntakeIO
{
    void updateInputs(IntakeInputs inputs);
    void setVoltage(double volts);
}
```

Method signatures inside an interface have no body — just a semicolon, no braces. `interface` is the keyword; a class agrees to the contract with `implements`:

```java
public class RealIntakeIO implements IntakeIO
{
    @Override
    public void updateInputs(IntakeInputs inputs) { /* real sensor reads */ }

    @Override
    public void setVoltage(double volts) { /* real motor.setVoltage(volts) */ }
}
```

A class implementing an interface must provide a real method body for *every* method the interface declares (default and static methods excepted — see below) — or the class fails to compile. Every one of those methods is implicitly `public`, even though `IntakeIO` never writes the word — an implementing method has to be written `public` too, or it doesn't compile: a `private` or package-private `updateInputs` would be *weakening* access the interface already promised as `public`.

## Multiple Interfaces, One Superclass

Unlike `extends` (limited to exactly one superclass — Lesson 17.1), a class can `implements` as many interfaces as it needs:

```java
public class Intake implements Stowable, Diagnosable
{
    // must provide every method declared by BOTH Stowable and Diagnosable
}
```

This is one of the biggest practical differences between inheritance and interfaces: a class has one parent, but can honor any number of separate contracts at once.

## Using an Interface as a Type

Just like a superclass (Lesson 17.3), an interface is a real reference type — a variable, parameter, array, or collection can be declared against an interface type, and hold any object whose class implements it:

```java
public void configureIntake(IntakeIO io)
{
    // works for RealIntakeIO, SimIntakeIO, or any other IntakeIO implementation
    io.setVoltage(0.0);
}
```

Code written against `IntakeIO` never needs to know or care which concrete implementation it's actually working with — real hardware, or a simulated stand-in (this exact pattern is the foundation of the IO-Layer Pattern, Ch.20).

## Interface Constants

A field declared inside an interface is implicitly `public static final` — a shared constant, not per-object state (an interface has no object state of its own; it declares behavior, not fields to hold data):

```java
public interface IntakeIO
{
    // implicitly public static final — same as Lesson 7.4's constants
    double MAX_VOLTS = 12.0;

    void setVoltage(double volts);
}
```

`IntakeIO.MAX_VOLTS` reads it directly off the interface name, exactly like any other `static final` constant (Lesson 7.4).

## One Interface Extending Another

An interface can `extends` another interface — not a class — to build a bigger contract out of a smaller one. Unlike a class, an interface can `extends` more than one interface at once, since there's no object state to conflict:

```java
public interface Diagnosable
{
    String getStatus();
}

public interface LoggingDiagnosable extends Diagnosable
{
    void logStatus(); // LoggingDiagnosable now requires BOTH getStatus() and logStatus()
}
```

A class that `implements LoggingDiagnosable` must provide both methods — the inherited one and the new one.

## Default and Static Methods

Normally every method in an interface is abstract (no body). **Default** and **static** methods are the exceptions. A **default method** provides a real implementation directly inside the interface, marked with the `default` keyword, which implementing classes inherit automatically without being forced to write it themselves. The strongest default methods build on top of the interface's own abstract methods, adding real behavior without weakening the contract:

```java
public interface IntakeIO
{
    void updateInputs(IntakeInputs inputs);
    void setVoltage(double volts);

    default void stop()
    {
        // built on top of the abstract method every implementer must provide
        setVoltage(0.0);
    }
}
```

`updateInputs` and `setVoltage` are still required — every implementing class must provide them, or it won't compile. `stop()` comes for free: it's written once, here, and every `IntakeIO` implementation inherits it automatically, calling that implementation's own `setVoltage`. This matters for a very practical reason: default methods let an interface add new methods later without breaking every class that already implements it — existing implementations simply inherit the default behavior rather than suddenly failing to compile. A class can still override a default method with its own real implementation, exactly like overriding an inherited method from a superclass (Lesson 18.1).

An interface can also declare **static methods** — utility methods associated with the interface itself, not with any implementing object, called directly on the interface name rather than through an instance:

```java
public interface IntakeIO
{
    static double clampVolts(double v)
    {
        return Math.max(-12.0, Math.min(12.0, v));
    }
}
```

`IntakeIO.clampVolts(14.0)` calls it directly on the interface name — no `IntakeIO` object needed, the same way `Math.max(...)` needs no `Math` object.

### When Two Interfaces' Defaults Collide

If a class implements two interfaces that both supply a default method with the same signature, Java can't pick one for you — the class must override that method itself (calling one of them explicitly, e.g. `Stowable.super.stop()`, if that's what's wanted), or it's a compile error. This only comes up with defaults; two abstract methods with the same signature just merge into one requirement.

## Interface or Abstract Class?

Lesson 17.5 introduced abstract classes as the other tool for "some methods without bodies, filled in by subclasses" — and promised this comparison. The short version: reach for an **abstract class** when the related classes share real state and code (fields, constructors, concrete helper methods) — like `RobotPart`'s `name` and `log()`. Reach for an **interface** when classes only need to share a set of methods, with no shared state, and especially when a class needs to honor more than one contract at once (a class can `implements` many interfaces, but `extends` only one class).

| | Abstract class | Interface |
|---|---|---|
| Fields (state) | Yes | Only `public static final` constants |
| Constructors | Yes | No |
| How many can a class have? | One (`extends`) | Any number (`implements`) |
| Method bodies allowed? | Yes, freely | Only `default`/`static` |

## Common Pitfalls

- **Forgetting to implement every abstract method an interface declares.** A class that leaves even one required method unimplemented fails to compile — every non-default, non-static method is a firm requirement.
- **Confusing `extends` and `implements`.** A class `extends` exactly one class, but can `implements` any number of interfaces — these are two entirely separate mechanisms.
- **Assuming every interface method needs to be written from scratch.** Default methods (like `stop()` on `IntakeIO` above) come "for free" — only override one if the default behavior isn't what you want.
- **Writing an implementing method with weaker access than `public`.** Every interface method is implicitly `public`; a `RealIntakeIO.updateInputs` declared without `public` (or as `private`) fails to compile with "attempting to assign weaker access privileges."
- **Making every interface method an empty default "for convenience."** That silently removes the compiler's guarantee that an implementation provides real behavior — a class that forgets to override an empty `default setVoltage(double)` compiles fine and simply never moves the motor. Keep methods abstract unless a default genuinely builds useful shared behavior on top of them.

## Key Takeaways

- An interface is a contract: method signatures with no implementation (default/static methods aside), specifying *what* a class can do, not *how* — every abstract method is implicitly `public`, and every field is implicitly `public static final`.
- A class agrees to an interface's contract with `implements`, and can implement any number of interfaces at once — unlike the single-superclass limit of `extends`. An interface can itself `extends` one or more other interfaces.
- An interface is a real type — variables, parameters, arrays, and collections can all be declared against it, holding any object whose class implements it.
- A `default` method provides a real implementation directly in the interface, letting implementing classes inherit it without writing their own; a `static` method belongs to the interface itself, called on its name. Two colliding defaults force the implementing class to override and resolve them.
- Abstract class vs. interface (Lesson 17.5): shared state and code → abstract class; shared behavior only, or multiple contracts at once → interface.

Derived from `other-reference-repo`: `oracle-java-tutorials/interfaces/01-interfaces.md`, `02-defining-an-interface.md`, `03-implementing-an-interface.md`, `04-using-an-interface-as-a-type.md`, `05-default-methods.md`, `06-summary-of-interfaces.md` (ORACLE 15.1-6)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 6 ("Interfaces as Contracts") — IntakeIO example
