import sys
sys.path.insert(0, 'narrated-lessons/_build')
sys.path.insert(0, 'narrated-lessons/_build/ch01')
from builder import build_lesson
import lesson_1_1

build_lesson(
    page_title='Ch.1.1 — Why Java for FRC',
    playerbar_title='SHOCKWAVE CURRICULUM · Live · Ch.1 — Why Java for FRC',
    beats=lesson_1_1.BEATS,
    voice='en-US-JennyNeural',
    audio_dir='narrated-lessons/ch01-audio/1.1',
    html_out_path='narrated-lessons/ch01-why-java-for-frc/1.1-narrated-lesson.html',
)
