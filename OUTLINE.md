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

## Combined Learning Path — v6

**This file is the source of truth.** Also viewable as a formatted page — the "Curriculum
Ledger" artifact (https://claude.ai/code/artifact/b33b0cff-ce35-4977-bddc-14f50d1a1b27), same
content as below with dots for existing/new, easier to scan. Sync flows one way: edit here
first, then mirror the change into the Ledger artifact (chapter/item text, dots, chip status).
**Any edit to this section without a matching Ledger update leaves the Ledger stale** — this
already happened once (the whole Oracle-capture status went unsynced for a while). Update both
in the same pass, don't defer the Ledger sync to "later."

**Numbering rule**: every chapter number is a pure organizational label — it never carries a
CSA reference itself. Every actual piece of content (existing or new) is a numbered item
underneath its chapter, even when there's only one. "Item" is a placeholder term, not "lesson"
— that already means something specific in mechacoder's own code (`registerLesson()`). Chapter
numbers here are sequence-order placeholders, not a proposed final naming scheme.

```
JAVA 1
1   Why Java for FRC?                                          [existing]
2   Variables & Types                                          [header]
    2.1 Variables and Data Types                    CSA 1.2     [existing]
    2.2 Expressions and Output                      CSA 1.3     [new]
    2.3 Assignment and Input                        CSA 1.4     [new]
    2.4 Casting and Ranges of Values                 CSA 1.5     [new]
    2.5 Compound Assignment Operators                CSA 1.6     [new]
3   APIs, Libraries & Documentation                  [header]
    3.1 APIs and Libraries                          CSA 1.7     [new]
    3.2 Documentation with Comments and Preconditions CSA 1.8    [new]
    3.3 Packages & Imports                                       [existing] ← folded in from old Ch.4; "packages" is a
        subsection inside CSA 1.7, already covered at 3.1, so no reason to keep it as its own chapter
4   Using Objects & Calling Methods                  [header, no existing anchor]
    4.1 Calling Class Methods                        CSA 1.10    [new]
    4.2 Using the Math Class                         CSA 1.11    [new]
    4.3 Objects – Instances of Classes                CSA 1.12    [new]
    4.4 Creating and Initializing Objects: Constructors CSA 1.13  [new]
    4.5 Calling Instance Methods                      CSA 1.14    [new]
5   Control Structures                                         [header]
    5.1 if Statements                                 CSA 2.3     [existing]
    5.2 For Loops                                      CSA 2.8     [existing]
    — Boolean Logic & Conditional Design —
    5.3 Algorithms with Selection and Repetition       CSA 2.1     [new]
    5.4 Boolean Expressions                            CSA 2.2     [new]
    5.5 Nested if Statements                           CSA 2.4     [new]
    5.6 Compound Boolean Expressions                   CSA 2.5     [new]
    5.7 Comparing Boolean Expressions (De Morgan's Laws) CSA 2.6   [new]
    — Loops in Depth —
    5.8 While Loops                                    CSA 2.7     [new]
    5.9 Implementing Selection and Iteration Algorithms CSA 2.9    [new]
    5.10 Nested Iteration                              CSA 2.11    [new]
    5.11 Informal Runtime Analysis of Loops            CSA 2.12    [new]
6   Strings                                            [header, no existing anchor] ← moved to right after Control
    Structures finishes (not mid-chapter) — a concrete thing to loop over right after loops are taught, and this also
    resolves the old two-parent dependency flag on String Algorithms (now cleanly follows both Strings and all of Loops)
    6.1 Strings                                        CSA 1.15    [new]
    6.2 String Algorithms                              CSA 2.10    [new]
7   The Class Blueprint                                        [header]
    7.1 Anatomy of a Java Class                        CSA 3.3     [existing]
    7.2 Methods: How to Write Them                     CSA 3.5     [existing]  ← "Reusable Methods" depth lives here
    7.3 Methods: Passing/Returning References of an Object CSA 3.6 [new]  ← moved from Ch.8
    7.4 Class (static) Variables and Methods           CSA 3.7     [new]  ← moved from Ch.8
8   Constructors & "this"                                       [header]
    8.1 Writing Constructors                           CSA 3.4     [existing]
    8.2 this Keyword                                   CSA 3.9     [existing]
9   Storing Data                                                [header]
    9.1 Array Creation and Access                      CSA 4.3     [existing]
    9.2 ArrayList and its Methods                      CSA 4.8     [existing]
    9.3 Optional: HashMap (Dictionary) Data Structure CSA 4.60    [existing]
    — Arrays & ArrayLists: Traversal Patterns —
    9.4 Array Traversals                               CSA 4.4     [new]
    9.5 Implementing Array Algorithms                  CSA 4.5     [new]
    9.6 ArrayList Traversals                           CSA 4.9     [new]
    9.7 Implementing ArrayList Algorithms              CSA 4.10    [new]
    — Wrapper Classes & Text Files (looser fit, flagged) —
    9.8 Using Text Files                                CSA 4.6     [new]
    9.9 Wrapper Classes – Integer and Double            CSA 4.7     [new]  ← candidate to drop later: mostly
        AP-exam-specific boxing/unboxing detail, int/double already covered at 2.1
10  2D Arrays                                          [header, no existing anchor] ← own chapter (FRC-relevant:
    vision matrices, odometry math)
    10.1 2D Array Creation and Access                  CSA 4.11    [new]
    10.2 2D Array Traversals: Nested Loops             CSA 4.12    [new]
    10.3 Implementing 2D Array Algorithms              CSA 4.13    [new]
11  Enums: Named Choices                                        [existing] ⚠ source needed — left in place on purpose (feeds Java 2's State Machines)
12  Exceptions & try/catch                                      [existing] ⚠ mechanism source needed
13  Common Gotchas                                              [existing]
14  How to Practice                                             [existing]

JAVA 2
15  Why Design Patterns?                                        [existing]
16  Advanced Collections (Set/Queue/Map)                        [existing] (no CSA equivalent at all)
17  Writing Your Own Generics                                   [existing]
18  Inheritance & Abstractions                                  [header]
    18.1 Inheritance, Superclass, Subclass            CSA 5.1     [existing]
    18.2 Inheritance and Constructors                  CSA 5.2     [new]
    18.3 Inheritance Hierarchies                       CSA 5.5     [new]
    18.4 Object Superclass                             CSA 5.7     [new]
19  Polymorphism: Many Forms                                    [header]
    19.1 Overriding Methods                            CSA 5.3     [existing]
    19.2 super Keyword                                 CSA 5.4     [existing]
    19.3 Polymorphism                                  CSA 5.6     [existing]
20  Interfaces as Contracts                                     [existing] (no CSA mapping at all, same case as 3.3)
    20.1 Lambdas & Method References                              [existing, relocated from Java 1] ⚠ source needed
21  The IO-Layer Pattern                                        [existing]
22  Static Factories                                            [existing]
23  The Builder Pattern                                         [existing]
24  Encapsulation & Final                                       [header]
    24.1 Scope and Access                              CSA 3.8     [existing]
25  Optional: Maybe a Value                                     [existing]
26  State Machines: Logic (enum)                                [existing]
27  Managing Transitions (switch)                               [existing]
28  Event Loops & Triggers                                      [existing]
29  Architecture Takeaways (DRY/YAGNI/SOLID)                    [existing]

ADDITIONAL TOPICS
30  Algorithms: Searching, Sorting & Recursion         [header, no existing anchor] ← placement still open, could fold into Ch.9 instead
    30.1 Searching Algorithms                          CSA 4.14    [new]
    30.2 Sorting Algorithms                            CSA 4.15    [new]
    30.3 Recursion                                     CSA 4.16    [new]
    30.4 Recursive Searching and Sorting                CSA 4.17    [new]

OPTIONAL / SUPPLEMENTARY
31  Program Design & Abstraction  ⚠ OPTIONAL          [header, no existing anchor] ← was the required "Bridge"
    between Java 1 and Java 2; demoted to optional and moved here. FRC teams build on WPILib's imposed architecture
    regardless, so general from-scratch program-design principles are informational, not a required gateway.
    31.1 Abstraction and Program Design                CSA 3.1     [new]
    31.2 Impact of Program Design                      CSA 3.2     [new]
32  Data Ethics & Data Sets  ⚠ OPTIONAL                [header, no existing anchor] ← was "flagged, recommend skip,"
    downgraded to optional rather than dropped entirely
    32.1 Ethical and Social Issues Around Data Collection CSA 4.1   [new]
    32.2 Data Sets                                     CSA 4.2     [new]
```

