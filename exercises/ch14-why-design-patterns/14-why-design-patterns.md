---
outlineRef: "14 — Why Design Patterns? (no citation — deck-original content)"
pairsWith: "[`lessons/ch14-why-design-patterns/14-why-design-patterns.md`](../../lessons/ch14-why-design-patterns/14-why-design-patterns.md)"
status: "new — authored exercises (Multiple Choice only — concept-only lesson, no code to reorder)"
---

# Why Design Patterns? — Exercises

## Multiple Choice

**Question:** A mentor reviewing your team's code says: "Because the intake code doesn't reach directly into the drivetrain's internals, we can swap in a simulated intake and test it on a laptop, with no robot on the table." Which benefit of design patterns is the mentor describing?

**Options:**

- A. Scalability — keeping a growing codebase organized
- B. A common language — shared vocabulary for describing a design
- C. Testability — decoupled pieces can be simulated or tested independently
- D. Speed — code built around patterns runs faster on the roboRIO

**Answer:** C

**Why:** The key words are "doesn't reach directly into ... internals" and "test it ... with no robot." That's decoupling, and the benefit it buys is testability. Each piece can be swapped out, simulated, or tested on its own, without the physical hardware.

- A is wrong because scalability is about keeping a codebase organized as more subsystems get added. The mentor's point is about testing one piece in isolation, not about organizing a growing robot program.
- B is wrong because a common language is about saying "this is a Builder" and having a teammate instantly understand the design. Nothing here involves naming a pattern to communicate with someone.
- D is wrong because the lesson never says patterns make code run faster. Their benefits are about reading, changing, and testing code, not how fast it executes.
