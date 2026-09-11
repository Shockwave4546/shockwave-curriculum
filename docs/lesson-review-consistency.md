# Lesson / review consistency check

## Why these can drift

`review/chNN.html` is **not generated** from `lessons/chNN-*/N.N-*.md` — there is no build
step connecting them. The review page exists purely so the content is easy to read (the
lesson `.md` files embed raw HTML/CSS-class code blocks, which are hard to read as plain
markdown). Both files were originally authored together, in the same commit, with the same
content — but they're two independently-maintained copies from that point on. Any later
edit to one (a wording tweak, a rendering fix) does not propagate to the other.

This is a real, confirmed risk, not a hypothetical one: `review/ch25.html` was hand-edited
twice after its initial commit (fixing a quote-rendering bug in a code comment) without the
matching change ever landing in `lessons/ch25-command-based-programming/25.7-*.md` — see
`tools/check_lesson_review_consistency.py`'s Ch.25 findings below.

## The check

`tools/check_lesson_review_consistency.py` diffs a chapter's lesson `.md` files against its
`review/chNN.html` `DATA` object. It compares, per lesson item:

- **Headings** (`## ...` in the `.md` vs `<h2>` in the review body) — excluding "Common
  Pitfalls" and "Key Takeaways", which are separate `DATA` fields in review, not body
  headings
- **Code blocks** — byte-exact after stripping markdown fences / HTML tags, in order
- **Pitfalls** and **Takeaways** — count, and a loose text match

Run it from the repo root:

```bash
python3 tools/check_lesson_review_consistency.py 25
```

It exits non-zero if it finds anything, so it's safe to use in a check/CI step later if
wanted.

## Known findings (Ch.25, as of this check)

Three real issues, not false positives:

1. **25.2** — the lesson has 6 code blocks; review has only 3. Review compressed the
   Sequential/Parallel/Race composition examples into inline one-liners inside a bullet
   list instead of showing them as the lesson's three separate full code blocks — a real
   loss of detail in review vs. the lesson.
2. **25.6** — Takeaway #1 is trimmed in review: it drops the lesson's `(a button, a sensor,
   an arbitrary check)` parenthetical.
3. **25.7** — Code block #4 differs by a single detail: the lesson's comment reads
   `// implicitly requires this`; review reads `// implicitly requires 'this'`. Traced via
   `git log` to a deliberate one-off fix applied only to review.html (it was originally an
   italicized `<i>this</i>` tag that rendered oddly, fixed by quoting it instead) — the fix
   never made it back into the lesson `.md`.

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

Confirmed clean on Ch.1 (`1.2-intro-to-algorithms-programming-and-compilers.md` vs.
`1.2-narrated-lesson.html`): all 3 lesson code blocks found verbatim in the rebuilt beats.
This was the direct answer to "are narrated scripts checked, and should they be" — they
weren't, until this tool existed; now they can be, and should be run after building or
editing any narrated lesson's beats.

Prose (pitfalls, takeaways, section coverage) still needs a human pass — that part doesn't
reduce to an exact-match check the way code does.

## What "closely matching" means going forward

Per the intended structure: `lessons/*.md` is the canonical, text-based reference students
read and return to; `review/*.html` exists only to make that same content easier to read
during review, so it must match the lesson faithfully, not paraphrase or compress it;
narrated-lesson scripts (`narrated-lessons/`) must also stay closely matched to the lesson
content, especially verbatim on code examples — see
[azure-tts-process.md](azure-tts-process.md)'s note on spelling out TTS-unfriendly symbols,
which is a similar "don't silently diverge from the source" lesson learned the hard way on
Ch.1.
