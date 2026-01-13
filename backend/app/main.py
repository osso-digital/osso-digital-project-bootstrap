from email_client import EmailClient
import os

client = EmailClient(
    imap_server=os.getenv("IMAP_SERVER"),
    email_user=os.getenv("EMAIL_USER"),
    email_password=os.getenv("EMAIL_PASSWORD")
)

client.connect()
emails = client.fetch_emails(limit=10)

for e in emails:
    print(e)

client.logout()
