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

## Combined Learning Path — v5

Also viewable as a formatted page: see the "Curriculum Ledger" artifact (dots for
existing/new, same content as below, easier to scan).

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
3   APIs, Libraries & Documentation                  [header, no existing anchor]
    3.1 APIs and Libraries                          CSA 1.7     [new]
    3.2 Documentation with Comments and Preconditions CSA 1.8    [new]
4   Packages & Imports                                         [existing] (moved up; no CSA number of its own)
5   Using Objects & Calling Methods                  [header, no existing anchor]
    5.1 Calling Class Methods                        CSA 1.10    [new]
    5.2 Using the Math Class                         CSA 1.11    [new]
    5.3 Objects – Instances of Classes                CSA 1.12    [new]
    5.4 Creating and Initializing Objects: Constructors CSA 1.13  [new]
    5.5 Calling Instance Methods                      CSA 1.14    [new]
6   Control Structures                                         [header]
    6.1 if Statements                                 CSA 2.3     [existing]
    6.2 For Loops                                      CSA 2.8     [existing]
    — Boolean Logic & Conditional Design —
    6.3 Algorithms with Selection and Repetition       CSA 2.1     [new]
    6.4 Boolean Expressions                            CSA 2.2     [new]
    6.5 Nested if Statements                           CSA 2.4     [new]
    6.6 Compound Boolean Expressions                   CSA 2.5     [new]
    6.7 Comparing Boolean Expressions (De Morgan's Laws) CSA 2.6   [new]
    — Loops in Depth —
    6.8 While Loops                                    CSA 2.7     [new]
    6.9 Implementing Selection and Iteration Algorithms CSA 2.9    [new]
    6.10 Nested Iteration                              CSA 2.11    [new]
    6.11 Informal Runtime Analysis of Loops            CSA 2.12    [new]
7   The Class Blueprint                                        [header]
    7.1 Anatomy of a Java Class                        CSA 3.3     [existing]
    7.2 Methods: How to Write Them                     CSA 3.5     [existing]  ← "Reusable Methods" depth lives here
    7.3 Methods: Passing/Returning References of an Object CSA 3.6 [new]  ← moved from Ch.8
    7.4 Class (static) Variables and Methods           CSA 3.7     [new]  ← moved from Ch.8
8   Constructors & "this"                                       [header]
    8.1 Writing Constructors                           CSA 3.4     [existing]
    8.2 this Keyword                                   CSA 3.9     [existing]
9   Strings                                            [header, no existing anchor]
    9.1 Strings                                        CSA 1.15    [new]
    9.2 String Algorithms                              CSA 2.10    [new]  (also depends on Ch.6 Loops)
10  Storing Data                                                [header]
    10.1 Array Creation and Access                     CSA 4.3     [existing]
    10.2 ArrayList and its Methods                     CSA 4.8     [existing]
    10.3 Optional: HashMap (Dictionary) Data Structure CSA 4.60    [existing]
    — Arrays & ArrayLists: Traversal Patterns —
    10.4 Array Traversals                              CSA 4.4     [new]
    10.5 Implementing Array Algorithms                 CSA 4.5     [new]
    10.6 ArrayList Traversals                          CSA 4.9     [new]
    10.7 Implementing ArrayList Algorithms             CSA 4.10    [new]
    — Wrapper Classes & Text Files (looser fit, flagged) —
    10.8 Using Text Files                               CSA 4.6     [new]
    10.9 Wrapper Classes – Integer and Double           CSA 4.7     [new]
11  2D Arrays                                          [header, no existing anchor] ← promoted to own chapter (FRC-relevant: vision matrices, odometry)
    11.1 2D Array Creation and Access                  CSA 4.11    [new]
    11.2 2D Array Traversals: Nested Loops             CSA 4.12    [new]
    11.3 Implementing 2D Array Algorithms              CSA 4.13    [new]
12  Enums: Named Choices                                        [existing] ⚠ source needed — left in place on purpose (feeds Java 2's State Machines)
13  Exceptions & try/catch                                      [existing] ⚠ mechanism source needed
14  Common Gotchas                                              [existing]
15  How to Practice                                             [existing]

BRIDGE
16  Program Design & Abstraction                      [header, no existing anchor] ← the entire Bridge
    16.1 Abstraction and Program Design                CSA 3.1     [new]
    16.2 Impact of Program Design                      CSA 3.2     [new]

JAVA 2
17  Why Design Patterns?                                        [existing]
18  Advanced Collections (Set/Queue/Map)                        [existing] (no CSA equivalent at all)
19  Writing Your Own Generics                                   [existing]
20  Inheritance & Abstractions                                  [header]
    20.1 Inheritance, Superclass, Subclass            CSA 5.1     [existing]
    20.2 Inheritance and Constructors                  CSA 5.2     [new]
    20.3 Inheritance Hierarchies                       CSA 5.5     [new]
    20.4 Object Superclass                             CSA 5.7     [new]
21  Polymorphism: Many Forms                                    [header]
    21.1 Overriding Methods                            CSA 5.3     [existing]
    21.2 super Keyword                                 CSA 5.4     [existing]
    21.3 Polymorphism                                  CSA 5.6     [existing]
22  Interfaces as Contracts                                     [existing] (no CSA mapping at all, same case as Ch.4)
    22.1 Lambdas & Method References                              [existing, relocated from Java 1] ⚠ source needed
23  The IO-Layer Pattern                                        [existing]
24  Static Factories                                            [existing]
25  The Builder Pattern                                         [existing]
26  Encapsulation & Final                                       [header]
    26.1 Scope and Access                              CSA 3.8     [existing]
27  Optional: Maybe a Value                                     [existing]
28  State Machines: Logic (enum)                                [existing]
29  Managing Transitions (switch)                               [existing]
30  Event Loops & Triggers                                      [existing]
31  Architecture Takeaways (DRY/YAGNI/SOLID)                    [existing]

ADDITIONAL TOPICS
32  Algorithms: Searching, Sorting & Recursion         [header, no existing anchor] ← placement still open, could fold into Ch.10 instead
    32.1 Searching Algorithms                          CSA 4.14    [new]
    32.2 Sorting Algorithms                            CSA 4.15    [new]
    32.3 Recursion                                     CSA 4.16    [new]
    32.4 Recursive Searching and Sorting                CSA 4.17    [new]
```

## Dropped from the deck, absorbed elsewhere

- **Reusable Methods** — was a thin, 3-bullet "statement of facts" slide, not real lesson depth.
  Folded into Ch.7 The Class Blueprint (a method doesn't exist outside a class anyway; CSA's own
  3.3→3.4→3.5 sequence treats class-anatomy and method-writing as one unit). Real depth lives at
  item 7.2 (CSA 3.5 "Methods: How to Write Them").

## Needs an external source — CSA doesn't (fully) cover these

**Chosen source: [Oracle's official Java Tutorials](https://docs.oracle.com/javase/tutorial/)**
(docs.oracle.com) — free, authoritative, web-based, has dedicated pedagogical lesson pages for
each of the 3 gaps below (not just reference docs). Kept inside this repo (Repo 3) directly for
now — no separate mirror repo the way `csawesome-2026` was built for CSA, since it's only 3
targeted topics, not a whole curriculum to structure.

| Item | What CSA actually has | Oracle source page | Status |
|---|---|---|---|
| Ch.12 Enums | Zero mentions anywhere in the captured content. Not on the AP exam at all. | [Enum Types](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) (Learning the Java Language > Classes and Objects) | Not started |
| Ch.13 Exceptions & try/catch — the **mechanism** | CSA teaches exception *concepts* substantively but scattered across many lessons (`ArithmeticException`, `IndexOutOfBoundsException`, `NullPointerException` all come up naturally — no new cluster needed for that, it'll thread through the other lessons as written). But CSA explicitly excludes `try`/`catch` itself: *"This method uses a try catch block for error-checking which is not covered in the AP exam"* (its own words, from the Consumer Review Lab). | [Lesson: Exceptions](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html) (Essential Java Classes) | Not started |
| 22.1 Lambdas & Method References | Zero CSA coverage (not on the AP exam; Java 8+ feature outside its scope). Moved to Java 2, under "Interfaces as Contracts" (Ch.22), since a lambda is really shorthand for a functional interface — teaching it before interfaces exist (its old Java 1 spot) had no real grounding. | [Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html) (Learning the Java Language > Classes and Objects) | Not started |

"Not started" = source identified, nothing fetched yet. Update this table's Status column (and
add a captured-content note, same provenance style as the CSA work) once any of these are
actually pulled in.

## Flagged from CSA — weak fit, reconsider before building

| CSA topics | Why flagged |
|---|---|
| 4.1 (Ethical/Social Issues Around Data), 4.2 (Data Sets) | Generic AP-exam content with no obvious FRC tie-in. Recommend skip. |

## Exercise/quiz sizing (proposed, not settled)

One exercise per cluster-lesson. 2-3 checkpoint quizzes total across all of this (end of the
Java-1-side new clusters, end of Bridge, end of Java-2-side/Additional Topics) rather than one
per cluster.

## Open questions (not yet decided)

- Ch.32 Algorithms (Searching, Sorting, Recursion) — still in "Additional Topics" (after Java 2).
  Ch.11 2D Arrays already promoted to its own chapter (confirmed FRC-relevant), but the user only
  confirmed that one — Algorithms' placement is still open, could fold into Ch.10 instead.
- Items 10.8/10.9 (Wrapper Classes & Text Files) — still flagged as a looser topical fit under
  Ch.10 Storing Data than the array items around them.
- Item 9.2 (String Algorithms) — genuinely depends on both Ch.9 (Strings) and Ch.6 (Loops); Ch.9
  was picked as the primary parent, not re-litigated further.
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
