"""Make the "Listen" recording for each blog post (Butch, 2026-11-15: a natural male voice, Voice 1).

Voice: Kokoro (open-source, Apache 2.0), voice "am_michael", run on this computer, so no paid service.
Each post becomes static/audio/<slug>.mp3 plus static/audio/<slug>.json with the time each paragraph
starts (the page uses it to highlight the paragraph being read). A post is only redone when its words change.

Usage (needs:  pip install kokoro-onnx soundfile  and ffmpeg, plus the two model files from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 in KOKORO_DIR):
    python audio.py                 every post and Study Note that has no recording yet, or whose words changed
    python audio.py <slug> ...      only these posts (a Study Note by its slug or note-<slug>)
The site works without them: a post with no recording uses the phone's own voice instead.
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

VOICE = "am_michael"  # blog posts
NOTE_VOICE = "bm_george"  # Study Notes: Butch picked "Voice 4", a British male voice, from 6 samples (2026-11-28)
SPEED = 1.0
OUT = Path(__file__).parent / "static" / "audio"
GAP = {"title": 0.9, "h": 0.55, "p": 0.45}  # seconds of quiet after each kind of part
LEAD_IN = 0.55  # quiet before a heading, so it sounds like a new section


def is_note(b):
    return "practice" in b  # a Study Note (notes.py), not a blog post


def name(b):
    """File name of the recording: blog posts by slug, Study Notes as note-<slug> (so the two never clash)."""
    return ("note-" if is_note(b) else "") + b["slug"]


def note_parts(n):
    """What is read aloud on a Study Note (Butch 2026-11-28: the same voice as the blog), in page order:
    title, summary, the body (each list item and table row on its own), then the worked example.
    Not read: the "Last checked" line, the blog link, the practice quiz, laws cited and the disclaimer."""
    out = [("title", n["title"]), ("p", n["summary"])]
    for x in n["body"]:
        if isinstance(x, str):
            out.append(("p", x))
        elif x[0] == "h":
            out.append(("h", x[1]))
        elif x[0] == "list":
            out += [("p", y) for y in x[1]]
        elif x[0] == "tip":
            out.append(("p", "Tip: " + x[1]))
        elif x[0] == "table":
            out += [("p", f"{row[0]}. {row[1]}") for row in x[2]]
    ex_title, steps, answer = n["example"]
    out.append(("h", ex_title))
    out += [("p", s) for s in steps]
    out.append(("p", "Answer: " + answer))
    return out


def parts(b):
    """What is read aloud, in page order, as (kind, text). Must match the parts the page highlights:
    title, summary, then paragraphs, headings, quotes and points (no photos, sources, buttons, Email me)."""
    if is_note(b):
        return note_parts(b)
    out = [("title", b["title"])]
    if b.get("summary"):
        out.append(("p", b["summary"]))
    for x in b["body"]:
        if isinstance(x, str):
            out.append(("p", x))
        elif x[0] == "h":
            out.append(("h", x[1]))
        elif x[0] == "quote":
            out.append(("p", x[1]))
        elif x[0] == "point":
            out.append(("p", f"{x[1]}. {x[2]}"))
    return out


_DIG = "zero one two three four five six seven eight nine".split()
_TEENS = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()


def _two(a):
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if a < 10:
        return "oh " + _DIG[a]
    return _TEENS[a - 10] if a < 20 else tens[a // 10] + ("-" + _DIG[a % 10] if a % 10 else "")


def ra_words(n):
    """How Butch reads law numbers (2026-11-15): RA 7160 -> "Ar Eh seventy-one sixty" (two pairs);
    RA 12010 -> "Ar Eh twelve zero one zero" (first two digits as a number, the rest digit by digit)."""
    if len(n) == 4:
        return _two(int(n[:2])) + " " + _two(int(n[2:]))
    return _two(int(n[:2])) + " " + " ".join(_DIG[int(d)] for d in n[2:])


def year_words(n):
    """How a year is said (Butch 2026-11-27): 1776 -> "seventeen seventy-six", 1905 -> "nineteen oh five",
    1900 -> "nineteen hundred", 2000 -> "two thousand", 2005 -> "two thousand five", 2024 -> "twenty twenty-four"."""
    y = int(n)
    if 2000 <= y <= 2009:
        return "two thousand" + (" " + _DIG[y - 2000] if y > 2000 else "")
    hi, lo = divmod(y, 100)
    return _two(hi) + " " + ("hundred" if lo == 0 else _two(lo))


def spoken(text):
    """Small fixes so the voice reads the way a person would."""
    s = text
    s = re.sub(r"\b(1[1-9]\d\d|20\d\d)[-–](1[1-9]\d\d|20\d\d)\b", r"\1 to \2", s)  # 2023-2024
    s = re.sub(r"₱\s?([\d,]+(?:\.\d+)?)(\s?(?:million|billion|thousand))?", lambda m: m.group(1) + (m.group(2) or "") + " pesos", s)
    s = s.replace("₱", "pesos ")
    s = re.sub(r"\bNos\.\s*(?=\d)", "Numbers ", s)  # "Republic Act No. 7160" -> "Republic Act Number 7160" (Butch, 2026-11-15)
    s = re.sub(r"\bNo\.\s*(?=\d)", "Number ", s)
    s = re.sub(r"\b(Republic Act Numbers?|RA|R\.A\.)\s*(\d{4,5})\b",
               lambda m: ("Ar Eh" if m.group(1) in ("RA", "R.A.") else m.group(1)) + " " + ra_words(m.group(2)), s)
    # Butch 2026-11-27: RA is said as the letters "Ar Eh" with no pause (he picked this from 3 samples).
    # "R A" made this voice say "Ar uh"; the spelling "Ar Eh" gives the right sound.
    s = re.sub(r"\bR\.?A(?:'s|s)(?=\W|$)", "Ar Eh's", s)
    s = re.sub(r"\bR\.A\.|\bRA\b", "Ar Eh", s)
    s = re.sub(r"\bCRAA[FP](s?)\b", r"Cra-ap\1", s)  # Butch 2026-11-15: CRAAF/CRAAP read "Cra-ap"
    s = re.sub(r"\bRAAF(s?)\b", r"Ra-ap\1", s)  # Butch 2026-11-15: RAAF read "Ra-ap"
    # Butch 2026-11-24: Filipino "ng" (Bangko Sentral ng Pilipinas) is said "nang", not "N G".
    # Voice only; the page keeps the correct spelling "ng". "nahng" makes this voice say the Filipino "nang".
    s = re.sub(r"\bng\b", "nahng", s)
    # Butch 2026-11-27: COA (Commission on Audit) is said "KO-wa", the way Filipinos say it. "kohwa" makes this voice say it.
    s = re.sub(r"\bCOA(?:'s|s)\b", "kohwa's", s)
    s = re.sub(r"\bCOA\b", "kohwa", s)
    # Butch 2026-11-28: ".dev" is said "dot dev", ".com" "dot com", ".org" "dot org" (aumahinay.dev -> "aumahinay dot dev").
    # Without this the voice drops the dot and says only "dev".
    s = re.sub(r"(?<=\w)\.(dev|com|org)\b", lambda m: " dot " + m.group(1).lower(), s, flags=re.I)
    s = re.sub(r"(?<![\w.])\.(dev|com|org)\b", lambda m: "dot " + m.group(1).lower(), s, flags=re.I)
    s = re.sub(r"\be\.g\.,?", "for example,", s)
    s = re.sub(r"\bi\.e\.,?", "that is,", s)
    s = re.sub(r"\bvs\.?(?=\s)", "versus", s)
    s = re.sub(r"\s*[—–]\s*", ", ", s)  # dashes become a short pause
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    s = s.replace("/", " / ") if re.search(r"\w/\w", s) and "http" not in s else s
    # Years (1100-2099, four digits, no comma) are said like years, not "one thousand seven hundred ...".
    # Not money ("1500 pesos"), not a number in a list of IDs ("Number 1776"), not part of a longer number.
    s = re.sub(r"(?<![\d,.₱/-])(?<!Number )(?<!Numbers )\b(1[1-9]\d\d|20\d\d)\b(?![\d,]\d|\.\d| pesos)",
               lambda m: year_words(m.group(1)), s)
    return re.sub(r"\s+", " ", s).strip()


def voice_of(b):
    """(voice, accent) for a post or note."""
    return (NOTE_VOICE, "en-gb") if is_note(b) else (VOICE, "en-us")


def say(kokoro, text, b):
    voice, lang = voice_of(b)
    if lang == "en-us":
        return kokoro.create(text, voice=voice, speed=SPEED, lang=lang)
    # The British accent links an "r" into "Cra-ap"/"Ra-ap" (CRAAF, RAAF), making "Crar-ap"; take it out.
    ph = re.sub(r"ɑːɹ(\s?)ˈap", "ɑːˈap", kokoro.tokenizer.phonemize(text, lang))
    return kokoro.create(ph, voice=voice, speed=SPEED, lang=lang, is_phonemes=True)


def words_hash(b):
    return hashlib.sha1(json.dumps([voice_of(b)[0], SPEED, [spoken(t) for _, t in parts(b)]]).encode()).hexdigest()[:12]


def make(b, kokoro):
    import numpy as np
    import soundfile as sf
    pieces, starts, at, rate = [], [], 0.0, 24000
    for i, (kind, text) in enumerate(parts(b)):
        if kind == "h" and i:
            pieces.append(np.zeros(int(LEAD_IN * rate), dtype="float32")); at += LEAD_IN
        starts.append(round(at, 2))
        audio, rate = say(kokoro, spoken(text), b)
        pieces += [audio.astype("float32"), np.zeros(int(GAP[kind] * rate), dtype="float32")]
        at += len(audio) / rate + GAP[kind]
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "a.wav"
        sf.write(wav, np.concatenate(pieces), rate)
        OUT.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-ac", "1", "-ar", "24000",
                        "-b:a", "40k", "-id3v2_version", "3", "-metadata", f"title={b['title']}",
                        "-metadata", "artist=Ambrosio “Butch” U. Mahinay", str(OUT / f"{name(b)}.mp3")], check=True)
    (OUT / f"{name(b)}.json").write_text(json.dumps({"hash": words_hash(b), "voice": voice_of(b)[0],
                                                       "duration": round(at, 1), "starts": starts}) + "\n")


def needs(b):
    j = OUT / f"{name(b)}.json"
    return not (OUT / f"{name(b)}.mp3").exists() or not j.exists() or json.loads(j.read_text())["hash"] != words_hash(b)


def main(slugs):
    from content import BLOG
    from notes import NOTES
    from kokoro_onnx import Kokoro
    d = Path(os.environ.get("KOKORO_DIR", "."))
    kokoro = Kokoro(str(d / "kokoro-v1.0.onnx"), str(d / "voices-v1.0.bin"))
    todo = [b for b in BLOG + NOTES if (b["slug"] in slugs or name(b) in slugs if slugs else needs(b))]
    for n, b in enumerate(todo, 1):
        print(f"[{n}/{len(todo)}] {name(b)}", flush=True)
        make(b, kokoro)


if __name__ == "__main__":
    main(sys.argv[1:])
