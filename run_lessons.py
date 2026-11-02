"""Run every tutorial script and save what it prints, so each lesson page shows real output.

    python run_lessons.py           # run all lesson scripts, write <script>.out files
    python run_lessons.py --check   # fail if any saved output no longer matches

The lesson scripts live in tutorials/<lesson>/. Lesson 4 needs pandas
(pip install pandas); the website build itself does not.
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent / "tutorials"


def run(script):
    env = {k: v for k, v in os.environ.items() if k != "AUDIT_KEY"}  # lesson 5 uses its practice key
    result = subprocess.run([sys.executable, script.name], cwd=script.parent, env=env,
                            capture_output=True, text=True, timeout=60)
    if result.returncode:
        sys.exit(f"{script} failed:\n{result.stderr}")
    return result.stdout


def main(check=False):
    stale = []
    for script in sorted(ROOT.glob("*/*.py")):
        out_file = script.with_suffix(".out")
        output = run(script)
        if check:
            if not out_file.exists() or out_file.read_text(encoding="utf-8") != output:
                stale.append(script)
        else:
            out_file.write_text(output, encoding="utf-8")
            print("ran", script.relative_to(ROOT.parent))
    if stale:
        sys.exit("Output out of date for: " + ", ".join(map(str, stale)) + "\nRun: python run_lessons.py")
    if check:
        print("All lesson outputs match.")


if __name__ == "__main__":
    main(check="--check" in sys.argv)
