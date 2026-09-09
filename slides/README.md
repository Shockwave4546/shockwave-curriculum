# Slides

Teaser slides for the combined curriculum — the quick-intro layer, not the full lesson (that
lives in `../lessons/`). One subfolder per outline chapter, one file per item (or per chapter,
for chapters with no items).

## Two kinds of file in here

- **Existing** — pulled verbatim from `mechacoder-test`'s `java-1.js`/`java-2.js` (frozen, never
  edited directly; these are copies, not moves). Every file says exactly which slide index it
  came from.
- **New** — freshly authored teaser slides, in the same HTML/CSS-class format as the existing
  deck (see `mechacoder-test/LESSON_FORMAT.md` for the class vocabulary), for items the deck has
  no slide for at all.

## A real wrinkle: the deck's slides are coarser than the outline's items

Several existing deck slides cover more than one outline item at once — e.g. one "Control
Structures" slide covers both 5.1 (if Statements) and 5.2 (For Loops); one "Storing Data" slide
covers 9.1+9.2+9.3 (Arrays, ArrayList, HashMap) together. Rather than fake-split a single slide's
content across several files, these are captured as one file named with the full item range
(`5.1-5.2-if-statements-and-for-loops.md`), with a note explaining the combined coverage. This
matches the deck's actual granularity honestly instead of manufacturing a false 1:1 mapping.

One slide is also **relocated** rather than just copied: item 19.1 (Lambdas & Method References)
physically lives in `java-1.js`, but the outline moved it under Ch.19 (Interfaces) for the new
curriculum. The frozen deck file itself is untouched — only this copy's *placement* in the new
structure differs from where the slide physically sits in the old one.

## Status

All 27 **existing** items pulled as of 2026-09-09 (every chapter/item the deck already has a
slide for). **New** items (~45 total, marked `[new]` in `OUTLINE.md`): Ch.2's 4 new items (2.2,
2.3, 2.4, 2.5) authored as a format/tone pilot — everything else still pending, chapter by
chapter, once the pilot's format is confirmed.
