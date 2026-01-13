import imaplib
import email
from email.header import decode_header
import os

class EmailClient:
    def __init__(self, imap_server, email_user, email_password):
        self.imap_server = imap_server
        self.email_user = email_user
        self.email_password = email_password
        self.connection = None

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.imap_server)
        self.connection.login(self.email_user, self.email_password)
        self.connection.select("INBOX")
        print("✅ Connected to email server")

    def fetch_emails(self, limit=50):
        status, messages = self.connection.search(None, "ALL")
        email_ids = messages[0].split()
        latest_ids = email_ids[-limit:]

        emails = []

        for eid in latest_ids:
            _, msg_data = self.connection.fetch(eid, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            subject, encoding = decode_header(msg.get("Subject"))[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8", errors="ignore")

            from_ = msg.get("From")

            emails.append({
                "id": eid,
                "from": from_,
                "subject": subject
            })

        return emails

    def logout(self):
        self.connection.logout()
        print("🔒 Logged out")

