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

BOOK_BASE = "/projects/altos-book/"

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


AUTHOR = {"title": "About the Author", "blocks": [
    _p("Ambrosio “Butch” U. Mahinay, MPA, works in the local treasury service of Quezon Province, with more than 15 "
       "years in government service, over 13 of them in public finance. He has been designated Acting Municipal "
       "Treasurer of municipalities in Quezon (2020–2022, and since September 2024). Outside official working hours "
       "he designed and built ALTOS, the Automated Local Treasury Operations System."),
    _p(("b", "Treasury career. "), "Administrative Assistant II (Disbursing Officer II), Office of the Provincial "
       "Treasurer (2013–2019); Local Revenue Collection Officer III (2019 to the present); designated Acting "
       "Municipal Treasurer (2020–2022, and since September 2024)."),
    _p(("b", "Education. "), "Master in Public Administration (2014) and Bachelor of Science in Public Administration "
       "(2008), Manuel S. Enverga University Foundation; Computer System Design and Programming, AMA Computer "
       "Learning Center (2000)."),
    _p(("b", "Teaching. "), "Part-time lecturer, Manuel S. Enverga University Foundation, Catanauan (2010)."),
    _p(("b", "Eligibility. "), "Career Service Professional (2012); Basic Competency on Local Treasury Examination "
       "(2018); Intermediate Competency on Local Treasury Examination (2019)."),
    _p(("b", "Google Professional Certificates. "), "Cybersecurity, Project Management, Data Analytics, Advanced Data "
       "Analytics, Business Intelligence, AI and IT Support (2025–2026)."),
    _p(("b", "Public finance training. "), "Bureau of Local Government Finance programs on local revenue forecasting "
       "and resource mobilization, devolution transition planning, property tax, local fees and charges, integrity "
       "in local government, treasury and assessment service excellence, and revenue target setting; Department of "
       "Information and Communications Technology (DICT) training for users of the electronic Business Permits and "
       "Licensing System (eBPLS); Civil Service Institute financial education; data privacy orientation."),
    _p(("b", "Organizations. "), "Member, Philippine Association of Local Treasurers and Assessors (PHALTRA); Vice "
       "President, UNIKA sa Quezon (2019–2025)."),
]}
