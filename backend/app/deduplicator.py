# Deduplication logic
from collections import defaultdict
import hashlib

def _hash_email(sender: str, subject: str) -> str:
    key = f"{sender.lower()}::{subject.lower()}"
    return hashlib.sha256(key.encode()).hexdigest()

class Deduplicator:
    def __init__(self):
        self.seen = set()

    def is_duplicate(self, sender: str, subject: str) -> bool:
        h = _hash_email(sender, subject)
        if h in self.seen:
            return True
        self.seen.add(h)
        return False
