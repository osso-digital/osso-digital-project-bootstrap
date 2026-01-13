"""
OSSO-DIGITAL Email Automation
Main entry point
"""

from email_client import EmailClient
from deduplicator import Deduplicator
from classifier import Classifier
from rules_engine import RulesEngine
from cleaner import apply_decision
from logger import log_decision
from storage import init_db, save_decision


def main():
    print("🧠 OSSO-DIGITAL EMAIL AUTOMATION ENGINE")
    print("🚀 Initializing...\n")

    # Initialize persistent storage
    init_db()

    # Initialize components
    client = EmailClient()
    client.connect()

    dedup = Deduplicator()
    classifier = Classifier()
    rules = RulesEngine()

    # Fetch emails
    emails = client.fetch_emails(limit=20)

    print(f"📨 {len(emails)} emails fetched\n")

    for email in emails:
        sender = email["sender"]
        subject = email["subject"]
        email_id = email["id"]

        # Deduplication
        if dedup.is_duplicate(sender, subject):
            decision = "DUPLICATE_SKIPPED"
            log_decision(sender, subject, decision)
            save_decision(sender, subject, decision)
            continue

        # Classification
        category = classifier.classify(sender, subject)

        # Decision engine
        decision = rules.decide(category)

        # Apply action
        apply_decision(email_id, decision)

        # Logging + persistence
        log_decision(sender, subject, decision)
        save_decision(sender, subject, decision)

    print("\n✅ Automation cycle completed successfully")


if __name__ == "__main__":
    main()
