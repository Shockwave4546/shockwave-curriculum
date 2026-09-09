# New-Content Outline — Combined Learning Path

Workspace repo (Repo 3), combining [`mechacoder-test`](../mechacoder-test) (Repo 1, frozen) and
[`csawesome-2026`](../csawesome-2026) (Repo 2, frozen) into new curriculum content. Neither
source repo is modified from here — corrections to captured CSA content happen upstream in
Repo 2, then get pulled forward.

Covers the CSA topics not in the deck at all, plus flags where existing "already covered"
(A-tagged) deck slides are thin and need real depth from their matching CSA content later (a
separate, not-yet-scoped authoring task — this outline just identifies where).

## Placement, not naming

Naming (Java 1a/2a vs. Java III/IV/V vs. something else) is deliberately left open. mechadv
capped things at two Java lessons because they teach live and a lecturer fills gaps in real
time; that constraint doesn't apply to solo learners here.

## Combined Learning Path — v3

```
Java 1
  Why Java for FRC?
  Variables & Types
    ↳ [NEW] Expressions, Assignment & Casting        [CSA 1.3,1.4,1.5,1.6]
  [NEW] APIs, Libraries & Documentation              [CSA 1.7,1.8]
  [NEW] Using Objects & Calling Methods              [CSA 1.10,1.11,1.12,1.13,1.14]
  Control Structures
    ↳ [NEW] Boolean Logic & Conditional Design       [CSA 2.1,2.2,2.4,2.5,2.6]
    ↳ [NEW] Loops in Depth                           [CSA 2.7,2.9,2.11,2.12]
  The Class Blueprint    ← absorbs "Reusable Methods" (dropped, see below); deepened later by CSA 3.5
  Constructors & "this"
    ↳ [NEW] Object References & Static Members       [CSA 3.6,3.7]
  [NEW] Strings                                      [CSA 1.15]
    ↳ [NEW] String Algorithms                        [CSA 2.10]
  Storing Data (arrays/collections)
    ↳ [NEW] Arrays & ArrayLists: Traversal Patterns  [CSA 4.4,4.5,4.9,4.10]
    ↳ [NEW] Wrapper Classes & Text Files             [CSA 4.6,4.7]
    ↳ [TENTATIVE, unconfirmed] 2D Arrays / Algorithms [CSA 4.11-4.17]
  Enums: Named Choices              ⚠ needs external source (see below)
  Packages & Imports                (FRC-flavored quick example; kept alongside the new APIs/Libraries cluster, not redundant with it)
  Exceptions & try/catch             ⚠ mechanism needs external source (see below)
  Common Gotchas
  How to Practice

Bridge
  ↳ [NEW] Program Design & Abstraction              [CSA 3.1,3.2]

Java 2
  Why Design Patterns?
  Advanced Collections (Set/Queue/Map)
  Writing Your Own Generics
  Inheritance & Abstractions
    ↳ [NEW] Inheritance in Depth                     [CSA 5.2,5.5,5.7]
  Polymorphism: Many Forms
  Interfaces as Contracts
    ↳ Lambdas & Method References    ← MOVED here from Java 1  ⚠ needs external source (see below)
  The IO-Layer Pattern
  Static Factories
  The Builder Pattern
  Encapsulation & Final
  Optional: Maybe a Value
  State Machines: Logic (enum)
  Managing Transitions (switch)
  Event Loops & Triggers
  Architecture Takeaways (DRY/YAGNI/SOLID)

Additional Topics
  (empty pending 2D Arrays/Algorithms placement decision)
```

## Dropped from the deck, absorbed elsewhere

- **Reusable Methods** — was a thin, 3-bullet "statement of facts" slide, not real lesson depth.
  Folded into "The Class Blueprint" (a method doesn't exist outside a class anyway; CSA's own
  3.3→3.4→3.5 sequence treats class-anatomy and method-writing as one unit). Real depth comes
  from CSA 3.5 "Methods: How to Write Them" whenever the A-topic depth-expansion pass happens.

## Needs an external source — CSA doesn't (fully) cover these

| Topic | What CSA actually has |
|---|---|
| Enums | Zero mentions anywhere in the captured content. Not on the AP exam at all. |
| Exceptions & try/catch — the **mechanism** | CSA teaches exception *concepts* substantively but scattered across many lessons (`ArithmeticException`, `IndexOutOfBoundsException`, `NullPointerException` all come up naturally — no new cluster needed for that, it'll thread through the other lessons as written). But CSA explicitly excludes `try`/`catch` itself: *"This method uses a try catch block for error-checking which is not covered in the AP exam"* (its own words, from the Consumer Review Lab). |
| Lambdas & Method References | Zero CSA coverage (not on the AP exam; Java 8+ feature outside its scope). Moved to Java 2, after "Interfaces as Contracts," since a lambda is really shorthand for a functional interface — teaching it before interfaces exist (its old Java 1 spot) had no real grounding. |

All three: user is finding book/reference material for these separately — not CSA's job.

## Flagged from CSA — weak fit, reconsider before building

| CSA topics | Why flagged |
|---|---|
| 4.1 (Ethical/Social Issues Around Data), 4.2 (Data Sets) | Generic AP-exam content with no obvious FRC tie-in. Recommend skip. |

## Exercise/quiz sizing (proposed, not settled)

One exercise per cluster-lesson. 2-3 checkpoint quizzes total across all of this (end of the
Java-1-side new clusters, end of Bridge, end of Java-2-side/Additional Topics) rather than one
per cluster.

## Open questions (not yet decided)

- 2D Arrays / Algorithms (Searching, Sorting, Recursion): fold into Java 1 (right after Storing
  Data) for CS-progression soundness, or keep deferred to "Additional Topics" after Java 2 for
  FRC-relevance-first pacing? Still the user's call.
- Final naming/numbering scheme (Java 1a/2a, Java III+, or something else).
- Should `java-1.js`/`java-2.js` themselves ever be split into finer lessons to match this new
  granularity, or stay as the fixed fast-overview tier permanently?

## Provenance convention for this repo

Every new lesson file built from this outline should carry a reference line back to its
sources, e.g.:
```
Derived from csawesome-2026: unit-2-selection-and-iteration/2.02-boolean-expressions.md (CSA 2.2)
Deck context: mechacoder-test/src/lessons/java-1.js ("Control Structures" slide)
```
