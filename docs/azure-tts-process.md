# Azure Speech TTS — narration generation recipe

Confirmed working process for generating lesson narration audio (used for Ch.1). Reuse this directly for future chapters instead of re-deriving it.

## Azure resource details

- Resource name: `joechan-9338-resource`
- Resource group: `rg-joe.chan-6204`
- Region: `westus3`
- Kind: `AIServices`
- Voice used: `en-US-JennyNeural`

## What does NOT work

- Custom-domain endpoint (`https://joechan-9338-resource.cognitiveservices.azure.com/cognitiveservices/v1`) + AAD bearer token → **404**. Wrong path for the Speech service specifically — the custom-domain form only works for endpoints in the AI Services multi-service surface, not `cognitiveservices/v1` TTS.
- Region-based endpoint (`https://westus3.tts.speech.microsoft.com/cognitiveservices/v1`) + AAD bearer token (`az account get-access-token --resource https://cognitiveservices.azure.com`) → **401**. Right path, wrong auth type — this endpoint wants a subscription key, not an AAD token.

## What works

Region-based endpoint + `Ocp-Apim-Subscription-Key` header, fetched via the Azure CLI:

```bash
SPEECH_KEY=$(az cognitiveservices account keys list \
  --name joechan-9338-resource \
  --resource-group rg-joe.chan-6204 \
  --query key1 -o tsv)

curl -sS -X POST "https://westus3.tts.speech.microsoft.com/cognitiveservices/v1" \
  -H "Ocp-Apim-Subscription-Key: $SPEECH_KEY" \
  -H "Content-Type: application/ssml+xml" \
  -H "X-Microsoft-OutputFormat: audio-24khz-48kbitrate-mono-mp3" \
  -H "User-Agent: shockwave-curriculum-tts" \
  --data-binary @beat.ssml \
  -o beat.mp3
```

Result: **200 OK**, valid MP3.

## SSML body format

```xml
<speak version='1.0' xml:lang='en-US'>
  <voice xml:lang='en-US' name='en-US-JennyNeural'>
    <prosody rate='-8%'>Your narration text goes here.</prosody>
  </voice>
</speak>
```

The `<prosody rate='-8%'>` wrapper slows playback slightly — full-speed neural voices read a
touch fast for teaching narration. Adjust the percentage if it still feels off in either
direction.

## Writing narration text: never put literal symbols in it

**Never type a literal underscore, slash, or other symbol character in narration text —
always spell it out phonetically.** The TTS engine reads literal characters exactly as
written, not as a human would say them out loud.

This bit us once already: Ch.1's recap beat had `SCREAMING_SNAKE_CASE` and `//` typed
literally, and the voice read the underscore and slashes out loud between each word,
sounding robotic and wrong — even though a different beat earlier in the same file spelled
the same term out correctly (`SCREAMING SNAKE CASE`, `Two slashes`). The inconsistency is
what caused it: one beat got it right, the recap didn't, because the recap text was written
separately and the symbol snuck back in.

Before generating audio for a beat, check its narration text for:
- Underscores (`_`) → spell out `underscore`, or replace with a space if the whole term is
  meant to sound like separate words (`SCREAMING_SNAKE_CASE` → `SCREAMING SNAKE CASE`)
- Slashes (`//`, `/* */`) → spell out (`two slashes`, `slash-star, star-slash`)
- Braces, arrows, and other code symbols (`{`, `}`, `->`, `::`) → describe them in words
  (`curly brace`, `arrow`)
- Dots in code (`MyClass.java`) → spell out `dot` (`MyClass dot java`)

A quick `grep -n "_\|//\|/\*"` (or similar) over the narration JSON before synthesizing
catches most of these before they cost an extra round of audio generation.

## Acronyms: use SSML `<say-as>`, not space-separated letters

**Never spell out an acronym with spaces (`F R C`, `W P I`) to force letter-by-letter
pronunciation — it's unreliable.** It happened to work for `F R C` and `J V M`, but failed
for `W P I`: the engine read "P I" as the word "pi," so "W P I Lib" came out sounding like
"pilot" or "pi-lib," not "W-P-I Lib." Space-separation depends on the TTS engine's own
heuristics for run-together short tokens, and there's no way to know in advance which
acronyms it'll handle right.

The reliable fix is SSML's own tool for this exact problem:

```xml
<say-as interpret-as="characters">WPI</say-as> Lib
```

This explicitly tells the engine to spell out `WPI` letter by letter, no guessing involved.

**So: write narration text with the natural, plain-English acronym spelling** (`FRC`, `JVM`,
`WPILib` — never spaced), and apply the `say-as` wrapping only at synthesis time, automatically,
via a shared helper: [tools/tts_helpers.py](../tools/tts_helpers.py). It holds one
`ACRONYM_PATTERNS` list (currently `FRC`, `JVM`, `WPILib`) and a `build_ssml(text, voice, rate)`
function that wraps every known acronym before constructing the SSML envelope. Add a new
acronym by adding one line to that list — no narration text ever needs to change for it.
Import it into any per-chapter build/synth script rather than re-deriving this logic.

