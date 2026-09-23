import base64
import json
import os
import subprocess

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
HYPERFRAMES_CLI = os.path.expanduser("~/dev/hyperframes-test/packages/cli/bin/hyperframes.mjs")
KOKORO_VENV_PYTHON = os.path.expanduser("~/dev/tools/tts-kokoro-venv/bin/python")


def synth(text, voice, outfile_mp3):
    """Synthesizes one beat's speak text locally via Kokoro (no SSML, no cloud call,
    no acronym wrapping needed -- see docs/kokoro-tts-process.md for why). Kokoro writes
    .wav directly; transcode to .mp3 via ffmpeg to avoid the ~7x size bloat wav causes
    once base64-embedded (confirmed in the Ch.1 A/B test)."""
    wav_path = outfile_mp3.rsplit(".", 1)[0] + ".tmp.wav"
    result = subprocess.run(
        ["node", HYPERFRAMES_CLI, "tts", text, "-o", wav_path, "-v", voice, "--json"],
        env={**os.environ, "HYPERFRAMES_PYTHON": KOKORO_VENV_PYTHON},
        capture_output=True, text=True
    )
    try:
        status = json.loads(result.stdout.strip())
    except (json.JSONDecodeError, ValueError):
        status = {"ok": False}
    if not status.get("ok"):
        print(f"FAILED: {outfile_mp3}\n{result.stdout}\n{result.stderr}")
        if os.path.exists(wav_path):
            os.remove(wav_path)
        return False

    ffmpeg = subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", wav_path,
         "-codec:a", "libmp3lame", "-b:a", "64k", outfile_mp3],
        capture_output=True, text=True
    )
    os.remove(wav_path)
    if ffmpeg.returncode != 0:
        print(f"FFMPEG FAILED: {outfile_mp3}\n{ffmpeg.stderr}")
        return False

    size = os.path.getsize(outfile_mp3)
    print(f"OK: {outfile_mp3} ({size} bytes, ~{status.get('durationSeconds', 0):.1f}s)")
    return True


def build_lesson(page_title, playerbar_title, beats, voice, audio_dir, html_out_path, audio_prefix="beat"):
    """
    Same shape/output as narrated-lessons/_build/builder.py's build_lesson() (Azure) --
    the templates, BEATS/AUDIO JS assembly, and base64-embedding are TTS-provider-agnostic,
    only the synth step differs. beats: list of dicts {screen: str, speak: str, continues:
    bool (optional)}.
    """
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(html_out_path)), exist_ok=True)

    audio_files = []
    for i, beat in enumerate(beats, start=1):
        outfile = os.path.join(audio_dir, f"{audio_prefix}-{i:02d}.mp3")
        if os.path.exists(outfile) and os.path.getsize(outfile) > 0:
            print(f"CACHED: {outfile}")
        elif not synth(beat["speak"], voice, outfile):
            raise RuntimeError(f"synthesis failed for beat {i} in {html_out_path}")
        audio_files.append(outfile)

    audio_b64 = []
    for f in audio_files:
        with open(f, "rb") as fh:
            audio_b64.append(base64.b64encode(fh.read()).decode("ascii"))

    beats_entries = []
    for beat in beats:
        cont = ", continues: true" if beat.get("continues") else ""
        beats_entries.append(
            f'  {{ screen: `{beat["screen"]}`,\n    speak: {json.dumps(beat["speak"])}{cont} }}'
        )
    beats_js = "const BEATS = [\n" + ",\n".join(beats_entries) + "\n];\n"

    audio_js = "const AUDIO = [\n" + ",\n".join(f'"data:audio/mpeg;base64,{b}"' for b in audio_b64) + "\n];\n"

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
