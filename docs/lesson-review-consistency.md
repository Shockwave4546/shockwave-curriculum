# Lesson / review consistency check

## Why these can drift

`review/chNN.html` is **not generated** from `lessons/chNN-*/N.N-*.md` — there is no build
step connecting them. The review page exists purely so the content is easy to read (the
lesson `.md` files embed raw HTML/CSS-class code blocks, which are hard to read as plain
markdown). Both files were originally authored together, in the same commit, with the same
content — but they're two independently-maintained copies from that point on. Any later
edit to one (a wording tweak, a rendering fix) does not propagate to the other.

This is a real, confirmed risk, not a hypothetical one — see "Full reconciliation" below:
a corpus-wide sweep found real drift in 16 of 28 chapters, including the two chapters
(Ch.1, Ch.25) previously believed fully clean.

## The check

`tools/check_lesson_review_consistency.py` diffs a chapter's lesson `.md` files against its
`review/chNN.html` `DATA` object. It compares, per lesson item:

- **Headings** (`## ...` in the `.md` vs `<h2>` in the review body) — excluding "Common
  Pitfalls" and "Key Takeaways", which are separate `DATA` fields in review, not body
  headings
- **Code blocks** — byte-exact after stripping markdown fences / HTML tags, in order
- **Pitfalls** and **Takeaways** — count, and a full exact text match (see "Checker bugs
  found and fixed" — this used to silently compare only the first 40 characters)

Run it from the repo root:

```bash
python3 tools/check_lesson_review_consistency.py 25
```

It exits non-zero if it finds anything, so it's safe to use in a check/CI step later if
wanted.

## Checker bugs found and fixed (2026-09-11)

Running this across every chapter (not just one at a time, as it had only ever been used
before) surfaced four real bugs in the checker itself, all now fixed:

1. **DATA-object extraction regex stopped early.** The old regex looked for the first
   `\n};` after `const DATA = {`. If a lesson's code sample itself contained a line ending
   in `};` (e.g. a Java array literal, as in Ch.10 and Ch.19), the regex matched that
   instead of the real end of the object — crashing the checker on those two chapters.
   Fixed by replacing the regex with a brace-depth scanner that skips over string/backtick
   content, so it always finds the true matching closing brace.
2. **`strip_tags` misread raw operators as HTML tags.** Its regex, `<[^>]+>`, strips
   anything between `<` and the next `>` — which also matches a raw, unescaped `<` or `<=`
   left in source code (e.g. `i < sensors.length`), eating everything up to the next real
   `>` and silently truncating the comparison text. This produced false "differs" reports
   on several chapters where review.html was actually correct. Fixed by requiring a tag to
   start with `<` followed immediately by `/` or a letter.
3. **Pitfall/takeaway comparison only checked the first 40 characters.** `a[:40] != b[:40]`
   masked most of the real drift in the corpus — reviews that kept a pitfall/takeaway's
   first sentence but dropped everything after it (a clarifying clause or example) read as
   identical. Fixed to a full-string compare, which is what actually surfaced the
   corpus-wide drift described below.
4. **Combined-lesson filenames were parsed wrong.** A lesson file covering two numbered
   lessons (e.g. `8.1-8.2-constructors-and-this.md`, keyed as `"8.1-8.2"` in review's
   `DATA`) was reduced to just `"8.1"` by naive `basename.split('-')[0]`, so the checker
   reported the combined entry as entirely missing from review — it wasn't; the lookup key
   was wrong. Fixed with a regex that keeps the full `N.N-N.N` prefix when present.

`norm_text` was also extended to strip single-`*` markdown italics (previously only `**`
bold was stripped) — Ch.1 and Ch.14 both use `*word*` emphasis in lesson `.md` prose that
renders as plain text in review's plain-string fields; that's a formatting difference, not
a content one.

## Full reconciliation (2026-09-11)

With all four bugs fixed, a sweep of all 28 chapters found 137 real issues across 16
chapters (05, 07, 09, 12, 15, 17–28) — overwhelmingly the same shape: a pitfall or takeaway
keeps its first sentence in review.html but drops a trailing clarifying clause or concrete
example present in the lesson `.md`. This pattern was present even in Ch.1 and Ch.25 (the
chapters this project had used as its "already verified" baseline), so it reads as a
systematic authoring habit for review.html, not a one-off mistake. Every flagged issue was
resolved by editing `review/chNN.html` to match the lesson `.md` verbatim (never the
reverse — `lessons/*.md` stays canonical). Chapters 9 and 25 additionally had missing whole
`<h2>` sections and code blocks (not just wording) that had to be re-added, not just
reworded. All 28 chapters now report `TOTAL ISSUES: 0`.

## Checking the narrated-lesson scripts too

`tools/check_lesson_review_consistency.py` only checks lesson vs. review — it does **not**
check narrated-lesson scripts (`narrated-lessons/`). That's a separate tool,
`tools/check_script_code.py`, because the comparison has to work differently: a narrated
lesson deliberately breaks a lesson's code into incremental reveals across several beats
(building a class up line by line, for example) instead of mirroring the lesson 1:1 the way
review does. A structural diff (same count, same order) would flag correct, intentional
pedagogy as a mismatch.

So instead it's a **containment check**: every code block in the lesson `.md` must appear,
byte-exact (after stripping HTML/markdown formatting), *somewhere* across the narrated
lesson's beats — it doesn't matter which beat, or whether it's split across several.

```bash
python3 tools/check_script_code.py <lesson.md> <narrated-lesson.html>
```

This tool shared the same `strip_tags` bug described above (bug #2) — fixed the same way,
same day.

Confirmed clean on Ch.1 (`1.2-...md` vs. `1.2-narrated-lesson.html`) and on all 7 of Ch.25's
lessons (`25.1-...md` through `25.7-...md` vs. their `25.N-narrated-lesson.html`): every
lesson code block is found verbatim in the built beats. Run after building or editing any
narrated lesson's beats.

Prose (pitfalls, takeaways, section coverage) is a deliberate exception, not an oversight:
narration beats are written as short, spoken-delivery paraphrases of a lesson's pitfalls and
takeaways on purpose (e.g. audio needs "this fights the entire declarative philosophy"
where the lesson's fuller prose reads "the goal is to describe *what* happens, and let the
scheduler handle *when*"). That's unrelated to the review.html drift pattern above — review
is supposed to mirror the lesson faithfully; narration is supposed to adapt it for spoken
delivery. Don't try to make narration prose pass a verbatim check; only its code blocks are
held to that standard.

## What "closely matching" means going forward

Per the intended structure: `lessons/*.md` is the canonical, text-based reference students
read and return to; `review/*.html` exists only to make that same content easier to read
during review, so it must match the lesson faithfully, not paraphrase or compress it;
narrated-lesson scripts (`narrated-lessons/`) must also stay closely matched to the lesson
content, especially verbatim on code examples — see
[azure-tts-process.md](azure-tts-process.md)'s note on spelling out TTS-unfriendly symbols,
which is a similar "don't silently diverge from the source" lesson learned the hard way on
Ch.1.
