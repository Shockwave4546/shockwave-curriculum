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

## Combined Learning Path — v15

**This file is the source of truth.** Also viewable as a formatted page — the "Curriculum
Ledger", source at `shockwave-curriculum/curriculum-ledger.html` (this is now the one
canonical local copy — never edit or publish from a session scratchpad path again), published
at https://claude.ai/code/artifact/b33b0cff-ce35-4977-bddc-14f50d1a1b27. Same content as below
with dots for existing/new, easier to scan. Sync flows one way: edit here first, then mirror
the change into `curriculum-ledger.html` and republish (pass the artifact URL above so it
updates in place rather than forking a new one). **Any edit to this section without a matching
Ledger update leaves the Ledger stale** — this already happened once (the whole Oracle-capture
status went unsynced for a while). Update both in the same pass, don't defer the Ledger sync to
"later."

**Numbering rule**: every chapter number is a pure organizational label — it never carries a
CSA reference itself. Every actual piece of content (existing or new) is a numbered item
underneath its chapter, even when there's only one. "Item" is a placeholder term, not "lesson"
— that already means something specific in mechacoder's own code (`registerLesson()`). Chapter
numbers here are sequence-order placeholders, not a proposed final naming scheme.

```
JAVA 1
1   Getting Started                                             [header]
    1.1 Why Java for FRC?                                       [existing]
    1.2 Intro to Algorithms, Programming & Compilers CSA 1.1     [new] — the base-syntax lesson
        (statements/semicolons, a first Java program, IDE/compiler concept, keywords, syntax vs.
        run-time errors, comments). Item 2.1 originally covered semicolons redundantly with this;
        removed from 2.1 once this item was added.
2   Variables & Types                                          [header]
    2.1 Variables and Data Types                    CSA 1.2     [existing]
    2.2 Expressions and Output                      CSA 1.3     [new]
    2.3 Assignment and Input                        CSA 1.4     [new]
    2.4 Casting and Ranges of Values                 CSA 1.5     [new]
    2.5 Compound Assignment Operators                CSA 1.6     [new]
3   APIs, Libraries & Documentation                  [header]
    3.1 APIs and Libraries                          CSA 1.7     [new]
    3.2 Documentation with Comments and Preconditions CSA 1.8    [new]
    3.3 Packages & Imports                          CSA 1.7 §1.7.2 [existing] ← folded in from old Ch.4; a real
        existing deck slide (java-1.js section 10), distinct from 3.1's not-yet-authored content — they just
        happen to share the same CSA source page (1.7.2 is the "Packages" subsection specifically)
4   Using Objects & Calling Methods                  [header, no existing anchor]
    4.1 Methods, Signatures and Parameters            CSA 1.9     [new] — genuinely missed on the first
        pass: csawesome-2026's own file tagged this "already covered in the FRC deck," but the deck's
        existing "Reusable Methods" slide (7.2) never actually teaches method signatures, parameters
        vs. arguments, call-by-value, or overloading — just shows one example with a parameter in
        passing. Caught while reviewing 2.1 during the Lessons-authoring pass; same class of mistake
        as the earlier 1.12/1.13 mis-tagging (see v4 history above).
    4.2 Calling Class Methods                        CSA 1.10    [new]
    4.3 Using the Math Class                         CSA 1.11    [new]
    4.4 Objects – Instances of Classes                CSA 1.12    [new]
    4.5 Creating and Initializing Objects: Constructors CSA 1.13  [new]
    4.6 Calling Instance Methods                      CSA 1.14    [new]
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
    9.8 Using Text Files                                CSA 4.6     [new]
10  2D Arrays                                          [header, no existing anchor] ← own chapter (FRC-relevant:
    vision matrices, odometry math)
    10.1 2D Array Creation and Access                  CSA 4.11    [new]
    10.2 2D Array Traversals: Nested Loops             CSA 4.12    [new]
    10.3 Implementing 2D Array Algorithms              CSA 4.13    [new]
11  Enums: Named Choices                        ORACLE 10.1     [existing] ✓ captured — left in place on purpose (feeds Java 2's State Machines)
12  Exceptions & try/catch                       ORACLE 11.1-16  [existing] ✓ mechanism captured —
    CSA excludes try/catch by its own words: "not covered in the AP exam" (exception concepts
    like ArithmeticException/IndexOutOfBoundsException/NullPointerException are taught, just not
    the try/catch mechanism itself)
13  Common Gotchas                                              [existing] ← likely thinner than
    it should be; a real practice/exercise pass will probably surface more real gotchas than the
    deck's current teaser slide covers (see Open questions)

JAVA 2
14  Why Design Patterns?                                        [existing]
15  Advanced Collections (Set/Queue/Map)         ORACLE 13.1-4   [existing] ✓ captured (no CSA equivalent at all)
16  Writing Your Own Generics                    ORACLE 14.1-5   [existing] ✓ captured
17  Inheritance & Abstractions                                  [header]
    17.1 Inheritance, Superclass, Subclass            CSA 5.1     [existing]
    17.2 Inheritance and Constructors                  CSA 5.2     [new]
    17.3 Inheritance Hierarchies                       CSA 5.5     [new]
    17.4 Object Superclass                             CSA 5.7     [new]
18  Polymorphism: Many Forms                                    [header]
    18.1 Overriding Methods                            CSA 5.3     [existing]
    18.2 super Keyword                                 CSA 5.4     [existing]
    18.3 Polymorphism                                  CSA 5.6     [existing]
19  Interfaces as Contracts                      ORACLE 15.1-6   [existing] ✓ captured (no CSA mapping at all, same case as 3.3)
    19.1 Lambdas & Method References              ORACLE 12.1-2  [existing, relocated from Java 1] ✓ captured —
        moved here since a lambda is really shorthand for a functional interface; teaching it
        before Interfaces exists (its old Java 1 spot) had no real grounding
20  The IO-Layer Pattern              ADVKIT 40.1-11, JDP 50.1  [existing] ✓ captured — the
    pattern's real origin: Team 6328's own AdvantageKit docs (hardware abstraction, why
    simulation/replay fall out of it for free) plus Hexagonal Architecture (Ports & Adapters)
    for generic-CS grounding. See "Needs an external source" below for the full writeup.
21  Static Factories                                 T5817 30.2   [existing]
22  The Builder Pattern                              T5817 30.1   [existing]
23  Encapsulation & Final                                       [header]
    23.1 Scope and Access                              CSA 3.8     [existing]
24  Optional: Avoiding Null Pointer Exceptions        ORACLE 16.1  [existing] ✓ captured — renamed
    from "Optional: Maybe a Value" to disambiguate from optional method parameters, per the label
    concern raised earlier; the deck's actual slide heading is unchanged (mechacoder-test is
    frozen), this is an outline-label-only rename
25  Command-Based Programming                       WPILIB 20.1-8 [header, no existing anchor] ← this
    is the big one: WPILib's own official architecture pattern (Subsystems + Commands + Triggers +
    Scheduler). Placed here since it builds directly on IO-Layer (20) and Interfaces (19). 25.4-25.6
    absorb what used to be three separate one-slide chapters (old Ch.25 State Machines, old Ch.26
    Managing Transitions, old Ch.27 Event Loops & Triggers) — real conceptual overlap: Command-Based
    IS the framework those three were describing pieces of. Order: intro → building blocks (Commands,
    Scheduler) → a common technique for a Subsystem/Command's internal logic (enum/switch state
    machines) → the external reactive piece (Triggers) → real project structure last.
    25.1 What Is Command-Based Programming?          WPILIB 20.1  [new]
    25.2 Commands & Command Compositions             WPILIB 20.2-3 [new]
    25.3 The Command Scheduler                       WPILIB 20.8  [new]
    25.4 State Machines: Logic (enum)                T5817 31.1-4 [existing, was Ch.25]
    25.5 Managing Transitions (switch)               T5817 31.1-4 [existing, was Ch.26]
    25.6 Binding Commands to Triggers                WPILIB 20.5  [existing, was Ch.27 "Event Loops & Triggers"]
    25.7 Structuring a Command-Based Robot Project    WPILIB 20.4,6-7 [new]
26  Architecture Takeaways (DRY/YAGNI/SOLID)                    [existing] ← was Ch.28; still unsourced,
    neither WPILib nor T5817 teach these as named general principles

OPTIONAL / ADVANCED TOPICS
27  Program Design & Abstraction  ⚠ OPTIONAL          [header, no existing anchor] ← conceptually sits between
    Java 1 and Java 2 (was the required "Bridge"); demoted to optional since FRC teams build on WPILib's imposed
    architecture regardless, so general from-scratch program-design principles are informational, not a required
    gateway. Listed first in this block to preserve that conceptual position even though physically both chapters
    here trail Java 2.
    27.1 Abstraction and Program Design                CSA 3.1     [new]
    27.2 Impact of Program Design                      CSA 3.2     [new]
28  Algorithms: Searching, Sorting & Recursion  ⚠ OPTIONAL  [header, no existing anchor] ← conceptually sits after
    Java 2 (deepens the data-structure work from Ch.9/Ch.10); optional rather than required.
    28.1 Searching Algorithms                          CSA 4.14    [new]
    28.2 Sorting Algorithms                            CSA 4.15    [new]
    28.3 Recursion                                     CSA 4.16    [new]
    28.4 Recursive Searching and Sorting                CSA 4.17    [new]
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
(Ch.15/16/19) are the ones confirmed as a genuine Oracle fit out of that group (see this file's
"Optional/Supplementary" history or [[project_csa_topic_mapping]] memory for the ones ruled out
as not an Oracle fit — design patterns, WPILib-specific content). See "Optional / Advanced
Topics" below for the Ch.27/28 renumbering and Ch.32's removal.

| Item | ORACLE ref | Oracle source page | Status |
|---|---|---|---|
| Ch.15 Advanced Collections (Set/Queue/Deque/Map) | ORACLE 13.1–13.4 | [Collections → Interfaces](https://docs.oracle.com/javase/tutorial/collections/interfaces/index.html) | **Captured** — `oracle-java-tutorials/collections-interfaces/` (4 files), verbatim |
| Ch.16 Generics (basics) | ORACLE 14.1–14.5 | [Lesson: Generics](https://docs.oracle.com/javase/tutorial/java/generics/index.html) | **Captured** — `oracle-java-tutorials/generics/` (5 files), verbatim |
| Ch.19 Interfaces (base topic) | ORACLE 15.1–15.6 | [Interfaces and Inheritance → Interfaces half](https://docs.oracle.com/javase/tutorial/java/IandI/index.html) | **Captured** — `oracle-java-tutorials/interfaces/` (6 files), verbatim |
| Ch.11 Enums | ORACLE 10.1 | [Enum Types](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) | **Captured** — `oracle-java-tutorials/enums/enum-types.md`, verbatim |
| Ch.12 Exceptions & try/catch — the **mechanism** | ORACLE 11.1–11.16 | [Lesson: Exceptions](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html) | **Captured** — `oracle-java-tutorials/exceptions/` (16 files), verbatim |
| 19.1 Lambdas & Method References | ORACLE 12.1–12.2 | [Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html) | **Captured** — `oracle-java-tutorials/lambdas/` (2 files: 12.1 Anonymous Classes, 12.2 Lambda Expressions), verbatim |
| Ch.24 Optional: Avoiding Null Pointer Exceptions | ORACLE 16.1 | ["Tired of Null Pointer Exceptions? Consider Using Java SE 8's Optional!"](https://www.oracle.com/technical-resources/articles/java/java8-optional.html) — an Oracle technical article, not the tutorial trail (confirmed via Oracle's own site-wide index that the classic trail has zero Optional coverage) | **Captured** — `oracle-java-tutorials/optional/java8-optional.md`, verbatim |

35 pages captured 2026-09-09 (34 from the tutorial trail + 1 technical article). **ORACLE unit
numbering** (10-16, deliberately clear of CSA's
0-5 so the two are never ambiguous) mirrors CSA's `Unit.Item` scheme — see each file's own
`**Oracle ref:**` line. Content-authoring (the actual FRC-geared rewrite) not started — these
are source material for that step, same relationship as the CSA files.

### WPILib's official docs — chosen source for Ch.25 Command-Based Programming

**Source: [WPILib's Command-Based Programming trail](https://docs.wpilib.org/en/stable/docs/software/commandbased/index.html)**
(docs.wpilib.org) — free, authoritative, the actual framework Team 6328 (and every other FRC
team) builds robot code on. Confirmed this is the *current/stable* docs, not a stale archived
version, before scoping it (checked directly — no more "2020 rewrite" framing that the old 2021
archive had). Scoped down to 8 pages, skipping PID Control, Motion Profiling, and the
C++-specific "Technical Discussion on C++ Commands" pages — those belong to a controls course,
not this Java/OOP curriculum. Captured into `other-reference-repo/wpilib/command-based/` — see
that repo's own README for the numbering scheme (**WPILIB Unit 20**).

| Item | WPILIB ref | Page | Status |
|---|---|---|---|
| 25.1 What Is Command-Based Programming? | WPILIB 20.1 | [What Is "Command-Based" Programming?](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html) | **Captured** — `wpilib/command-based/01-what-is-command-based.md`, verbatim |
| 25.2 Commands & Command Compositions | WPILIB 20.2-3 | [Commands](https://docs.wpilib.org/en/stable/docs/software/commandbased/commands.html), [Command Compositions](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-compositions.html) | **Captured** — `wpilib/command-based/02-commands.md`, `03-command-compositions.md`, verbatim |
| 25.7 Structuring a Command-Based Robot Project | WPILIB 20.4,6-7 | [Subsystems](https://docs.wpilib.org/en/stable/docs/software/commandbased/subsystems.html), [Structuring a Command-Based Robot Project](https://docs.wpilib.org/en/stable/docs/software/commandbased/structuring-command-based-project.html), [Organizing Command-Based Robot Projects](https://docs.wpilib.org/en/stable/docs/software/commandbased/organizing-command-based.html) | **Captured** — `wpilib/command-based/04-subsystems.md`, `06-structuring-command-based-project.md`, `07-organizing-command-based.md`, verbatim |
| 25.6 Binding Commands to Triggers (was Ch.27) | WPILIB 20.5 | [Binding Commands to Triggers](https://docs.wpilib.org/en/stable/docs/software/commandbased/binding-commands-to-triggers.html) | **Captured** — `wpilib/command-based/05-binding-commands-to-triggers.md`, verbatim |
| 25.3 The Command Scheduler | WPILIB 20.8 | [The Command Scheduler](https://docs.wpilib.org/en/stable/docs/software/commandbased/command-scheduler.html) | **Captured** — `wpilib/command-based/08-command-scheduler.md`, verbatim |

### Team 5817's public training guide — chosen source for Ch.21, Ch.22, and 25.4/25.5

**Source: [Team 5817's Programming Training guide](https://uni-rex5817.gitbook.io/programming-training/)**
— another FRC team's publicly-published GitBook, no login/paywall, no restrictive license notice
found on the site. User found the Builder page directly; browsing that same guide's Design
Patterns section turned up a matching Factory page, and its Subsystems section turned up real
FRC-code examples of enum state machines living inside command-based subsystems. Captured into
`other-reference-repo/team-5817-training/` — see that repo's own README for the numbering scheme
(**T5817 Unit 30** design patterns, **Unit 31** subsystem/state-based patterns).

| Item | T5817 ref | Page | Status |
|---|---|---|---|
| Ch.22 The Builder Pattern | T5817 30.1 | [Builder](https://uni-rex5817.gitbook.io/programming-training/code/design-patterns/builder) | **Captured** — `team-5817-training/design-patterns/builder.md`, verbatim |
| Ch.21 Static Factories | T5817 30.2 | [Factory](https://uni-rex5817.gitbook.io/programming-training/code/design-patterns/factory) | **Captured** — `team-5817-training/design-patterns/factory.md`, verbatim |
| 25.4 State Machines / 25.5 Managing Transitions | T5817 31.1-4 | [How do I make a Subsystem Work?](https://uni-rex5817.gitbook.io/programming-training/code/how-do-i-make-a-subsystem-work) + 3 sub-pages (Servo/Roller state-based subsystems, Subsystem Manager) | **Captured** — `team-5817-training/subsystems/` (4 files), verbatim |

### AdvantageKit + java-design-patterns.com — chosen sources for Ch.20 The IO-Layer Pattern

**Source: [AdvantageKit's official docs](https://docs.advantagekit.org/)** — Team 6328
(Mechanical Advantage)'s own logging/telemetry/replay framework, used by 598 FRC teams as of
2025. This is the actual origin of Ch.20's pattern, not just an analogy: the deck's existing
IntakeIOSparkMax/IntakeIOSim example is a direct application of AdvantageKit's "IO layer"
convention. User specifically wanted to lean into this source heavily, since it's one of Team
6328's biggest community contributions and the curriculum's deck is expected to go deeper on it
later. Captured into `other-reference-repo/advantagekit/` — see that repo's own README for the
numbering scheme (**ADVKIT Unit 40**) and full scope table (11 pages: the conceptual "why",
real case studies, data-flow mechanics including the anchor "IO Interfaces" page, and replay
theory including real 2025 usage-comparison data against Hoot Replay).

**Also: [java-design-patterns.com](https://java-design-patterns.com/) — Hexagonal Architecture
(Ports and Adapters)**, for generic-CS grounding. Initially considered "Layered Architecture"
(closer to N-tier web-app layers, a looser match) — checked both pages directly and picked
Hexagonal Architecture instead, since "core logic isolated from external interfaces... exchangeable
at any level, facilitates test automation" is a much closer conceptual match to the real/sim
IO-interface split. Captured into `other-reference-repo/java-design-patterns/` (**JDP Unit 50**).

| Item | Ref | Page | Status |
|---|---|---|---|
| Ch.20 (why AdvantageKit exists, the "why" narrative) | ADVKIT 40.1-40.4 | Getting Started section | **Captured** — `advantagekit/getting-started/` (4 files), verbatim |
| Ch.20 (data-flow mechanics) | ADVKIT 40.5-40.9 | Data Flow section | **Captured** — `advantagekit/data-flow/` (5 files), verbatim |
| Ch.20 (the anchor page) | ADVKIT 40.8 | [IO Interfaces](https://docs.advantagekit.org/data-flow/recording-inputs/io-interfaces) | **Captured** — matches the deck's existing IntakeIOSparkMax/IntakeIOSim example almost line-for-line |
| Ch.20 (deeper theory + real usage stats) | ADVKIT 40.10-40.11 | Theory section | **Captured** — `advantagekit/theory/` (2 files; Replay Case Studies' 6 sub-pages NOT captured, flagged below) |
| Ch.20 (generic-CS anchor) | JDP 50.1 | [Hexagonal Architecture](https://java-design-patterns.com/patterns/hexagonal-architecture/) | **Captured** — `java-design-patterns/hexagonal-architecture.md`, verbatim |

**Not captured, flagged for later:** AdvantageKit's "Replay Case Studies" turned out to be a
6-sub-page category (Elevator Profile, Autoscoring, Command Gremlins, Aiming Functions, AprilTag
Vision, Traditional Vision), deeper than the originally scoped "1 page" — only the thin index
page was captured. Revisit if a future chapter wants real worked-example depth.

**Also checked and rejected:** a Stackify article
(`stackify.com/optional-parameters-java/`) was suggested as a possible Ch.24 source — read in
full, it never mentions `java.util.Optional` at all; it's entirely about Java's lack of default
*method parameters* (solved via overloading/static factories/Builder/varargs), which is exactly
the *other* "optional" concept flagged in the Open Questions below as a likely source of Ch.24's
label confusion. Also, the live page has what looks like injected SEO spam (gambling site links)
in its footer — avoided citing or capturing anything from that site regardless of content match.

Ch.14 (Why Design Patterns?) and Ch.26 (Architecture Takeaways, DRY/YAGNI/SOLID) — checked
WPILib, Team 5817, AdvantageKit, and java-design-patterns.com; none teach these as named general
principles. Filed as "slide-only" rather than a blocking gap — see the "Slide-only chapters"
section below. See
"Background notes for Ch.14" below for raw material to work from when that authoring happens.

## Background notes for Ch.14 (Why Design Patterns?) — not a source, just notes

**This is NOT a captured/citable source** — it's a synthesized AI-search answer (via Google AI
Search), not a primary source with a single author to attribute. Held onto here as background
material for whenever Ch.14 actually gets written, since it correctly identifies real, relevant
points even though it isn't citable the way Oracle/WPILib/AdvantageKit are:

- **Why patterns matter in FRC specifically:** prevents "spaghetti code" as robots grow more
  complex; isolates hardware from behavior (this IS Ch.20's IO-Layer point); prevents multiple
  mechanisms fighting over the same motor/resource (this is what WPILib's Command Scheduler
  actually does — see Ch.25.3); lets multiple students work on different parts of the robot
  without breaking each other's code.
- **Patterns it names as most relevant to FRC:** the Command-Based pattern itself (already
  Ch.25), the State pattern (already Ch.25.4/25.5 — enum-based state machines for things like an
  arm or elevator), and Singleton (used for subsystems/robot-container-style single-instance
  objects so multiple files don't send conflicting commands to the same motor controller — not
  currently a chapter, worth considering if Ch.14 ends up needing a concrete pattern to point at
  beyond Command-Based).
- Underlying source URLs the AI search cited, for whoever writes Ch.14 to check directly rather
  than trust the synthesis: a Medium post on command-based robotics, a WPILib docs page (already
  captured as ADVKIT/WPILIB material elsewhere), and a couple of community discussion threads —
  not reproduced here since they're just links, not content worth capturing on their own.

## Optional / Advanced Topics (Ch.27-28)

Merged from two separate trailing blocks ("Additional Topics" + "Optional/Supplementary") into
one, since both chapters ended up optional-for-FRC anyway and having two nearly-identical
trailing sections added no real distinction:

- **Ch.27 Program Design & Abstraction** (CSA 3.1, 3.2) — was the required "Bridge" between
  Java 1 and Java 2. Downgraded to optional: FRC teams build on WPILib's imposed architecture
  regardless of what general program-design theory says, so this is informational rather than a
  required gateway with no other option in practice. Ordered first in this block to keep its
  conceptual "sits between Java 1 and Java 2" position visible, even though physically it's
  listed after Java 2 like everything else here.
- **Ch.28 Algorithms: Searching, Sorting & Recursion** (CSA 4.14-4.17) — was "Additional
  Topics," its own band. Folded into this merged block instead since it's also optional for FRC
  purposes; ordered second since it conceptually deepens the data-structure work from Ch.9/10,
  which sits after Java 2 content-wise.

## Excluded from scope — Data Ethics & Data Sets

**Ch.32 Data Ethics & Data Sets (CSA 4.1, 4.2) was dropped from the outline entirely**, not just
demoted to optional. Previously "flagged, recommend skip," then downgraded to optional — now
removed outright. Reasoning: it has no FRC application for the students this curriculum targets,
and the one plausible future use (statistics for scouting/data analysis) isn't a project this
team is anywhere near ready to take on. Revisit only if/when scouting-stats work actually starts
— until then this isn't worth carrying as a phantom optional chapter nobody will assign. Removed
from the Ledger too (never shown there now); this note is the only remaining record.

## Restructured — Command-Based Programming absorbs old Ch.25-27

**New Ch.25 "Command-Based Programming"** was inserted right after Ch.24 (Optional), and old
Ch.25 (State Machines), old Ch.26 (Managing Transitions), and old Ch.27 (Event Loops & Triggers)
were folded into it as items 25.4-25.6 rather than staying separate one-slide chapters. Reasoning:
Command-Based is WPILib's actual blessed architecture (Subsystems + Commands + Triggers +
Scheduler) — old Ch.27's "Event Loops & Triggers" content is really just Command-Based's own
"Binding Commands to Triggers" piece under a different name, and old Ch.25/26's enum+switch state
machine is a common technique used *inside* a command-based Subsystem/Command, not a separate
architecture. Keeping them as three disconnected one-slide chapters was hiding that they're all
part of the same bigger framework. Old Ch.28 (Architecture Takeaways) simply shifted down to
Ch.26; everything in the trailing Optional/Advanced block shifted down by one more (was 29-30,
now 27-28).

Also considered and rejected: moving Ch.21 Static Factories / Ch.22 Builder Pattern up next to
Ch.14 (Why Design Patterns?). Checked the actual deck slides first — Ch.20 IO-Layer Pattern's own
slide text explicitly depends on Ch.19 Interfaces ("the Subsystem only talks to the Interface"),
so 20/21/22 stay where they are, right after Interfaces, matching the original deck's own slide
order.

## Removed — How to Practice (old Ch.14)

**Old Ch.14 "How to Practice" was removed entirely**, not renumbered into anything else. It's a
mechadv-specific chapter (how *their* practice/exercise routine works) — this curriculum's own
practice model will differ and land in a different placement once decided, so keeping it here in
its current MechAdv-shaped form would misrepresent what this outline actually plans to do. Every
chapter from the old Java 2 start onward shifted down by one to close the gap (old Ch.15 →
Ch.14, ... old Ch.31 → Ch.30) — chapter numbers are sequence placeholders anyway, so closing the
gap keeps the sequence readable rather than leaving a skipped 14. Revisit once this curriculum's
own practice/exercise approach and its placement are actually decided.

## Dropped — Item 9.9 (Wrapper Classes – Integer and Double)

**Dropped entirely**, not folded anywhere else. Was CSA 4.7 — mostly AP-exam-specific
boxing/unboxing detail, and int/double are already covered at item 2.1. No item renumbering
needed since 9.9 was the last item in Ch.9 — 9.8 (Using Text Files) is now the chapter's last
item. The "Wrapper Classes & Text Files" subgroup-label was also removed (Text Files alone
didn't need a two-item subgroup label).

## Slide-only chapters (no deeper lesson content yet)

Ch.13 (Common Gotchas), Ch.14 (Why Design Patterns?), and Ch.26 (Architecture Takeaways —
DRY/YAGNI/SOLID) share a real category, not three separate problems: each is a genuine existing
deck slide with no deeper external source backing it, and — for now — that's fine rather than
broken. They're not "missing" content so much as they're simply slide-only for the moment, same
as most of the deck was before this whole sourcing effort started. Revisit any of them
individually if real depth surfaces later (a better source is found, or the practice/exercise
pass surfaces more material), same treatment as everything else in this outline — but there's no
standing obligation to fix these three specifically. Checked against all 6 sources currently in
use (CSA, Oracle, WPILib, Team 5817, AdvantageKit, java-design-patterns.com) for Ch.14/26 before
settling on this framing — none teach either topic as a dedicated lesson.

## Exercise/quiz sizing (proposed, not settled)

One exercise per item. 2-3 checkpoint quizzes total across all of this (end of the Java-1-side
new content, end of Java 2/Additional Topics) rather than one per item.

## Open questions (not yet decided)

- Ch.13, Ch.14, Ch.26 — see "Slide-only chapters" above; not blocking, revisit individually if
  real depth surfaces.
- This curriculum's own practice/exercise model and where it lives in the sequence — needed
  before old Ch.14 "How to Practice" (mechadv-specific, removed) gets any real replacement.
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
