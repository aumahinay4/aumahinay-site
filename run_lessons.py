"""Run every tutorial script and save what it prints, so each lesson page shows real output.

    python run_lessons.py           # run all lesson scripts, write <script>.out files
    python run_lessons.py --check   # fail if any saved output no longer matches

The lesson scripts live in tutorials/<lesson>/. Some lessons need extra libraries
(pip install pandas openpyxl flask pytest); the website build itself does not.

- Answer scripts (answer_*.py) run after the lesson's other scripts, because some
  of them open a file the main script saved (an Excel file, a database).
- Test files (test_*.py) are run the way the lesson tells readers to: with pytest.
  pytest ends with how long the tests took, which changes on every run, so that
  number is ignored when outputs are compared.
- Scripts in NOT_RUN start a web server that keeps running; the lesson shows the
  output of a separate script that visits the pages instead.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent / "tutorials"
NOT_RUN = {"10-flask-web-page/app.py", "09-test-with-pytest/rpt.py", "09-test-with-pytest/series.py"}
TIMING = re.compile(r" in \d+\.\d+s")


def run(script):
    env = {k: v for k, v in os.environ.items() if k != "AUDIT_KEY"}  # lesson 5 uses its practice key
    if script.name.startswith("test_"):
        cmd = [sys.executable, "-m", "pytest", "-v", "--no-header", "-p", "no:cacheprovider", "--tb=short", script.name]
        ok = (0, 1)  # 1 means "some tests failed", which one lesson shows on purpose
    else:
        cmd, ok = [sys.executable, script.name], (0,)
    result = subprocess.run(cmd, cwd=script.parent, env=env, capture_output=True, text=True, timeout=60)
    if result.returncode not in ok:
        sys.exit(f"{script} failed:\n{result.stdout}{result.stderr}")
    return result.stdout


def same(a, b):
    return TIMING.sub("", a) == TIMING.sub("", b)


def order(script):
    return (script.parent.name, script.name.startswith("answer_"), script.name)


def main(check=False):
    stale = []
    for script in sorted(ROOT.glob("*/*.py"), key=order):
        if script.relative_to(ROOT).as_posix() in NOT_RUN:
            continue
        out_file = script.with_suffix(".out")
        output = run(script)
        old = out_file.read_text(encoding="utf-8") if out_file.exists() else None
        if check:
            if old is None or not same(old, output):
                stale.append(script)
        elif old is None or not same(old, output):  # keep the saved file if only the timing differs
            out_file.write_text(output, encoding="utf-8")
            print("ran", script.relative_to(ROOT.parent))
        else:
            print("ran", script.relative_to(ROOT.parent), "(unchanged)")
    if stale:
        sys.exit("Output out of date for: " + ", ".join(map(str, stale)) + "\nRun: python run_lessons.py")
    if check:
        print("All lesson outputs match.")


if __name__ == "__main__":
    main(check="--check" in sys.argv)
