import os
from pathlib import Path
from datetime import datetime

# ===============================
# CONFIG
# ===============================
PROJECT_NAME = "osso-digital-email-automation"
ROOT = Path.cwd()  # assume execução na raiz do repo

NOW = datetime.now().strftime("%d/%m/%Y %H:%M")

# ===============================
# FILE STRUCTURE + CONTENT
# ===============================
STRUCTURE = {
    "README.md": f"""# OSSO-DIGITAL — Email Automation System

Backend-first automation system designed to reduce email overload by eliminating redundancy, spam and irrelevant notifications before the user opens the inbox.

## Core idea
Configure once. Forget forever.

## What this system does
- Reduces repeated emails from the same sender
- Prioritizes important communication
- Cleans promotional and social noise
- Runs automatically on the server (24/7)

## Stack
- Python (backend automation)
- VPS (DigitalOcean)
- Mobile App (control panel)
- IMAP / Email APIs

## Project status
Under active development as an OSSO-DIGITAL product.

Created on {NOW}
""",

    # ===============================
    # DOCS
    # ===============================
    "docs/PRODUCT_VISION.md": """# Product Vision

This project was created to solve a real and recurring problem: email overload.

Modern email clients classify messages, but they do not reduce decision fatigue.
This system focuses on eliminating redundancy and preserving signal.

The user should never need to manually clean the inbox again.
""",

    "docs/ARCHITECTURE.md": """# System Architecture

The system is composed of three main layers:

1. Mobile App (iOS / Android)
2. Backend API (Python, VPS)
3. Email Server (IMAP / Provider APIs)

The mobile app acts only as a control panel.
All logic and automation run on the backend.
""",

    "docs/MVP.md": """# MVP Scope

The initial MVP focuses on:

- Email deduplication by sender and subject
- Spam and promotion reduction
- Priority-based inbox filtering
- Safe deletion with logging

No AI is required for the first version.
""",

    "docs/ROADMAP.md": """# Roadmap

Phase 1:
- Core automation
- Deduplication engine
- Rule-based classification

Phase 2:
- Mobile control panel
- User preferences
- Logs and metrics

Phase 3:
- Learning layer (optional AI)
- SaaS packaging
""",

    # ===============================
    # BACKEND
    # ===============================
    "backend/README.md": """# Backend

This folder contains the Python backend responsible for all automation logic.

The backend runs continuously on a VPS and connects directly to email servers.
""",

    "backend/app/__init__.py": "",
    "backend/app/config.py": "# Environment configuration loader\n",
    "backend/app/main.py": '''"""
OSSO-DIGITAL Email Automation
Main entry point
"""
def main():
    print("OSSO-DIGITAL Email Automation running")

if __name__ == "__main__":
    main()
''',

    "backend/app/email_client.py": "# IMAP email client abstraction\n",
    "backend/app/deduplicator.py": "# Deduplication logic\n",
    "backend/app/rules_engine.py": "# Rules engine\n",
    "backend/app/classifier.py": "# Email classifier\n",
    "backend/app/cleaner.py": "# Cleaning engine\n",
    "backend/app/logger.py": "# Logging system\n",

    "backend/storage/.gitkeep": "",
    "backend/storage/README.md": "Storage for decisions, logs and audit trails\n",

    "backend/.env.example": """EMAIL_PROVIDER=
EMAIL_USER=
EMAIL_PASSWORD=
IMAP_SERVER=
""",

    "backend/requirements.txt": """python-dotenv
imaplib2
""",

    # ===============================
    # MOBILE
    # ===============================
    "mobile/README.md": """# Mobile App

This app is a control panel for the email automation backend.

- No email processing
- No email storage
- Backend-first architecture
""",

    "mobile/ui-mockups/.gitkeep": "",

    # ===============================
    # SCRIPTS
    # ===============================
    "scripts/.gitkeep": ""
}

# ===============================
# ENGINE
# ===============================
def create_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    print("🦴 OSSO-DIGITAL Project Bootstrap")
    print(f"📁 Root: {ROOT}")
    print(f"🕒 {NOW}\n")

    for relative_path, content in STRUCTURE.items():
        full_path = ROOT / relative_path
        create_file(full_path, content)

    print("✅ Full project structure created successfully")
    print("🚀 Ready for git add / commit / push")

if __name__ == "__main__":
    main()
