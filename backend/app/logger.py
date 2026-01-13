# Logging system
from datetime import datetime

def log_decision(sender, subject, decision):
    ts = datetime.now().isoformat()
    line = f"[{ts}] {decision} | {sender} | {subject}\n"

    with open("backend/storage/decisions.log", "a", encoding="utf-8") as f:
        f.write(line)
