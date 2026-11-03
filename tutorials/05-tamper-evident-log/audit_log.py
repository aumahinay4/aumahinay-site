"""A tamper-evident log: each entry is sealed with an HMAC that also covers the entry before it."""

import hashlib
import hmac
import json
import os

# In real use the key comes from outside the code, e.g. an environment variable.
SECRET_KEY = os.environ.get("AUDIT_KEY", "practice-key-only").encode()


def seal(entry: dict, previous_seal: str) -> str:
    message = previous_seal + json.dumps(entry, sort_keys=True)
    return hmac.new(SECRET_KEY, message.encode(), hashlib.sha256).hexdigest()


def add(log: list, entry: dict) -> None:
    previous = log[-1]["seal"] if log else "START"
    log.append({"entry": entry, "seal": seal(entry, previous)})


def verify(log: list) -> list:
    """Return the positions of entries whose seal no longer matches."""
    problems, previous = [], "START"
    for i, item in enumerate(log, start=1):
        if not hmac.compare_digest(item["seal"], seal(item["entry"], previous)):
            problems.append(i)
        previous = item["seal"]
    return problems


log = []
add(log, {"time": "2026-11-02 08:15", "user": "collector_a", "action": "issue OR", "or": 7650101, "amount": "4500.00"})
add(log, {"time": "2026-11-02 08:40", "user": "collector_a", "action": "issue OR", "or": 7650102, "amount": "1250.75"})
add(log, {"time": "2026-11-02 09:05", "user": "collector_a", "action": "cancel OR", "or": 7650103, "amount": "0.00"})
add(log, {"time": "2026-11-02 16:30", "user": "treasurer", "action": "deposit", "amount": "5750.75"})

for i, item in enumerate(log, start=1):
    e = item["entry"]
    print(f"{i}. {e['time']}  {e['action']:<10}{e['amount']:>9}  seal {item['seal'][:12]}...")

print("\nCheck 1:", verify(log) or "all seals match")

# Someone quietly edits the amount on the second receipt
log[1]["entry"]["amount"] = "250.75"
print("Check 2:", verify(log) or "all seals match")

# Put the amount back, then remove the cancelled receipt from the log instead
log[1]["entry"]["amount"] = "1250.75"
del log[2]
print("Check 3:", verify(log) or "all seals match")
