# New-Content Outline — CSA Topics Not in the Deck

Workspace repo (Repo 3), combining [`mechacoder-test`](../mechacoder-test) (Repo 1, frozen) and
[`csawesome-2026`](../csawesome-2026) (Repo 2, frozen) into new curriculum content. Neither
source repo is modified from here — corrections to captured CSA content happen upstream in
Repo 2, then get pulled forward.

This pass covers only the 42 CSA topics tagged **B** (not in the deck at all) in the original
mapping. It does **not** cover the "full lesson" depth-expansion for the 61 **A**-tagged
(already-in-deck) topics — that's a separate, not-yet-scoped task.

## Placement, not naming

Naming (Java 1a/2a vs. Java III/IV/V vs. something else) is deliberately left open — that's a
UX/manifest decision, not a content-structure one. What's fixed here is **prerequisite
placement**: does a cluster need to come before Java II, does it deepen Java II, or does it
stand on its own? mechadv (the original team) capped things at two Java lessons because they
teach live and a lecturer fills gaps in real time; that constraint doesn't apply to solo
learners here, so there's no reason to force everything back into two lessons.

## Combined Learning Path — v1

One interleaved tree: existing deck topics (Java 1 / Java 2) with new clusters slotted in at
the point they extend or attach to. Section labels (`Bridge`, `Additional Topics`) are
placeholders at "mechacoder level," not final names. CSA's own topic order was set aside to
build this — easy to flip back to CSA order later if needed.

This is v1, expected to change. Neither mechacoder's existing ordering nor CSA's is treated as
fixed — the next pass is refactoring this purely for student learning-progression sense,
possibly drawing on how other Java textbooks/courses sequence these same topics, not just these
two sources. A topic like Strings is a known example of an awkward single-parent fit (it
also belongs with Arrays, not just Variables & Types) — expect more of these to surface.

```
Java 1
  Why Java for FRC?
  Variables & Types
    ↳ [NEW] Expressions, Assignment & Casting        [CSA 1.3,1.4,1.5,1.6]
    ↳ [NEW] Strings                                  [CSA 1.15]
  Storing Data (arrays/collections)
    ↳ [NEW] Arrays & ArrayLists: Traversal Patterns  [CSA 4.4,4.5,4.9,4.10]
    ↳ [NEW] Wrapper Classes & Text Files             [CSA 4.6,4.7]
  Control Structures
    ↳ [NEW] Boolean Logic & Conditional Design       [CSA 2.1,2.2,2.4,2.5,2.6]
    ↳ [NEW] Loops in Depth                           [CSA 2.7,2.9,2.11,2.12]
    ↳ [NEW] String Algorithms                        [CSA 2.10]  (needs Strings + Loops above)
  Reusable Methods
    ↳ [NEW] Class/Instance Methods & the Math Library [CSA 1.10,1.11,1.14]
    ↳ [NEW] Code Documentation & Preconditions        [CSA 1.8]
  The Class Blueprint
  Constructors & "this"
  Enums: Named Choices
  Packages & Imports
  Exceptions & try/catch
  Lambdas & Method References
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
  The IO-Layer Pattern
  Static Factories
    ↳ [NEW] Object References & Static Members       [CSA 3.6,3.7]
  The Builder Pattern
  Encapsulation & Final
  Optional: Maybe a Value
  State Machines: Logic (enum)
  Managing Transitions (switch)
  Event Loops & Triggers
  Architecture Takeaways (DRY/YAGNI/SOLID)

Additional Topics
  ↳ [NEW] 2D Arrays                                    [CSA 4.11,4.12,4.13]
  ↳ [NEW] Algorithms: Searching, Sorting & Recursion   [CSA 4.14,4.15,4.16,4.17]

(dropped) Tier 0 — CSA 1.1, reference CSA site directly
(flagged, not building) Data Ethics & Data Sets — CSA 4.1, 4.2
```

## Original tier/cluster tables (detail behind the tree above)

## Dropped: Tier 0 (CSA 1.1 — Foundations of Programming)

Not building a lesson for this. It's general CS literacy (what's an algorithm, what's a
compiler), not FRC- or Java-specific — CSAwesome2026 itself is the reference for it. Any
student curious about that level can be pointed to the live CSA site directly rather than us
authoring our own version of it.

## Tier 1 — Before Java II (extends/deepens Java I)

