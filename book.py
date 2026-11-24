"""360° Accountability as web pages: one page per chapter, plus the glossary and the references
(Butch 2026-11-23: "All chapter now are open for adsense").

The text lives in book_text.json, taken from the 1st Edition PDF (October 2026) and then fact-checked
and proofread. The Preface and About the Author are left out (they name a municipality). Edit the JSON to
change the text; each block is one of:
  {"t": "h", "text": ...}                section heading
  {"t": "p", "r": RICH}                  paragraph
  {"t": "ul"|"ol", "items": [RICH, ...]} list
  {"t": "box", "label": ..., "r": RICH}  "In the treasury" / "In ALTOS" box
  {"t": "table", "head": [...], "rows": [[RICH, ...], ...]}
  {"t": "fig"}                           Figure 1.1 (static/altos-loop.png)
  {"t": "ref", "r": RICH}                one reference
RICH is a list of [style, text] runs, style "" (plain), "b" (bold) or "i" (italic).
"""
import json
from pathlib import Path

_DATA = json.loads((Path(__file__).parent / "book_text.json").read_text(encoding="utf-8"))

BOOK_BASE = "/book/"  # was /projects/altos-book/ until 2026-11-24 (no Projects menu any more); old links redirect

PARTS = [
    ("I", "Foundations", "The ALTOS principle and the theory behind it", range(1, 5)),
    ("II", "The Philippine Setting", "The fiscal state and the treasury as an institution", range(5, 7)),
    ("III", "Collect · Disburse · Report", "The three movements of public money", range(7, 10)),
    ("IV", "Control, Integrity, Evidence and Change", "Trust by design in a digital treasury", range(10, 14)),
    ("V", "The Framework and the Road Ahead", "Ten principles and a research agenda", range(14, 16)),
]

CHAPTERS = [s for s in _DATA if isinstance(s["n"], int)]
GLOSSARY = next(s for s in _DATA if s["n"] == "glossary")
REFERENCES = next(s for s in _DATA if s["n"] == "references")


def part_of(n):
    return next(p for p in PARTS if n in p[3])


def chapter_url(n):
    return f"{BOOK_BASE}chapter-{n}/"


GLOSSARY_URL = f"{BOOK_BASE}glossary/"
REFERENCES_URL = f"{BOOK_BASE}references/"


def plain(rich):
    return "".join(text for _, text in rich)


def words(section):
    total = 0
    for b in section["blocks"]:
        if b["t"] == "h":
            total += len(b["text"].split())
        for r in ([b["r"]] if "r" in b else []) + b.get("items", []) + [c for row in b.get("rows", []) for c in row]:
            total += len(plain(r).split())
    return total


# About the Author, from the book's page 79 (Butch 2026-11-23: "Just add the author"), matched to the About page:
# no municipality named, eligibility years as on the About page, all seven Google certificates.
AUTHOR_URL = f"{BOOK_BASE}about-the-author/"


def _p(*runs):
    return {"t": "p", "r": [list(r) if isinstance(r, tuple) else ["", r] for r in runs]}


# Shortened to brief information (Butch 2026-11-24: "Make it short information"); the full profile is on /about/.
AUTHOR = {"title": "About the Author", "blocks": [
    _p("Ambrosio “Butch” U. Mahinay, MPA, works in the local treasury service of Quezon Province. He has more "
       "than 15 years in government service, over 13 of them in public finance and local treasury work."),
    _p("He holds a Master in Public Administration and seven Google Professional Certificates. Outside official "
       "working hours he designed and built ALTOS, the Automated Local Treasury Operations System."),
    # Exams passed (Butch 2026-11-24: "add ... all examinations that the author have passed"). Names and years
    # only, never ratings; names as printed on his CSC certificates.
    _p("He has passed three government examinations:"),
    {"t": "ul", "items": [
        [["", "Intermediate Competency on Local Treasury Examination (ICLTE), 2018"]],
        [["", "Basic Competency on Local Treasury Examination (BCLTE), 2017"]],
        [["", "Career Service Professional Examination, 2012"]],
    ]},
]}