## Dropped from the deck, absorbed elsewhere

- **Reusable Methods** — was a thin, 3-bullet "statement of facts" slide, not real lesson depth.
  Folded into Ch.7 The Class Blueprint (a method doesn't exist outside a class anyway; CSA's own
  3.3→3.4→3.5 sequence treats class-anatomy and method-writing as one unit). Real depth lives at
  item 7.2 (CSA 3.5 "Methods: How to Write Them").

## Needs an external source — CSA doesn't (fully) cover these

**Chosen source: [Oracle's official Java Tutorials](https://docs.oracle.com/javase/tutorial/)**
(docs.oracle.com) — free, authoritative, web-based, has dedicated pedagogical lesson pages for
each item below (not just reference docs). Captured into `other-reference-repo/oracle-java-tutorials/`
(a 4th repo, generic across future external sources too — see that repo's own README) rather
than a CSA-style mirror repo, since this pull is much narrower than a full trail per item.

Original scope was just the 3 gaps below the line; a later pass caught that ~11 of Java 2's
chapters had zero CSA mapping *and* zero external-source plan — the 3 rows above the line
(Ch.16/17/20) are the ones confirmed as a genuine Oracle fit out of that group (see this file's
"Optional/Supplementary" history or [[project_csa_topic_mapping]] memory for the ones ruled out
as not an Oracle fit — design patterns, WPILib-specific content).

| Item | Oracle source page | Status |
|---|---|---|
| Ch.16 Advanced Collections (Set/Queue/Deque/Map) | [Collections → Interfaces](https://docs.oracle.com/javase/tutorial/collections/interfaces/index.html) | **Captured** — `oracle-java-tutorials/collections-interfaces/` (4 files), verbatim |
| Ch.17 Generics (basics) | [Lesson: Generics](https://docs.oracle.com/javase/tutorial/java/generics/index.html) | **Captured** — `oracle-java-tutorials/generics/` (5 files), verbatim |
| Ch.20 Interfaces (base topic) | [Interfaces and Inheritance → Interfaces half](https://docs.oracle.com/javase/tutorial/java/IandI/index.html) | **Captured** — `oracle-java-tutorials/interfaces/` (6 files), verbatim |
| Ch.11 Enums | [Enum Types](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) | **Captured** — `oracle-java-tutorials/enums/enum-types.md`, verbatim |
| Ch.12 Exceptions & try/catch — the **mechanism** | [Lesson: Exceptions](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html) | **Captured** — `oracle-java-tutorials/exceptions/` (16 files), verbatim |
| 20.1 Lambdas & Method References | [Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html) | **Captured** — `oracle-java-tutorials/lambdas/` (2 files + Anonymous Classes companion), verbatim |

All 34 pages captured 2026-09-09. Content-authoring (the actual FRC-geared rewrite) not started
— these are source material for that step, same relationship as the CSA files.

## Optional / Supplementary (Ch.31-32)

Two chapters demoted from "required" to optional this round:

- **Ch.31 Program Design & Abstraction** (CSA 3.1, 3.2) — was the required "Bridge" between
  Java 1 and Java 2. Downgraded to optional and moved to the end: FRC teams build on WPILib's
  imposed architecture regardless of what general program-design theory says, so this is
  informational rather than a required gateway with no other option in practice.
- **Ch.32 Data Ethics & Data Sets** (CSA 4.1, 4.2) — previously "flagged, recommend skip."
  Downgraded to optional rather than dropped entirely.

## Exercise/quiz sizing (proposed, not settled)

One exercise per item. 2-3 checkpoint quizzes total across all of this (end of the Java-1-side
new content, end of Java 2/Additional Topics) rather than one per item.

## Open questions (not yet decided)

- Ch.30 Algorithms (Searching, Sorting, Recursion) — still in "Additional Topics." Ch.10 2D
  Arrays already promoted to its own chapter (confirmed FRC-relevant), but the user only
  confirmed that one — Algorithms' placement is still open, could fold into Ch.9 instead.
- Item 9.9 (Wrapper Classes – Integer and Double) — flagged as a candidate to drop entirely:
  mostly AP-exam-specific boxing/unboxing detail, and int/double are already covered at 2.1.
- Final naming/numbering scheme — the chapter numbers above are sequence-order placeholders
  only (Java 1a/2a, Java III+, or something else still open).
- Should `java-1.js`/`java-2.js` themselves ever be split into finer items to match this new
  granularity, or stay as the fixed fast-overview tier permanently?

## Provenance convention for this repo

Every new lesson file built from this outline should carry a reference line back to its
sources, e.g.:
```
Derived from csawesome-2026: unit-2-selection-and-iteration/2.02-boolean-expressions.md (CSA 2.2)
Deck context: mechacoder-test/src/lessons/java-1.js ("Control Structures" slide)
```
