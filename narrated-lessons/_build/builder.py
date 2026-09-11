import base64
import json
import os
import subprocess

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
ENDPOINT = "https://westus3.tts.speech.microsoft.com/cognitiveservices/v1"
RATE = "-8%"


def get_speech_key():
    return subprocess.run(
        ["az", "cognitiveservices", "account", "keys", "list",
         "--name", "joechan-9338-resource",
         "--resource-group", "rg-joe.chan-6204",
         "--query", "key1", "-o", "tsv"],
        capture_output=True, text=True, check=True
    ).stdout.strip()


def synth(text, voice, outfile, speech_key):
    ssml = (
        "<speak version='1.0' xml:lang='en-US'>"
        f"<voice xml:lang='en-US' name='{voice}'>"
        f"<prosody rate='{RATE}'>{text}</prosody>"
        "</voice>"
        "</speak>"
    )
    ssml_path = outfile + ".ssml.tmp"
    with open(ssml_path, "w", encoding="utf-8") as f:
        f.write(ssml)

    result = subprocess.run(
        ["curl", "-sS", "-X", "POST", ENDPOINT,
         "-H", f"Ocp-Apim-Subscription-Key: {speech_key}",
         "-H", "Content-Type: application/ssml+xml",
         "-H", "X-Microsoft-OutputFormat: audio-24khz-48kbitrate-mono-mp3",
         "-H", "User-Agent: shockwave-curriculum-tts",
         "--data-binary", f"@{ssml_path}",
         "-o", outfile,
         "-w", "%{http_code}"],
        capture_output=True, text=True
    )
    os.remove(ssml_path)
    status = result.stdout.strip()
    if status != "200":
        with open(outfile, "r", errors="replace") as f:
            body = f.read()
        print(f"FAILED ({status}): {outfile}\n{body}")
        return False
    size = os.path.getsize(outfile)
    print(f"OK: {outfile} ({size} bytes, ~{size*8/48000:.1f}s)")
    return True


def build_lesson(page_title, playerbar_title, beats, voice, audio_dir, html_out_path, audio_prefix="beat"):
    """
    beats: list of dicts {screen: str, speak: str, continues: bool (optional)}
    """
    os.makedirs(audio_dir, exist_ok=True)
    speech_key = get_speech_key()

    # 1. Generate audio for each beat
    audio_files = []
    for i, beat in enumerate(beats, start=1):
        outfile = os.path.join(audio_dir, f"{audio_prefix}-{i:02d}.mp3")
        synth(beat["speak"], voice, outfile, speech_key)
        audio_files.append(outfile)

    # 2. Base64-encode audio
    audio_b64 = []
    for f in audio_files:
        with open(f, "rb") as fh:
            audio_b64.append(base64.b64encode(fh.read()).decode("ascii"))

    # 3. Build BEATS JS array
    beats_entries = []
    for beat in beats:
        cont = ", continues: true" if beat.get("continues") else ""
        beats_entries.append(
            f'  {{ screen: `{beat["screen"]}`,\n    speak: {json.dumps(beat["speak"])}{cont} }}'
        )
    beats_js = "const BEATS = [\n" + ",\n".join(beats_entries) + "\n];\n"

    # 4. Build AUDIO JS array
    audio_js = "const AUDIO = [\n" + ",\n".join(f'"data:audio/mpeg;base64,{b}"' for b in audio_b64) + "\n];\n"

    # 5. Load templates
    with open(os.path.join(TEMPLATE_DIR, "template_prefix.html")) as f:
        prefix = f.read()
    with open(os.path.join(TEMPLATE_DIR, "template_logic.js")) as f:
        logic = f.read()

    prefix = prefix.replace("{{PAGE_TITLE}}", page_title)
    prefix = prefix.replace("{{PLAYERBAR_TITLE}}", playerbar_title)
    prefix = prefix.replace("{{TOTAL_BEATS}}", str(len(beats)))

    html = (
        prefix
        + "<script>\n" + audio_js + "</script>\n"
        + "<script>\n" + beats_js + "\n" + logic + "</script>\n"
    )

    with open(html_out_path, "w") as f:
        f.write(html)

    print(f"Built {html_out_path} ({len(beats)} beats, {len(html)} bytes)")
    return html_out_path
