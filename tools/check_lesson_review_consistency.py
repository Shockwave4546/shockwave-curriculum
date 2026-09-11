#!/usr/bin/env python3
"""
Checks that lessons/chNN-*/N.N-*.md and review/chNN.html stay in sync.

review/chNN.html duplicates each lesson's content by hand (title, body HTML, pitfalls,
takeaways) inside a JS `DATA` object -- it is NOT generated from the markdown, so the two
can drift whenever one gets edited without the other. This script diffs them: heading
order, code blocks (byte-exact after stripping HTML/markdown formatting), pitfalls, and
takeaways.

Usage:
    python3 check_lesson_review_consistency.py <chapter-number>

Example:
    python3 check_lesson_review_consistency.py 25
    # checks lessons/ch25-command-based-programming/*.md against review/ch25.html

Run from the repo root (shockwave-curriculum/).
"""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from html import unescape


def strip_tags(s):
    # A tag starts with `<` immediately followed by `/` or a letter. Requiring that (instead
    # of bare `<[^>]+>`) keeps this from misreading a raw, unescaped `<`/`<=` operator left in
    # source code (e.g. `i < sensors.length`) as a tag opener and eating everything up to the
    # next real `>` -- a real bug that was producing false "differs" reports on ch04/05/07/09.
    s = re.sub(r'<(?:/|(?=[a-zA-Z]))[^>]*>', '', s)
    return unescape(s)


def normalize_code(s):
    return strip_tags(s).strip('\n')


