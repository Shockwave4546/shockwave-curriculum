# Kokoro (local) TTS — narration generation recipe

Confirmed working process for generating lesson narration audio locally, via HyperFrames'
bundled Kokoro-82M model — free, offline, no API key, no per-character cost. Chosen for
Ch.2 onward after a direct A/B test against the existing Azure pipeline
([azure-tts-process.md](azure-tts-process.md)) on Ch.1's own script. Ch.1 and Ch.25 stay
on Azure since they're already built — this is for everything built from here forward.

## Setup

- **CLI:** `@hyperframes/cli` (sibling repo `~/dev/hyperframes-test/packages/cli`, its own
  monorepo — not an npm-installed dependency of this repo). Run via
  `node packages/cli/bin/hyperframes.mjs tts ...` from that repo, or `npx hyperframes tts`
  if a global/project install exists.
- **Python backend:** the CLI shells out to a local Python venv for the actual model
  (`kokoro-onnx` + `soundfile`, approved and installed 2026-09-22). Existing venv:
  `~/dev/tools/tts-kokoro-venv` — reuse this one; don't create a second one (a fresh venv
  hit a broken `espeakng-loader` data-path bug — see "Known environment gotcha" below).
  Point the CLI at it with `HYPERFRAMES_PYTHON=~/dev/tools/tts-kokoro-venv/bin/python`.
- **Model + voice files:** cached at `~/.cache/hyperframes/tts/models/kokoro-v1.0.onnx` and
  `~/.cache/hyperframes/tts/voices/voices-v1.0.bin` (54 voices total; only English ones are
  relevant here — prefix `a` = American English, `b` = British English).

```bash
HYPERFRAMES_PYTHON=~/dev/tools/tts-kokoro-venv/bin/python \
  node ~/dev/hyperframes-test/packages/cli/bin/hyperframes.mjs tts \
  "Your narration text." -o beat-01.wav -v am_adam --json
```

Output is `.wav` (not `.mp3` like Azure) — transcode with `ffmpeg -i in.wav -codec:a libmp3lame -b:a 64k out.mp3`
before embedding in a built lesson page, or the base64-embedded HTML balloons in size
(confirmed: one Ch.1-equivalent page was 23.6MB as raw wav vs. 3.2MB as mp3).

### Known environment gotcha

A freshly-created venv with the same `kokoro-onnx`/`espeakng-loader` versions failed with:
```
Speech synthesis failed
Error processing file '/home/runner/work/espeakng-loader/espeakng-loader/espeak-ng/_dynamic/share/espeak-ng-data/phontab': No such file or directory.
```
This is a hardcoded CI build path baked into the `espeakng-loader` wheel's compiled
library — not fixable via `ESPEAK_DATA_PATH` or any other env var, since the path is
compiled into the `.so`, not read at runtime. The existing `~/dev/tools/tts-kokoro-venv`
somehow avoided this (built at a different time/from a different wheel build). **Reuse
that venv rather than re-installing** until this is root-caused properly.

## No SSML — verified, not just untested

`kokoro-onnx`'s `Tokenizer.phonemize()` calls `phonemizer.phonemize(text, lang, preserve_punctuation=True, with_stress=True)`
directly — the `phonemizer-fork` package has zero SSML/markup-mode code anywhere in its
espeak backend (checked the source directly). Even espeak-ng's own `[[phoneme]]`
bracket-override syntax gets read as literal text through this path. There is no tag-based
pronunciation override available here, unlike Azure's `<say-as interpret-as="characters">`.

## Pronunciation pitfalls — found by testing `phonemizer.phonemize()` output directly

Kokoro's failure mode is the **opposite** of Azure's: Azure needed acronyms explicitly
*wrapped* to force letter-spelling; Kokoro's espeak-ng backend already spells out short,
unrecognized ALL-CAPS tokens *by default* — the risk is it mis-fires on ordinary code-style
words, and separately, on compound words its dictionary doesn't know.

