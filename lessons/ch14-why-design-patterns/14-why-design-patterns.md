# Why Design Patterns?

**Outline ref:** 14 — Why Design Patterns? (no citation — deck-original content)
**Status:** new — authored lesson (fuller depth than the teaser slide)

## What This Chapter Starts

Everything up to Ch.13 was single-class, mostly single-file Java: variables, control flow, arrays, one class with a few methods. From here on ("Java II"), the curriculum shifts to how *multiple* classes work together as a codebase grows — the concerns become organization, reuse, and change over time, not just "does this one method work."

A **design pattern** is a named, reusable solution to a problem that keeps showing up across different programs — not a specific piece of code to copy-paste, but a *shape* of solution (which classes exist, how they relate) that's been proven to work well for that kind of problem. The chapters that follow each cover one real pattern actually used in FRC codebases: the Builder Pattern, Static Factories, the IO-Layer Pattern, and eventually the biggest one, Command-Based Programming itself.

> "Code is read much more often than it is written." — Guido van Rossum (adapted)

That quote is the real motivation for this whole unit. A robot's codebase gets read by every teammate who touches it, every mentor reviewing it, and by *you* again in six months — far more often than it gets freshly written. Patterns exist because they make code easier to read and change later, not just easier to write once.

## Why Bother

**Scalability.** A single `Robot.java` file with everything crammed inside works fine for a "blink an LED" program. It stops working once a robot has a drivetrain, an intake, a shooter, vision processing, and autonomous routines all interacting — patterns are how experienced teams keep that complexity organized instead of it collapsing into an unmaintainable mess.

**A common language.** Telling another mentor "I'm using a Factory here" or "this is a Builder" communicates an entire shape of design in a few words — they immediately know how the pieces relate, without you having to walk through every class. Patterns are shared vocabulary across the whole FRC (and broader software) community, not something invented per-team.

**Testability.** Code built around patterns tends to be more **decoupled** — pieces don't reach directly into each other's internals, so they can be swapped, simulated, or tested independently. A drivetrain built with a clean pattern can be tested in simulation, with no real motors or robot required; one where every class directly depends on every other class often can't be tested at all without the physical hardware present.

## What This Chapter Is Not

This chapter doesn't teach a specific pattern — the chapters immediately following it do that one at a time. Its only job is to answer "why does any of this matter," before the actual mechanics of Advanced Collections, Generics, Inheritance, and the named patterns begin.

## Common Pitfalls

- **Reaching for a pattern before there's a real problem it solves.** Patterns exist to manage genuine complexity — forcing one onto a two-class program just because "patterns are good practice" usually adds complexity instead of removing it.
- **Treating pattern names as a vocabulary test rather than a design tool.** The value of saying "this is a Factory" is that it communicates real structure to a teammate — not that it sounds impressive.

## Key Takeaways

- A design pattern is a reusable *shape* of solution to a recurring design problem, not a snippet of code to copy.
- Patterns matter for three concrete reasons: keeping a growing codebase organized (scalability), giving the team shared vocabulary (common language), and making code easier to test in isolation (decoupling).
- The chapters that follow each teach one specific, real pattern used in actual FRC codebases.

Derived from `mechacoder-test`: `src/lessons/java-2.js`, slide 1 ("Why Design Patterns?") — original deck content, no external citation
