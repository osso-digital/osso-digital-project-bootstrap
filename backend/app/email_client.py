# IMAP email client abstraction
class EmailClient:
    def connect(self):
        print("Connected (mock)")

    def fetch_emails(self, limit=10):
        return [
            {"id": 1, "sender": "promo@store.com", "subject": "Oferta imperdível"},
            {"id": 2, "sender": "boss@empresa.com", "subject": "Reunião urgente"},
            {"id": 3, "sender": "promo@store.com", "subject": "Oferta imperdível"},
        ]
