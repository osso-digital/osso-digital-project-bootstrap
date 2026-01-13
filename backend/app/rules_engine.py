# Rule-based decision engine
class RulesEngine:
    def decide(self, category: str) -> str:
        if category == "PROMOTIONAL":
            return "ARCHIVE"

        if category == "IMPORTANT":
            return "KEEP"

        return "REVIEW"
