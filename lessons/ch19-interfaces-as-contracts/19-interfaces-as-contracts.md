# Interfaces as Contracts

**Outline ref:** 19 — Interfaces as Contracts (ORACLE 15.1-6)
**Status:** new — authored lesson (fuller depth than the teaser slide)

## What vs. How

An **interface** defines *what* an object can do, without specifying *how* it does it. It's a "contract" — a set of method signatures any implementing class agrees to provide, with no implementation of its own for those methods. This matters enormously in real engineering: it lets two groups write code against a shared agreement without either needing to know the other's internals — a hardware vendor and an application team can each build against the same interface independently, as long as both honor it.

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

A class implementing an interface must provide a real method body for *every* method the interface declares (default and static methods excepted — see below) — or the class fails to compile.

## Multiple Interfaces, One Superclass

Unlike `extends` (limited to exactly one superclass — Lesson 17.1), a class can `implements` as many interfaces as it needs:

```java
public class Robot implements Loggable, Sendable
{
    // must provide every method declared by BOTH Loggable and Sendable
}
```

This is one of the biggest practical differences between inheritance and interfaces: a class has one parent, but can honor any number of separate contracts at once.

## Using an Interface as a Type

Just like a superclass (Lesson 17.3), an interface is a real reference type — a variable, parameter, array, or collection can be declared against an interface type, and hold any object whose class implements it:

```java
public void configureIntake(IntakeIO io)
{
    io.setVoltage(0.0); // works for RealIntakeIO, SimIntakeIO, or any other IntakeIO implementation
}
```

Code written against `IntakeIO` never needs to know or care which concrete implementation it's actually working with — real hardware, or a simulated stand-in (this exact pattern is the foundation of the IO-Layer Pattern, Ch.20).

## Default and Static Methods

Normally every method in an interface is abstract (no body). A **default method** is the one exception — it provides a real implementation directly inside the interface, marked with the `default` keyword, which implementing classes inherit automatically without being forced to write it themselves:

```java
public interface IntakeIO
{
    default void updateInputs(IntakeInputs inputs) {}  // default: does nothing unless overridden
    default void setVoltage(double volts) {}           // default: does nothing unless overridden
}
```

This matters for a very practical reason: default methods let an interface add new methods later without breaking every class that already implements it — existing implementations simply inherit the default behavior rather than suddenly failing to compile. A class can still override a default method with its own real implementation, exactly like overriding an inherited method from a superclass (Lesson 18.1).

An interface can also declare **static methods** — utility methods associated with the interface itself, not with any implementing object, called directly on the interface name rather than through an instance.

## Common Pitfalls

- **Forgetting to implement every abstract method an interface declares.** A class that leaves even one required method unimplemented fails to compile — every non-default, non-static method is a firm requirement.
- **Confusing `extends` and `implements`.** A class `extends` exactly one class, but can `implements` any number of interfaces — these are two entirely separate mechanisms.
- **Assuming every interface method needs to be written from scratch.** Default methods (like the empty ones in `IntakeIO` above) come "for free" — only override one if the default behavior isn't what you want.

## Key Takeaways

- An interface is a contract: method signatures with no implementation (default/static methods aside), specifying *what* a class can do, not *how*.
- A class agrees to an interface's contract with `implements`, and can implement any number of interfaces at once — unlike the single-superclass limit of `extends`.
- An interface is a real type — variables, parameters, arrays, and collections can all be declared against it, holding any object whose class implements it.
- A `default` method provides a real implementation directly in the interface, letting implementing classes inherit it without writing their own — the mechanism behind adding new interface methods without breaking existing code.

Derived from `other-reference-repo`: `oracle-java-tutorials/interfaces/01-interfaces.md`, `02-defining-an-interface.md`, `03-implementing-an-interface.md`, `04-using-an-interface-as-a-type.md`, `05-default-methods.md`, `06-summary-of-interfaces.md` (ORACLE 15.1-6)
**Deck context:** mechacoder-test/src/lessons/java-2.js, slide 6 ("Interfaces as Contracts") — IntakeIO example