def norm_text(s):
    # Strip markdown emphasis markers (**bold** and *italic*, one or two asterisks) and
    # backticks -- review.html's plain-text fields render as plain text, so lesson.md's
    # markdown syntax around a word is a formatting difference, not a content one.
    s = re.sub(r'\*\*?|`', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def parse_lesson_md(path):
    with open(path) as f:
        text = f.read()

    result = {"headings": [], "code_blocks": [], "pitfalls": [], "takeaways": []}

    all_headings = re.findall(r'^## (.+)$', text, re.MULTILINE)
    result["headings"] = [h for h in all_headings if h not in ("Common Pitfalls", "Key Takeaways")]

    result["code_blocks"] = re.findall(r'```(?:java|html|)\n(.*?)```', text, re.DOTALL)
    result["code_blocks"] = [c.strip('\n') for c in result["code_blocks"]]

    m = re.search(r'## Common Pitfalls\n(.*?)\n## ', text, re.DOTALL)
    if m:
        result["pitfalls"] = re.findall(r'^- (.+)$', m.group(1), re.MULTILINE)

    m = re.search(r'## Key Takeaways\n(.*?)(?:\nDerived from|\Z)', text, re.DOTALL)
    if m:
        result["takeaways"] = re.findall(r'^- (.+)$', m.group(1), re.MULTILINE)

    return result


def parse_review_item(item):
    """Handles two review.html schemas seen in this repo: a flat one (item.body/
    item.pitfalls/item.takeaways, e.g. ch25) and a nested one (item.lesson.body/
    item.lesson.pitfalls/item.lesson.takeaways, plus a sibling item.exercise, e.g. ch01)."""
    result = {"headings": [], "code_blocks": [], "pitfalls": [], "takeaways": []}

    source = item.get("lesson", item)

    body = source.get("body", "")
    result["headings"] = [strip_tags(h) for h in re.findall(r'<h2>(.*?)</h2>', body)]
    result["code_blocks"] = [normalize_code(c) for c in re.findall(r'<pre class="code"><code>(.*?)</code></pre>', body, re.DOTALL)]
    result["pitfalls"] = [strip_tags(p) for p in source.get("pitfalls", [])]
    result["takeaways"] = [strip_tags(t) for t in source.get("takeaways", [])]

    return result


def compare(lesson, review):
    issues = []

    lh = [norm_text(h) for h in lesson["headings"]]
    rh = [norm_text(h) for h in review["headings"]]
    if lh != rh:
        issues.append(f"HEADINGS differ:\n    lesson: {lh}\n    review: {rh}")

    lc = [norm_text(c) for c in lesson["code_blocks"]]
    rc = [norm_text(c) for c in review["code_blocks"]]
    if len(lc) != len(rc):
        issues.append(f"CODE BLOCK COUNT differs: lesson has {len(lc)}, review has {len(rc)}")
    else:
        for i, (a, b) in enumerate(zip(lc, rc)):
            if a != b:
                issues.append(f"CODE BLOCK #{i+1} differs:\n    lesson: {a[:200]}\n    review: {b[:200]}")

    for label, key in (("PITFALL", "pitfalls"), ("TAKEAWAY", "takeaways")):
        la = [norm_text(x) for x in lesson[key]]
        ra = [norm_text(x) for x in review[key]]
        if len(la) != len(ra):
            issues.append(f"{label}S COUNT differs: lesson has {len(la)}, review has {len(ra)}")
        else:
            # Full-string compare -- the previous 40-char-prefix check missed real drift
            # past that point (a systematic pattern: review dropped a clarifying example or
            # parenthetical past the first ~40 chars of many pitfalls/takeaways).
            for i, (a, b) in enumerate(zip(la, ra)):
                if a != b:
                    issues.append(f"{label} #{i+1} differs:\n    lesson: {a}\n    review: {b}")

    return issues


def find_data_object(html):
    """Finds `const DATA = { ... };` and returns the object literal text (braces included).

    A regex that lazily matches up to the first `\\n};` breaks on chapters whose lesson body
    embeds a code sample that itself ends a line with `};` (e.g. a Java 2D array literal, as
    in ch10/ch19) -- it stops at that fake end instead of the real one. This scans brace depth
    char-by-char instead, skipping over string/backtick literal contents so braces inside
    embedded HTML/code text don't get counted as structural.
    """
    marker = "const DATA = "
    start = html.find(marker)
    if start == -1 or html[start + len(marker)] != '{':
        return None

    i = start + len(marker)
    obj_start = i
    depth = 0
    in_string = None
    escaped = False
    for i in range(obj_start, len(html)):
        c = html[i]
        if in_string:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == in_string:
                in_string = None
        elif c in ('"', "'", '`'):
            in_string = c
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return html[obj_start:i + 1]
    return None


def extract_review_data(review_html_path):
    """Extracts the `const DATA = {...}` object literal from the review HTML and uses Node to
    evaluate it (it's a JS object literal with unquoted keys and template-literal backtick
    strings, not JSON, so it can't be parsed with json.loads directly)."""
    with open(review_html_path) as f:
        html = f.read()

    data_text = find_data_object(html)
    if data_text is None:
        print(f"DATA object not found in {review_html_path}", file=sys.stderr)
        sys.exit(1)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as tf:
        tf.write(f"const DATA = ({data_text});\nconsole.log(JSON.stringify(DATA));\n")
        temp_path = tf.name

    try:
        result = subprocess.run(["node", temp_path], capture_output=True, text=True)
    finally:
        os.unlink(temp_path)

    if result.returncode != 0:
        print(f"Failed to extract DATA from {review_html_path}: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    chapter_num = sys.argv[1]
    lessons_glob = glob.glob(f"lessons/ch{int(chapter_num):02d}-*/")
    if not lessons_glob:
        print(f"No lessons/ch{int(chapter_num):02d}-* directory found")
        sys.exit(1)
    lessons_dir = lessons_glob[0]
    review_html_path = f"review/ch{int(chapter_num):02d}.html"

    if not os.path.exists(review_html_path):
        print(f"No {review_html_path} found")
        sys.exit(1)

    review_data = extract_review_data(review_html_path)
    lesson_files = sorted(glob.glob(os.path.join(lessons_dir, "*.md")))

    total_issues = 0
    for lesson_file in lesson_files:
        basename = os.path.basename(lesson_file)
        # A filename can cover two combined lesson numbers (e.g. "8.1-8.2-constructors-and-
        # this.md" -> review key "8.1-8.2") -- split('-')[0] alone would only grab "8.1" and
        # falsely report the combined entry as missing from review DATA.
        m = re.match(r'^\d+\.\d+(?:-\d+\.\d+)?', basename)
        num = m.group(0) if m else basename.split('-')[0]

        lesson = parse_lesson_md(lesson_file)
        if num not in review_data:
            print(f"=== {num}: NOT FOUND in review DATA ===")
            total_issues += 1
            continue
        review = parse_review_item(review_data[num])

        issues = compare(lesson, review)
        if issues:
            print(f"=== {num}: {len(issues)} issue(s) ===")
            for issue in issues:
                print(f"  - {issue}")
            print()
            total_issues += len(issues)
        else:
            print(f"=== {num}: OK, no issues found ===")

    print(f"\nTOTAL ISSUES: {total_issues}")
    sys.exit(1 if total_issues else 0)


if __name__ == "__main__":
    main()
