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
- **Nothing is pushed yet** (curriculum or academy). Narration HTML is ~214 MB plus 161 MB of mp3
  sources, over the Azure Static Web Apps Free-tier 250 MB cap once the app bundles it.
- **Hosting (owner decision, 2026-09-27; replaces the earlier "keep SWA Free, move narration to
  Azure storage" plan):** the academy app moves to DreamHost shared hosting at
  `academy.dovershockwave.org`, with a PHP + MySQL back end for accounts and progress. A test
  upload of the full site worked with no app code changes. See the academy repo's
  `docs/dreamhost-deployment.md` (and `docs/azure-deployment.md` for why, and what moving back
  to an Azure VM would cost).
- The academy's Azure Static Web Apps workflow no longer runs on push (automatic triggers
  disabled 2026-09-30), so pushing is safe: push curriculum, bump the academy submodule, push
  academy. Deploying to DreamHost is a manual `rsync` until a GitHub Actions deploy is built.
- Listen-through of the narration (pronunciation, e.g. "Pose2d"; the earlier "text cut off on
  screen" note).
