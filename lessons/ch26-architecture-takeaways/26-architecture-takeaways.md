# Architecture Takeaways

**Outline ref:** 26 — Architecture Takeaways (DRY/YAGNI/SOLID) (no citation — deck-original content; neither WPILib nor T5817 teach these as named general principles)
**Status:** new — authored lesson (fuller depth than the teaser slide)

Java II opened (Ch.14) with why patterns matter at all. This closing chapter names the general software-engineering principles that everything since — inheritance, interfaces, the IO-Layer Pattern, factories, builders, command-based itself — has actually been demonstrating in FRC-specific form. These aren't FRC-specific or Java-specific ideas; they're widely known across the software industry, which is exactly why they're worth naming explicitly.

## DRY: Don't Repeat Yourself

If the same logic (or the same literal value) appears in more than one place, a future change has to remember to update every copy — and it's easy to miss one. The fix is almost always one of the tools this curriculum already covered: pull shared behavior into a common superclass (Ch.17), a shared utility method, or a single `Constants` class (Ch.25.7) instead of copy-pasting a magic number into five different files.

```java
// NOT DRY — the same speed value is hardcoded in three places
intakeMotor.set(0.8);
indexerMotor.set(0.8);
feederMotor.set(0.8);

// DRY — one named constant, one place to change it
intakeMotor.set(IntakeConstants.kRollerSpeed);
indexerMotor.set(IntakeConstants.kRollerSpeed);
feederMotor.set(IntakeConstants.kRollerSpeed);
```

## YAGNI: You Ain't Gonna Need It

Don't build flexibility or abstraction for a requirement that doesn't exist yet — every layer of abstraction (a `Builder`, Ch.22; a generic type, Ch.16; an extra interface) has a real cost in complexity, and that cost is only worth paying once the actual need shows up. A `Builder` for a 2-parameter class, or a factory (Ch.21) that only ever returns one concrete implementation, is YAGNI in practice: solving a problem the code doesn't actually have yet, at the expense of a codebase that's harder to read today for a payoff that may never arrive.

## SOLID: Five Principles, One Letter Each

SOLID isn't a single idea — it's an acronym for five distinct principles, each addressing a different way a class or module's design can go wrong. All five show up somewhere in this curriculum already, even though they weren't named until now:

**S — Single Responsibility.** A class should have one, and only one, reason to change. A `Subsystem` (Ch.20/25) that only manages one piece of hardware is a direct application of this — its only job is that hardware, not also handling button bindings or autonomous logic.

**O — Open/Closed.** A module should be open for extension, but closed for modification — you should be able to add new behavior without editing code that already works. The IO-Layer Pattern (Ch.20) is a textbook example: adding a brand-new `IntakeIOSim` implementation never requires touching `Intake`'s own logic, since both implementations honor the same `IntakeIO` contract.

**L — Liskov Substitution.** A subclass should be usable anywhere its superclass is expected, without breaking anything. This is exactly the is-a substitution test from Ch.17.1 — if substituting a subclass object somewhere a superclass is expected changes the correctness of the code, the inheritance relationship was wrong to begin with.

**I — Interface Segregation.** Don't force a class to implement methods it doesn't actually need, just because they're bundled into one large interface. Several small, focused interfaces (each describing one real capability) are preferable to one bloated interface everything is forced to implement in full.

**D — Dependency Inversion.** Code should depend on abstractions (interfaces), not concrete implementations. Every constructor that accepts an `IntakeIO` instead of hardcoding `new IntakeIOSparkMax()` directly (Ch.20/21), and every static factory returning an interface type rather than a specific class (Ch.21), is dependency inversion in action.

## Why Name These at All

None of DRY, YAGNI, or SOLID are FRC-specific or even Java-specific — they're widely-used vocabulary across the whole software industry, which is exactly the "common language" benefit Ch.14 opened with. Being able to say "this violates single responsibility" or "that's YAGNI" communicates a specific, well-understood critique in a few words, to any programmer familiar with these terms — not just people who've read this particular curriculum.

## Common Pitfalls

- **Applying DRY so aggressively that unrelated code gets forced together.** Two pieces of code that happen to look similar today, but for unrelated reasons, don't necessarily belong in one shared abstraction — premature DRY-ing can create awkward, tangled dependencies between things that should stay separate.
- **Treating YAGNI as an excuse to never plan ahead.** YAGNI argues against building unneeded flexibility *now* — it doesn't mean ignoring architecture altogether; the IO-Layer Pattern (Ch.20) is worth its overhead in FRC precisely because simulation and hardware-swapping are real, common needs, not speculative ones.
- **Only remembering the "S" of SOLID.** The deck's own shorthand ("one class, one responsibility") is genuinely just Single Responsibility — SOLID names four more distinct principles beyond that one.

## Key Takeaways

- DRY: don't duplicate logic or values — a single source of truth (a constant, a shared method, a superclass) means one place to fix or change something.
- YAGNI: don't build abstraction or flexibility for a need that doesn't exist yet — every layer of indirection has a real cost, worth paying only once it's actually needed.
- SOLID is five separate principles — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion — each already demonstrated somewhere in this curriculum's FRC examples.
- These principles are industry-standard vocabulary, not FRC- or Java-specific — naming them precisely is itself a form of the "common language" benefit patterns provide (Ch.14).

Derived from `mechacoder-test`: `src/lessons/java-2.js`, slide 13 ("Architecture Takeaways") — original deck content, expanded here since SOLID is a real five-principle acronym the original slide only partially named