| Text as written | Kokoro says | Fix |
|---|---|---|
| `Drivetrain` (one word) | "driver-train" — no dictionary entry, wrong rule-based guess | Write as two words: `Drive Train` |
| `MAX underscore SPEED` | "M-A-X underscore Speed" — short ALL-CAPS token spelled out | Drop to mixed case: `Max underscore Speed` |

**Already fine, no special handling needed:**
- `WPILib`, `FRC`, `JVM` — espeak's default heuristic already spells these out correctly
  (`WPILib` → "W-P-I Lib", etc.) with zero markup, unlike Azure which needed the SSML wrap.
- `SCREAMING SNAKE CASE` (three separate words) reads fine as three plain words — the
  letter-spelling heuristic only fires on *short* (~3-letter) all-caps tokens, not on
  longer recognized English words in all caps.
- `PI` reads as "pie" (the constant's actual spoken name), not spelled letter-by-letter —
  this is correct, not a bug.
- The word **"underscore"** being spoken aloud (e.g. in "Max underscore Speed") is
  **intentional**, not a Kokoro artifact — same convention as Azure: narration describes
  the literal constant name including its underscore. Cosmetically minor either way.

**Rule of thumb for narration text going forward:** write it in natural spoken case, not
code-matching case, for any short (~2-4 letter) all-caps fragment that isn't meant to be
spelled out; watch for compound/unusual words that might not have an espeak dictionary
entry, and split them into separate words if a synthesized test sounds wrong.

## Voice selection

Reviewed all 28 English voices (of 54 total — the rest are Spanish/French/Hindi/Italian/
Japanese/Portuguese/Mandarin) side by side, same test line including "FRC" so pronunciation
could be judged too. Shortlisted 6, confirmed by ear:

- **Female:** Jessica (`af_jessica`), Heart (`af_heart`), Emma (`bf_emma`)
- **Male:** Echo (`am_echo`), Puck (`am_puck`), Fable (`bm_fable`)

### Chapter assignment (2026-09-22)

One voice per chapter, kept consistent start-to-finish within that chapter — never
rotated mid-chapter. Rotated *across* chapters instead, alternating gender where possible.
A perfect alternation across all of Ch.1–28 isn't mathematically possible (Ch.1 is
female/Jenny, Ch.25 is male, 23 chapters apart — an odd distance forces exactly one
same-gender adjacency somewhere); that one adjacency was placed deliberately at the
Java I → Java II seam (Ch.13/14) rather than mid-track.

| Ch. | Voice | | Ch. | Voice |
|---|---|---|---|---|
| 1 | Jenny (Azure, existing — not re-recorded) | | 15 | Echo |
| 2 | Echo | | 16 | Heart |
| 3 | Jessica | | 17 | Puck |
| 4 | Puck | | 18 | Emma |
| 5 | Heart | | 19 | Fable |
| 6 | Fable | | 20 | Jessica |
| 7 | Emma | | 21 | Echo |
| 8 | Echo | | 22 | Heart |
| 9 | Jessica | | 23 | Puck |
| 10 | Puck | | 24 | Emma |
| 11 | Heart | | 25 | (Azure, existing, male — voice name never recorded, not re-built) |
| 12 | Fable | | 26 | Jessica |
| 13 | Emma | | 27 | Fable |
| 14 | Jessica *(deliberate same-gender pair, Java I/II boundary)* | | 28 | Heart |

Each voice lands 4-5 times across the 26 Kokoro-narrated chapters — reasonably balanced,
not a strict round-robin count.

## Everything else stays the same as Azure

Beat-to-beat pause timing, the `_build/template_prefix.html` / `template_logic.js` shared
templates (including the already-fixed body-flex-centering CSS bug), the code-verbatim
requirement checked by `tools/check_script_code.py`, and the base64-embedding approach for
wiring audio into the built HTML page are all unchanged — see
[azure-tts-process.md](azure-tts-process.md) for those, they're TTS-provider-agnostic.
Only the synthesis call itself (`builder.py`'s Azure `curl` request) needs a Kokoro
equivalent when a new chapter's build script is written.
