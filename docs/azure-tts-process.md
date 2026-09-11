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

## Reusable script pattern

Adapt this for a new chapter — swap `OUTDIR` and the list of `synth` calls at the bottom:

```bash
#!/bin/bash
set -e

OUTDIR="/home/cjoe/dev/shockwave-curriculum/narrated-lessons/chXX-audio"
ENDPOINT="https://westus3.tts.speech.microsoft.com/cognitiveservices/v1"
VOICE="en-US-JennyNeural"
mkdir -p "$OUTDIR"

SPEECH_KEY=$(az cognitiveservices account keys list --name joechan-9338-resource --resource-group rg-joe.chan-6204 --query key1 -o tsv)

synth() {
  local num="$1"
  local text="$2"
  local outfile="$OUTDIR/beat-$(printf '%02d' "$num").mp3"
  local ssmlfile="/tmp/beat-$(printf '%02d' "$num").ssml"

  cat > "$ssmlfile" << EOF
<speak version='1.0' xml:lang='en-US'>
  <voice xml:lang='en-US' name='$VOICE'>
    $text
  </voice>
</speak>
EOF

  local status
  status=$(curl -sS -X POST "$ENDPOINT" \
    -H "Ocp-Apim-Subscription-Key: $SPEECH_KEY" \
    -H "Content-Type: application/ssml+xml" \
    -H "X-Microsoft-OutputFormat: audio-24khz-48kbitrate-mono-mp3" \
    -H "User-Agent: shockwave-curriculum-tts" \
    --data-binary @"$ssmlfile" \
    -o "$outfile" \
    -w "%{http_code}")

  if [ "$status" == "200" ]; then
    echo "beat-$(printf '%02d' "$num").mp3: OK ($(stat -c%s "$outfile") bytes)"
  else
    echo "beat-$(printf '%02d' "$num").mp3: FAILED (HTTP $status)"
    cat "$outfile"
    echo
  fi
  rm -f "$ssmlfile"
}

synth 1 "First line of narration."
synth 2 "Second line of narration."
# ...one synth call per beat

echo "=== DONE ==="
ls -la "$OUTDIR"
```

Timing: all 17 Ch.1 clips generated in under a minute — this is fast, no need to route it through an MCP agent.

## Wiring audio into the narrated-lesson artifact

The Claude Artifact asset store (`upload_asset`) does **not** accept bare audio formats (`.mp3` is rejected — whitelist is `png, jpg, jpeg, gif, webp, svg, mp4, webm, pdf, woff2, woff, ttf, otf, csv, md, markdown, json, txt`).

Working approach instead: base64-encode each mp3 and embed as a `data:audio/mpeg;base64,...` string directly in the page's JS, played through a single `<audio>` element (`.src` swapped per beat, advance-on-`ended`). ~1MB of raw audio becomes ~1.4MB of base64 — well under the 16MB artifact size cap.

```python
import base64
with open('beat-01.mp3', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('ascii')
data_uri = f"data:audio/mpeg;base64,{b64}"
```
