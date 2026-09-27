# Content audit (Sept 2026)

| File | What it is |
|---|---|
| `tracker.md` | Every Phase-1 finding (533) with status, plus the owner decisions table. All closed. |
| `fix-brief.md` | The binding rules the Phase-2 fix agents followed (targets, conventions, coverage placement). |
| `ch25-v3-outline.md` | Plan used to rewrite Ch.25 for Commands v3. |

## Outcome (2026-09-27)
- All 533 issues closed (fixed, already fixed, or won't-fix with a reason) across Ch.1-28:
  lessons, worked examples, exercises, narration scripts and `review/` pages.
- New lessons: **5.12** `switch` Statements and Expressions, **17.5** Abstract Classes and Methods.
- Ch.25 rewritten for **Commands v3** / WPILib 2027, incl. a "Reading Commands v2 code" section.
- Targets now in force are summarised in `docs/exercise-authoring-conventions.md`
  ("2026-09 content audit — conventions now in force").
- All 80 narrated lessons rebuilt with Kokoro and verified (titles, beat/audio counts, on-screen
  code verbatim with the lesson). Ch.1 re-voiced `af_heart`, Ch.25 `am_echo`.

## Still to do (next session)
- **Nothing is pushed yet** (curriculum or academy). Narration HTML is ~223 MB plus mp3 sources,
  over the Azure Static Web Apps Free-tier 250 MB cap once the app bundles it.
- **Storage decoupling** (owner decision): keep the front end on SWA Free, move narrated-lesson
  assets to paid Azure storage, and change the app to load them from there; upgrade the front end
  only if performance requires it. Then push curriculum, bump the academy submodule, push academy.
- The academy's local submodule checkout currently points at the new curriculum commit for
  local preview only — **do not commit that pointer** until the storage work is done.
- Listen-through of the narration (pronunciation, e.g. "Pose2d"; the earlier "text cut off on
  screen" note).