This also simplifies the JS side: since narration text stays in its natural, readable form
end to end, the caption display needs zero cleanup — no `.replace(/F R C/g, 'FRC')`-style
hacks in the beat-rendering code. (An earlier version of this file did exactly that, precisely
because the source text had been manually space-separated — that whole category of hack goes
away once acronym-wrapping happens only at the synthesis boundary.)

## Beat-to-beat pause timing (in the player's JS, not the audio itself)

Every narrated-lesson page pauses briefly between beats rather than snapping straight to the
next one — three tiers, all in the shared `template_logic.js` (and copied into each already-
built lesson's own `<script>` block, since each page is a standalone file):

- **`CONTINUATION_PAUSE_MS`** (350ms) — used when the next beat is marked `continues: true`,
  i.e. it's revealing one more item in the same list or building up the same code block one
  line at a time (the four "why FRC" bullets, a class gaining a method beat by beat). Fast,
  because it's one continuous thought.
- **`BIG_PAUSE_MS`** (800ms) — the default, for a genuine topic change.
- **Code-reading bonus** — on top of `BIG_PAUSE_MS`, `codeReadingExtraMs()` scans the beat
  that just finished narrating for `<pre class="code">` blocks, counts their (tag-stripped)
  characters, and adds roughly 12ms per character, capped at `CODE_READING_MS_CAP` (2500ms) so
  a huge class doesn't force a silly-long wait. A beat with no code gets zero bonus. This
  exists so a reader gets a moment to actually look at a code sample before the page moves on,
  without relying on them to know to hit Space to pause manually (which still works too, and
  is the answer whenever a reader wants *more* time than any fixed default gives them).

Mark a beat `continues: true` only when it's genuinely a continuation of the immediately
prior one (same list, same code block being built up) — everything else should get the full
topic-change treatment, code bonus included.

## Building a new chapter: use `narrated-lessons/_build/`, not a one-off script

The bash `curl` loop shown earlier in this doc is the underlying API call, still correct, but
by Ch.25 that had grown into scattered one-off Python scripts per lesson — hard to redo or
audit. `narrated-lessons/_build/` is the cleaned-up, reusable version of that same pipeline:

- **`_build/template_prefix.html`** — the shared static markup (player chrome, CSS, CC
  button) every narrated lesson is built from.
- **`_build/template_logic.js`** — the shared playback JS (pause tiers, code-reading bonus,
  CC toggle, keyboard shortcuts) — see the pause-timing section above. Fix a bug or tune a
  constant here once and it's ready to apply to the next chapter you build.
- **`_build/builder.py`** — `build_lesson(page_title, playerbar_title, beats, voice,
  audio_dir, html_out_path)`: synthesizes audio for every beat (via Azure, with the acronym
  `say-as` wrapping baked in — see above) and assembles the final standalone HTML from the
  two templates.
- **`_build/ch25/lesson_25_1.py` … `lesson_25_7.py`** — the actual per-lesson content: a
  `BEATS` list of `{screen, speak, continues}` dicts, one per lesson. This is the real
  "source" for a narrated lesson — the built HTML is a compiled artifact of it, the same
  relationship `lessons/*.md` has to `review/*.html`. Editing a lesson later means editing
  this file and rebuilding, not hand-patching the giant built HTML.

To build a new chapter: write `_build/chNN/lesson_NN_M.py` (copy an existing `ch25` file as a
starting template), then:

```python
import sys
sys.path.insert(0, 'narrated-lessons/_build')
sys.path.insert(0, 'narrated-lessons/_build/chNN')
from builder import build_lesson
import lesson_NN_M

build_lesson(
    page_title='...',
    playerbar_title='...',
    beats=lesson_NN_M.BEATS,
    voice='en-US-RyanMultilingualNeural',  # or whichever voice this chapter uses
    audio_dir='narrated-lessons/chNN-audio/NN.M',
    html_out_path='narrated-lessons/chNN-.../NN.M-narrated-lesson.html',
)
```

Then run the two checkers (`tools/check_lesson_review_consistency.py` and
`tools/check_script_code.py`) before publishing — see
[lesson-review-consistency.md](lesson-review-consistency.md).

**Known gap:** Ch.1 predates this system and doesn't have an equivalent `lesson_1_2.py` —
only `_build/ch01/narration.json` (just the narration text, not the beat screens). If Ch.1
needs another full rebuild, it's worth writing a proper `lesson_1_2.py` for it first rather
than hand-patching the built HTML again.

Timing: a chapter's worth of beats (7-12 per lesson) synthesizes in well under a minute —
fast enough that there's no need to route it through an MCP agent or any async job.

## Wiring audio into the narrated-lesson artifact

The Claude Artifact asset store (`upload_asset`) does **not** accept bare audio formats (`.mp3` is rejected — whitelist is `png, jpg, jpeg, gif, webp, svg, mp4, webm, pdf, woff2, woff, ttf, otf, csv, md, markdown, json, txt`).

Working approach instead: base64-encode each mp3 and embed as a `data:audio/mpeg;base64,...` string directly in the page's JS, played through a single `<audio>` element (`.src` swapped per beat, advance-on-`ended`). ~1MB of raw audio becomes ~1.4MB of base64 — well under the 16MB artifact size cap.

```python
import base64
with open('beat-01.mp3', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('ascii')
data_uri = f"data:audio/mpeg;base64,{b64}"
```