| Cluster | CSA topics | Notes |
|---|---|---|
| Expressions, Assignment & Casting | 1.3, 1.4, 1.5, 1.6 | Directly extends Java I's one-slide "Variables & Types." |
| Code Documentation & Preconditions | 1.8 | Small. Could fold into the deck's "General" category instead of "Java." |
| Class Methods, Instance Methods & the Math Library | 1.10, 1.11, 1.14 | Extends Java I's "Methods" slide; 1.9 (Method Signatures) is already A-tagged/covered, so this cluster is the deeper half. |
| Strings | 1.15 | Meaty enough to stand alone. |
| Boolean Logic & Conditional Design | 2.1, 2.2, 2.4, 2.5, 2.6 | Extends Java I's "Control Structures" slide, which never covers boolean expressions in depth or De Morgan's Laws at all. |
| Loops in Depth | 2.7, 2.9, 2.11, 2.12 | While loops, nested loops, runtime analysis — none of this is in the deck currently (it only shows a for-each example). |
| String Algorithms | 2.10 | Depends on both Strings and Loops in Depth — sequence it after both. |
| Arrays & ArrayLists: Traversal & Algorithm Patterns | 4.4, 4.5, 4.9, 4.10 | Deepens the already-covered 4.3/4.8 (which the deck only shows as one-line examples). |
| Wrapper Classes & Text Files | 4.6, 4.7 | Text files has real FRC relevance (config/log files, ties to `DataLogManager` already mentioned in `general-1.js`). |

## Bridge — immediately before Java II

| Cluster | CSA topics | Notes |
|---|---|---|
| Program Design & Abstraction | 3.1, 3.2 | Natural lead-in to Java II's existing "Why Design Patterns?" opening slide — sequence this as the last thing before Java II, not just generically "before it." |

## Tier 2 — After Java II (deepens Java II's OOP/architecture content)

| Cluster | CSA topics | Notes |
|---|---|---|
| Object References & Static Members | 3.6, 3.7 | Deepens Java II's OOP mechanics. Note: 3.7 (static variables/methods) may actually need to land *before* Java II's own "Static Factories" slide specifically, not after the whole lesson — flagging as a within-Java-II sequencing wrinkle, not a clean "after" fit. |
| Inheritance in Depth | 5.2, 5.5, 5.7 | Deepens Java II's existing Inheritance/Polymorphism slides. |
| 2D Arrays | 4.11, 4.12, 4.13 | No deck equivalent at all. Lower FRC priority (robot code rarely uses 2D arrays) — reasonable to place late. |
| Algorithms: Searching, Sorting & Recursion | 4.14, 4.15, 4.16, 4.17 | Classic CS-fundamentals depth, not FRC-specific, valuable as general grounding — after Java II. |

## Flagged — weak fit, reconsider before building

| CSA topics | Why flagged |
|---|---|
| 4.1 (Ethical/Social Issues Around Data), 4.2 (Data Sets) | Generic AP-exam content (data privacy, working with real-world CSV datasets) with no obvious FRC tie-in. Recommend skip, or at most a very light optional mention, rather than a full lesson — don't force every CSA topic into the curriculum just because it exists. |

## Exercise/quiz sizing (proposed, not settled)

One exercise per cluster-lesson, matching the existing "exercise per lesson" cadence — this
naturally gives more, smaller checkpoints than the current deck, which was the original goal.
Rather than a quiz per cluster, propose 2-3 checkpoint quizzes total for all of this: one after
Tier 1 (before Java II), one after the Bridge cluster (right before Java II starts), one after
Tier 2 (after Java II). Matches the "1-2 quizzes for a topic this size" scale mentioned earlier,
and keeps quiz gates meaningful rather than trivial.

## Open questions this outline surfaces (not yet decided)

- Does a single dense CSA topic (e.g. "Boolean Logic & Conditional Design" bundling 5 CSA
  sub-topics) become one lesson or split further? Proposed as one cluster = one lesson here,
  but some clusters are denser than others.
- Final naming/numbering scheme (Java 1a/2a, Java III+, or something else) — open, separate
  decision from this placement outline.
- Should `java-1.js`/`java-2.js` themselves ever be split into finer lessons to match this new
  granularity, or do they stay as the fixed fast-overview tier permanently?

## Provenance convention for this repo

Every new lesson file built from this outline should carry a reference line back to its
sources, e.g.:
```
Derived from csawesome-2026: unit-2-selection-and-iteration/2.02-boolean-expressions.md (CSA 2.2)
Deck context: mechacoder-test/src/lessons/java-1.js ("Control Structures" slide)
```
