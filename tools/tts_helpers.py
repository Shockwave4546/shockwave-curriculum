"""
Shared TTS synthesis helpers. Single source of truth for the acronym-pronunciation rule:

Space-separated letters (e.g. "F R C", "W P I") are NOT a reliable way to force a TTS
engine to spell out an acronym letter-by-letter -- it depends on the engine's own heuristics,
and can silently fail (e.g. "W P I" got read as something close to "pilot", because "P I"
looks like the word "pi" to the model). The correct, reliable tool is SSML's own
<say-as interpret-as="characters">TOKEN</say-as> tag, which explicitly tells the engine to
spell out TOKEN letter by letter, with the whole SSML env staying well-formed XML.

So: narration source text should ALWAYS use the natural, plain-English acronym spelling
("FRC", "JVM", "WPILib", not "F R C" / "J V M" / "W P I Lib") -- this keeps captions correct
with zero cleanup needed. The acronym -> SSML wrapping happens automatically, only at
synthesis time, via wrap_acronyms_for_ssml() below.

Add a new acronym by adding one line to ACRONYM_PATTERNS.
"""
import re

ACRONYM_PATTERNS = [
    (re.compile(r'\bWPILib\b'), '<say-as interpret-as="characters">WPI</say-as> Lib'),
    (re.compile(r'\bFRC\b'), '<say-as interpret-as="characters">FRC</say-as>'),
    (re.compile(r'\bJVM\b'), '<say-as interpret-as="characters">JVM</say-as>'),
]


def wrap_acronyms_for_ssml(text):
    for pattern, replacement in ACRONYM_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def build_ssml(text, voice, rate="-8%"):
    ssml_text = wrap_acronyms_for_ssml(text)
    return (
        "<speak version='1.0' xml:lang='en-US'>"
        f"<voice xml:lang='en-US' name='{voice}'>"
        f"<prosody rate='{rate}'>{ssml_text}</prosody>"
        "</voice>"
        "</speak>"
    )
