"""Make the "Listen" recording for each blog post (Butch, 2026-11-15: a natural male voice, Voice 1).

Voice: Kokoro (open-source, Apache 2.0), voice "am_michael", run on this computer, so no paid service.
Each post becomes static/audio/<slug>.mp3 plus static/audio/<slug>.json with the time each paragraph
starts (the page uses it to highlight the paragraph being read). A post is only redone when its words change.

Usage (needs:  pip install kokoro-onnx soundfile  and ffmpeg, plus the two model files from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 in KOKORO_DIR):
    python audio.py                 every post that has no recording yet, or whose words changed
    python audio.py <slug> ...      only these posts
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

VOICE = "am_michael"
SPEED = 1.0
OUT = Path(__file__).parent / "static" / "audio"
GAP = {"title": 0.9, "h": 0.55, "p": 0.45}  # seconds of quiet after each kind of part
LEAD_IN = 0.55  # quiet before a heading, so it sounds like a new section


def parts(b):
    """What is read aloud, in page order, as (kind, text). Must match the parts the page highlights:
    title, summary, then paragraphs, headings, quotes and points (no photos, sources, buttons, Email me)."""
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


def spoken(text):
    """Small fixes so the voice reads the way a person would."""
    s = text
    s = re.sub(r"₱\s?([\d,]+(?:\.\d+)?)(\s?(?:million|billion|thousand))?", lambda m: m.group(1) + (m.group(2) or "") + " pesos", s)
    s = s.replace("₱", "pesos ")
    s = re.sub(r"\bNos\.\s*(?=\d)", "Numbers ", s)  # "Republic Act No. 7160" -> "Republic Act Number 7160" (Butch, 2026-11-15)
    s = re.sub(r"\bNo\.\s*(?=\d)", "Number ", s)
    s = re.sub(r"\be\.g\.,?", "for example,", s)
    s = re.sub(r"\bi\.e\.,?", "that is,", s)
    s = re.sub(r"\bvs\.?(?=\s)", "versus", s)
    s = re.sub(r"\s*[—–]\s*", ", ", s)  # dashes become a short pause
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'")
    s = s.replace("/", " / ") if re.search(r"\w/\w", s) and "http" not in s else s
    return re.sub(r"\s+", " ", s).strip()


def words_hash(b):
    return hashlib.sha1(json.dumps([VOICE, SPEED, [spoken(t) for _, t in parts(b)]]).encode()).hexdigest()[:12]


def make(b, kokoro):
    import numpy as np
    import soundfile as sf
    pieces, starts, at, rate = [], [], 0.0, 24000
    for i, (kind, text) in enumerate(parts(b)):
        if kind == "h" and i:
            pieces.append(np.zeros(int(LEAD_IN * rate), dtype="float32")); at += LEAD_IN
        starts.append(round(at, 2))
        audio, rate = kokoro.create(spoken(text), voice=VOICE, speed=SPEED, lang="en-us")
        pieces += [audio.astype("float32"), np.zeros(int(GAP[kind] * rate), dtype="float32")]
        at += len(audio) / rate + GAP[kind]
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "a.wav"
        sf.write(wav, np.concatenate(pieces), rate)
        OUT.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-ac", "1", "-ar", "24000",
                        "-b:a", "40k", "-id3v2_version", "3", "-metadata", f"title={b['title']}",
                        "-metadata", "artist=Ambrosio “Butch” U. Mahinay", str(OUT / f"{b['slug']}.mp3")], check=True)
    (OUT / f"{b['slug']}.json").write_text(json.dumps({"hash": words_hash(b), "voice": VOICE,
                                                       "duration": round(at, 1), "starts": starts}) + "\n")


def needs(b):
    j = OUT / f"{b['slug']}.json"
    return not (OUT / f"{b['slug']}.mp3").exists() or not j.exists() or json.loads(j.read_text())["hash"] != words_hash(b)


def main(slugs):
    from content import BLOG
    from kokoro_onnx import Kokoro
    d = Path(os.environ.get("KOKORO_DIR", "."))
    kokoro = Kokoro(str(d / "kokoro-v1.0.onnx"), str(d / "voices-v1.0.bin"))
    todo = [b for b in BLOG if (b["slug"] in slugs if slugs else needs(b))]
    for n, b in enumerate(todo, 1):
        print(f"[{n}/{len(todo)}] {b['slug']}", flush=True)
        make(b, kokoro)


if __name__ == "__main__":
    main(sys.argv[1:])
