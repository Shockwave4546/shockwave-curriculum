#!/usr/bin/env python3
"""
Checks that every code block in a lesson .md appears verbatim SOMEWHERE across a narrated
lesson's beats (screen HTML). Unlike lesson<->review, narrated lessons intentionally break
a lesson's code into incremental reveals across several beats (build up a class line by
line, etc.) instead of mirroring it 1:1 -- so this is a containment check, not a structural
diff: each lesson code block should appear, byte-exact once normalized, in at least one beat.

Usage:
    python3 check_script_code.py <lesson.md> <narrated-lesson.html>
"""
import re
import subprocess
import sys
from html import unescape


def strip_tags(s):
    return unescape(re.sub(r'<[^>]+>', '', s))


def norm(s):
    # strip backticks too: a lesson's code comment sometimes uses markdown-style
    # `this` backtick-emphasis for an identifier, which reads correctly as prose but
    # would be redundant punctuation once it's already inside a monospaced code block
    # in the narrated lesson -- not a real content gap, same treatment as
    # check_lesson_review_consistency.py's norm_text().
    s = re.sub(r'`', '', s)
    return re.sub(r'\s+', ' ', strip_tags(s)).strip()


def lesson_code_blocks(path):
    with open(path) as f:
        text = f.read()
    blocks = re.findall(r'```(?:java|html|)\n(.*?)```', text, re.DOTALL)
    return [b.strip('\n') for b in blocks]


def narrated_lesson_screens(path):
    """Extracts every beat's `screen` template-literal string via Node (same eval-on-
    trusted-own-file approach as check_lesson_review_consistency.py -- these are files this
    repo authored, never external input)."""
    result = subprocess.run(
        ["node", "-e", f"""
        const fs = require('fs');
        const html = fs.readFileSync('{path}', 'utf8');
        const m = html.match(/const BEATS = (\\[[\\s\\S]*?\\n\\]);/);
        if (!m) {{ console.error('BEATS array not found'); process.exit(1); }}
        // eval is safe here: this only ever runs against narrated-lesson HTML this repo
        // authored (never external/untrusted input); the BEATS array uses JS template-
        // literal backticks, so it isn't valid JSON and JSON.parse can't read it.
        const BEATS = eval(m[1]);
        console.log(JSON.stringify(BEATS.map(b => b.screen)));
        """],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Failed to extract BEATS from {path}: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    import json
    return json.loads(result.stdout)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    lesson_path, narrated_path = sys.argv[1], sys.argv[2]

    lesson_blocks = lesson_code_blocks(lesson_path)
    screens = narrated_lesson_screens(narrated_path)

    # concatenate all code found across all beat screens (each <pre class="code"><code>...)
    all_screen_code = []
    for screen in screens:
        all_screen_code.extend(re.findall(r'<pre class="code"[^>]*><code>(.*?)</code></pre>', screen, re.DOTALL))
    all_screen_code_norm = [norm(c) for c in all_screen_code]

    # a lesson block can legitimately be split across two adjacent beats (e.g. a class
    # with several methods, taught one method at a time) -- so also try each adjacent
    # pair concatenated before declaring a block missing.
    adjacent_pairs_norm = [
        all_screen_code_norm[i] + " " + all_screen_code_norm[i + 1]
        for i in range(len(all_screen_code_norm) - 1)
    ]

    missing = []
    for i, block in enumerate(lesson_blocks):
        block_norm = norm(block)
        if block_norm not in all_screen_code_norm and block_norm not in adjacent_pairs_norm:
            missing.append((i + 1, block))

    print(f"Lesson code blocks: {len(lesson_blocks)}")
    print(f"Narrated-lesson code snippets found: {len(all_screen_code_norm)}")
    if missing:
        print(f"\n{len(missing)} lesson code block(s) NOT found verbatim in the narrated lesson:")
        for num, block in missing:
            print(f"  --- lesson code block #{num} ---")
            print("  " + block.replace("\n", "\n  "))
    else:
        print("\nAll lesson code blocks found verbatim somewhere in the narrated lesson. OK.")

    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
