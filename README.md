# Shockwave Curriculum

The authoring workspace (Repo 3 of 4) for a self-paced Java/WPILib learning platform for FRC
Team 6328. This is where new curriculum content actually gets combined and written — not a raw
source-material repo like the other two below, and not the existing app.

## The four repos

1. **[mechacoder-test](../mechacoder-test)** — the existing static slide-deck app (`java-1.js`/
   `java-2.js` and friends). Frozen: never edited directly from this project. Pushed to the
   team's GitHub org (`Shockwave4546/mechacoder-test`, private).
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

## Current stage (as of 2026-09-09, outline v9)

**Structure and sourcing, not yet content-authoring.** Concretely:

- The combined outline is stable-ish at v9: 28 numbered chapters across Java 1, Java 2, and an
  Optional/Advanced Topics block, each item citing exactly where its real content will come from
  (CSA, Oracle, WPILib, Team 5817, or "existing deck slide").
- External sourcing is done for every identified gap **except** Ch.14 (Why Design Patterns?)
  and Ch.26 (Architecture Takeaways — DRY/YAGNI/SOLID), which still need a source — likely
  original authorship rather than something borrowed, since neither WPILib nor Team 5817 teach
  those as named general principles.
- A few small open questions remain (item 9.9 as a drop candidate, Ch.13 Common Gotchas likely
  needing real expansion, Ch.24's label possibly being misleading, final chapter naming scheme)
  — see `OUTLINE.md`'s "Open questions" section for the full, current list.
- **The actual content-authoring pass — turning all this captured, verbatim source material
  into original, FRC-geared lessons, exercises, and quizzes — has not started yet.** That's the
  next real phase once the outline settles further.

## Provenance & eventual open-sourcing

Every new lesson file built from this outline should carry a reference line back to its sources
— see `OUTLINE.md`'s "Provenance convention" section for the exact format. When this project
eventually goes open-source, full credit will go to every original source (CSAwesome/Runestone,
Oracle, WPILib, Team 5817, and any added later), with Claude's role in the process documented
transparently.
