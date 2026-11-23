"""Run every Python example in glossary.py and check that it prints exactly what the page says.

    python check_glossary.py        (needs pandas, openpyxl, flask and pytest installed)

Examples whose label says they are typed in the terminal, or that show a file (CSV), are skipped.
For an example that ends in an error, the last line of the error is compared.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from glossary import GLOSSARY

SKIP = {"pip", "CSV"}            # a terminal command and a data file, not Python to run
failed = 0
for g in GLOSSARY:
    if g["term"] in SKIP or g.get("output") is None:
        continue
    with tempfile.TemporaryDirectory() as tmp:
        if g["term"] == "Library":   # show the error a missing library gives, without uninstalling pandas
            cmd = [sys.executable, "-I", "-S", "-c", g["code"]]
        elif g["term"] == "Test":
            Path(tmp, "test_peso.py").write_text(g["code"] + "\n", encoding="utf-8")
            cmd = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_peso.py"]
        else:
            Path(tmp, "example.py").write_text(g["code"] + "\n", encoding="utf-8")
            cmd = [sys.executable, "example.py"]
        r = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
    got = r.stdout.strip() if r.returncode == 0 else r.stderr.strip().splitlines()[-1]
    if g["term"] == "Test":
        got = r.stdout.strip().splitlines()[-1].split(" in ")[0].strip("= ")
    ok = got == g["output"]
    failed += not ok
    print(f"{'ok  ' if ok else 'FAIL'} {g['term']}")
    if not ok:
        print("     expected:", repr(g["output"]), "\n     got:     ", repr(got))
print(f"\n{len(GLOSSARY)} words, {failed} failed")
sys.exit(1 if failed else 0)
