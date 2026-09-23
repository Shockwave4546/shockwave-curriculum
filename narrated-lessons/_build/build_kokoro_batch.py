"""
Batch driver for Ch.2-13's Kokoro-narrated lessons. Deviates from the one-driver-per-lesson
convention (build_1_1.py etc.) on purpose -- 45 lessons would mean 45 near-identical
boilerplate files; a manifest-driven loop is more maintainable at this scale. Re-derives
each lesson's real itemNum from its actual lessons/*.md filename (not from the .py script's
own name) since that's what the live app's narratedUrl lookup keys off -- getting this
wrong would silently 404 in the app despite the file existing on disk.

Usage: python3 narrated-lessons/_build/build_kokoro_batch.py [--only 2,3] [--skip-existing]
"""
import argparse
import glob
import importlib.util
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kokoro_builder import build_lesson

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

CHAPTER_SLUGS = {
    2: 'ch02-variables-and-types', 3: 'ch03-apis-libraries-and-documentation',
    4: 'ch04-using-objects-and-calling-methods', 5: 'ch05-control-structures',
    6: 'ch06-strings', 7: 'ch07-the-class-blueprint', 8: 'ch08-constructors-and-this',
    9: 'ch09-storing-data', 10: 'ch10-2d-arrays', 11: 'ch11-enums-named-choices',
    12: 'ch12-exceptions-and-try-catch', 13: 'ch13-common-gotchas',
}

CHAPTER_NAMES = {
    2: 'Variables & Types', 3: 'APIs, Libraries & Documentation',
    4: 'Using Objects & Calling Methods', 5: 'Control Structures', 6: 'Strings',
    7: 'The Class Blueprint', 8: 'Constructors & "this"', 9: 'Storing Data',
    10: '2D Arrays', 11: 'Enums: Named Choices', 12: 'Exceptions & try/catch',
    13: 'Common Gotchas',
}

# One voice per chapter -- see docs/kokoro-tts-process.md for the full table/rationale.
CHAPTER_VOICES = {
    2: 'am_echo', 3: 'af_jessica', 4: 'am_puck', 5: 'af_heart', 6: 'bm_fable',
    7: 'bf_emma', 8: 'am_echo', 9: 'af_jessica', 10: 'am_puck', 11: 'af_heart',
    12: 'bm_fable', 13: 'bf_emma',
}


def item_num_from_filename(stem):
    m = re.match(r'^([\d.]+(?:-[\d.]+)?)-(.+)$', stem)
    if not m:
        raise ValueError(f"can't parse item number from {stem!r}")
    return m.group(1)


def lesson_title(md_path):
    with open(md_path) as f:
        first_line = f.readline().strip()
    return first_line.lstrip('#').strip()


def python_module_suffix(item_num):
    first_seg = item_num.split('-')[0]
    return first_seg.replace('.', '_') if '.' in first_seg else f'{first_seg}_1'


def import_beats(build_dir, chapter_num, module_suffix):
    module_path = os.path.join(build_dir, f'lesson_{chapter_num}_{module_suffix.split("_", 1)[1]}.py')
    spec = importlib.util.spec_from_file_location(f"lesson_mod_{chapter_num}_{module_suffix}", module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BEATS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--only', help='comma-separated chapter numbers, e.g. 2,3')
    parser.add_argument('--skip-existing', action='store_true')
    args = parser.parse_args()

    chapters = sorted(CHAPTER_SLUGS)
    if args.only:
        wanted = {int(x) for x in args.only.split(',')}
        chapters = [c for c in chapters if c in wanted]

    built, skipped, failed = 0, 0, []

    for ch in chapters:
        slug = CHAPTER_SLUGS[ch]
        voice = CHAPTER_VOICES[ch]
        lessons_dir = os.path.join(REPO_ROOT, 'lessons', slug)
        build_dir = os.path.join(REPO_ROOT, 'narrated-lessons', '_build', f'ch{ch:02d}')
        out_dir = os.path.join(REPO_ROOT, 'narrated-lessons', slug)
        audio_root = os.path.join(REPO_ROOT, 'narrated-lessons', f'ch{ch:02d}-audio')

        md_files = sorted(glob.glob(os.path.join(lessons_dir, '*.md')))
        for md_path in md_files:
            stem = os.path.splitext(os.path.basename(md_path))[0]
            item_num = item_num_from_filename(stem)
            title = lesson_title(md_path)
            suffix = python_module_suffix(item_num)

            html_out_path = os.path.join(out_dir, f'{item_num}-narrated-lesson.html')
            if args.skip_existing and os.path.exists(html_out_path):
                print(f"SKIP (exists): {html_out_path}")
                skipped += 1
                continue

            module_file = os.path.join(build_dir, f'lesson_{suffix}.py')
            if not os.path.exists(module_file):
                print(f"MISSING SCRIPT for {item_num} ({title}): expected {module_file}")
                failed.append((item_num, "missing script file"))
                continue

            spec = importlib.util.spec_from_file_location(f"lesson_mod_{ch}_{suffix}", module_file)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            beats = mod.BEATS

            audio_dir = os.path.join(audio_root, item_num)

            print(f"\n=== Ch.{item_num} — {title} (voice={voice}, {len(beats)} beats) ===")
            try:
                build_lesson(
                    page_title=f'Ch.{item_num} — {title}',
                    playerbar_title=f'SHOCKWAVE CURRICULUM · Live · Ch.{ch} — {CHAPTER_NAMES[ch]}',
                    beats=beats,
                    voice=voice,
                    audio_dir=audio_dir,
                    html_out_path=html_out_path,
                )
                built += 1
            except Exception as e:
                print(f"FAILED: {item_num}: {e}")
                failed.append((item_num, str(e)))

    print(f"\n\nDone. Built {built}, skipped {skipped}, failed {len(failed)}.")
    if failed:
        print("Failures:")
        for item_num, err in failed:
            print(f"  {item_num}: {err}")
        sys.exit(1)


if __name__ == '__main__':
    main()
