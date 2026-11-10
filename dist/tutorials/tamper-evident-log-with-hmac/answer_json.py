"""Answer: save the sealed log to a JSON file, load it back, and verify it."""

import hashlib
import hmac
import json
import os

SECRET_KEY = os.environ.get("AUDIT_KEY", "practice-key-only").encode()


def seal(entry, previous_seal):
    message = previous_seal + json.dumps(entry, sort_keys=True)
    return hmac.new(SECRET_KEY, message.encode(), hashlib.sha256).hexdigest()


def add(log, entry):
    previous = log[-1]["seal"] if log else "START"
    log.append({"entry": entry, "seal": seal(entry, previous)})


def verify(log):
    problems, previous = [], "START"
    for i, item in enumerate(log, start=1):
        if not hmac.compare_digest(item["seal"], seal(item["entry"], previous)):
            problems.append(i)
        previous = item["seal"]
    return problems


log = []
add(log, {"time": "2026-11-02 08:15", "action": "issue OR", "or": 7650101, "amount": "4500.00"})
add(log, {"time": "2026-11-02 08:40", "action": "issue OR", "or": 7650102, "amount": "1250.75"})

with open("audit_log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2)

with open("audit_log.json", encoding="utf-8") as f:
    loaded = json.load(f)
print("Loaded copy:", verify(loaded) or "all seals match")

# Edit the file the way a person would in a text editor: change 1250.75 to 250.75
with open("audit_log.json", encoding="utf-8") as f:
    text = f.read()
with open("audit_log.json", "w", encoding="utf-8") as f:
    f.write(text.replace('"1250.75"', '"250.75"'))

with open("audit_log.json", encoding="utf-8") as f:
    edited = json.load(f)
print("After editing the file:", verify(edited) or "all seals match")
