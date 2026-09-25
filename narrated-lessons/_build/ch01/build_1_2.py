"""Rebuild Ch.1.2 without the "four reasons" intro (now owned by Ch.1.1).

Source of truth for screens/speech is the previously built 1.2 HTML plus
narration.json. Only the two new opening beats are synthesized; every other
beat reuses its existing mp3 unchanged so the voice can't drift.

Run from the repo root:  python3 narrated-lessons/_build/ch01/build_1_2.py
"""
import base64
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
from builder import TEMPLATE_DIR, get_speech_key, synth

ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
HTML_PATH = os.path.join(ROOT, 'narrated-lessons/ch01-why-java-for-frc/1.2-narrated-lesson.html')
AUDIO_DIR = os.path.join(ROOT, 'narrated-lessons/ch01-audio')
NARRATION = os.path.join(HERE, 'narration.json')
VOICE = 'en-US-JennyNeural'
PAGE_TITLE = 'Ch.1.2 — Intro to Algorithms, Programming and Compilers'
PLAYERBAR_TITLE = 'Ch.1.2 — Intro to Algorithms, Programming and Compilers'
DROP = 6  # old beats 1-6: title + "four reasons"

NEW_BEAT_1 = {
    "screen": """<div class="scr-title">
      <div class="scr-eyebrow">Ch. 1 &middot; Java Foundations</div>
      <h1>Intro to Algorithms, Programming and Compilers</h1>
      <p class="scr-sub">A live walkthrough &mdash; press play and follow along.</p>
    </div>""",
    "speak": "Welcome back. Now that you know why FRC teams use Java, let's get your very first Java program up and running.",
}
OLD_7_PREFIX = "Let's back up even further. What is an algorithm?"
NEW_7_PREFIX = "First, what is an algorithm?"


def parse_old_beats(html):
    body = html.split('const BEATS = [', 1)[1].split('\n];', 1)[0]
    pat = re.compile(r'\{ screen: `(.*?)`,\n    speak: ("(?:[^"\\]|\\.)*")(, continues: true)? \}', re.S)
    return [{"screen": s, "speak": json.loads(sp), "continues": bool(c)}
            for s, sp, c in pat.findall(body)]


def main():
    with open(HTML_PATH) as f:
        old = parse_old_beats(f.read())
    with open(NARRATION) as f:
        narration = json.load(f)
    assert len(old) == 23 == len(narration), (len(old), len(narration))
    assert all(b["speak"] == narration[f"{i:02d}"] for i, b in enumerate(old, 1))
    assert old[DROP]["speak"].startswith(OLD_7_PREFIX)

    beat2 = dict(old[DROP], speak=old[DROP]["speak"].replace(OLD_7_PREFIX, NEW_7_PREFIX, 1))
    beats = [NEW_BEAT_1, beat2] + old[DROP + 1:]
    kept_audio = [os.path.join(AUDIO_DIR, f"beat-{i:02d}.mp3") for i in range(DROP + 2, 24)]

    # Stage reused audio first, before any file in AUDIO_DIR is overwritten.
    staged = [open(p, 'rb').read() for p in kept_audio]

    key = get_speech_key()
    new_files = [os.path.join(AUDIO_DIR, f"beat-{i:02d}.mp3") for i in range(1, len(beats) + 1)]
    for i in (0, 1):
        if not synth(beats[i]["speak"], VOICE, new_files[i], key):
            sys.exit("synthesis failed; audio for beats 1-2 may be partial")
    for data, path in zip(staged, new_files[2:]):
        with open(path, 'wb') as f:
            f.write(data)
    for i in range(len(beats) + 1, 24):
        os.remove(os.path.join(AUDIO_DIR, f"beat-{i:02d}.mp3"))

    audio_b64 = [base64.b64encode(open(p, 'rb').read()).decode('ascii') for p in new_files]
    entries = []
    for b in beats:
        cont = ", continues: true" if b.get("continues") else ""
        entries.append(f'  {{ screen: `{b["screen"]}`,\n    speak: {json.dumps(b["speak"])}{cont} }}')
    beats_js = "const BEATS = [\n" + ",\n".join(entries) + "\n];\n"
    audio_js = "const AUDIO = [\n" + ",\n".join(f'"data:audio/mpeg;base64,{b}"' for b in audio_b64) + "\n];\n"

    with open(os.path.join(TEMPLATE_DIR, "template_prefix.html")) as f:
        prefix = f.read()
    with open(os.path.join(TEMPLATE_DIR, "template_logic.js")) as f:
        logic = f.read()
    prefix = (prefix.replace("{{PAGE_TITLE}}", PAGE_TITLE)
                    .replace("{{PLAYERBAR_TITLE}}", PLAYERBAR_TITLE)
                    .replace("{{TOTAL_BEATS}}", str(len(beats))))
    html = prefix + "<script>\n" + audio_js + "</script>\n<script>\n" + beats_js + "\n" + logic + "</script>\n"
    with open(HTML_PATH, 'w') as f:
        f.write(html)

    with open(NARRATION, 'w') as f:
        json.dump({f"{i:02d}": b["speak"] for i, b in enumerate(beats, 1)}, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Built {HTML_PATH} ({len(beats)} beats)")


if __name__ == '__main__':
    main()
