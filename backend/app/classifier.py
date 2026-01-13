# Email classification
PROMOTIONAL_KEYWORDS = [
    "promo", "oferta", "desconto", "sale", "newsletter"
]

class Classifier:
    def classify(self, sender: str, subject: str) -> str:
        text = f"{sender} {subject}".lower()

        for word in PROMOTIONAL_KEYWORDS:
            if word in text:
                return "PROMOTIONAL"

        return "IMPORTANT"
