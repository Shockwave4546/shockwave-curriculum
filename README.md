# Shockwave Curriculum

An early-stage learning-platform idea.  The concept didn't solidify until seeing Mechanical Advantage (FRC 6328)'s lesson-deck ([`mechacoder-test`](../mechacoder-test)) — it's being built outward from there ever since.  So this is very much inspired by, and honestly borrowing generously from, their approach.

The bigger idea this feeds: a fuller self-paced Java/WPILib learning platform — real lessons and
exercises, plus (the actual motivating piece) an in-browser inline code editor with real
code-execution checking against a remote server, so a learner gets immediate feedback instead of
just reading slides. That execution/editor/hosting side isn't built yet — still very much in the
laying-down-ideas-and-planning stage. This repo is just the curriculum-*content* slice of that
bigger idea: combining Team 6328's existing lesson structure with real AP CS A content and other
sources into a fuller, sourced outline, ready for an eventual lesson-writing pass.

## The four repos

1. **[mechacoder-test](../mechacoder-test)** — Team 6328's existing static slide-deck app
   (`java-1.js`/`java-2.js` and friends), the starting point/inspiration for all of this. Frozen:
   never edited directly from this project.
2. **[csawesome-2026](../csawesome-2026)** — verbatim capture of CSAwesome2 (AP CSA Java), the
   primary content source. Frozen except for corrections.
3. **shockwave-curriculum (this repo)** — combines Repo 1's existing structure with Repo 2's
   (and Repo 4's) captured content into a new, fuller outline and eventually real lesson/
   exercise/quiz content.
4. **[other-reference-repo](../other-reference-repo)** — verbatim captures of other external
   sources (Oracle's Java Tutorials, WPILib's docs, another FRC team's public training guide)
   for topics CSAwesome doesn't cover at all.

## What's here

- **`OUTLINE.md`** — the source of truth. A plain-text chapter/item tree of the entire combined
  curriculum, with CSA/ORACLE/WPILIB/T5817 citations on every item, plus the reasoning behind
  every structural decision (why something moved, was dropped, was merged, is still open).
- **`curriculum-ledger.html`** — a published, formatted view of the same structure (numbers,
  names, existing/new status, source citations only — no rationale/prose, that all lives in
  `OUTLINE.md`). Synced from `OUTLINE.md` one-way: edit the outline first, then mirror the
  change here and republish. See the top of `OUTLINE.md` for the full sync-workflow rule.

## Current stage (as of 2026-09-09, outline v11)

**Structure and sourcing, not yet content-authoring.** Concretely:

- The combined outline is at v11: 28 numbered chapters across Java 1, Java 2, and an
  Optional/Advanced Topics block, each item citing exactly where its real content will come from
  (CSA, Oracle, WPILib, Team 5817, AdvantageKit, java-design-patterns.com, or "existing deck
  slide").
- External sourcing is done for every chapter **except** Ch.14 (Why Design Patterns?) and Ch.26
  (Architecture Takeaways — DRY/YAGNI/SOLID), filed as "slide-only" rather than a blocking gap —
  checked against all 6 sources in use, none teach either as a dedicated lesson; not a problem to
  fix, just where they stand for now.
- Item 9.9 (Wrapper Classes) was dropped entirely (AP-exam-specific detail, redundant with an
  earlier item). A few small open questions remain (Ch.13 Common Gotchas likely needing real
  expansion once practice content exists, Ch.24's label possibly being misleading, final chapter
  naming scheme) — see `OUTLINE.md`'s "Open questions" section for the current list.
- **The actual content-authoring pass — turning all this captured, verbatim source material
  into original, FRC-geared lessons, exercises, and quizzes — has not started yet.** That's the
  next real phase once the outline settles further.

## Provenance & eventual open-sourcing

Every new lesson file built from this outline should carry a reference line back to its sources
— see `OUTLINE.md`'s "Provenance convention" section for the exact format. When this project
eventually goes open-source, full credit will go to every original source and inspiration —
Team 6328's own lesson deck, CSAwesome/Runestone, Oracle, WPILib, Team 5817, and any added
later — with Claude's role in the process documented transparently.
