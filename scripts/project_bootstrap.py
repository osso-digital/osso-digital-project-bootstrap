from pathlib import Path
from datetime import datetime

ROOT = Path.cwd()
NOW = datetime.now().strftime("%d/%m/%Y %H:%M")

FILES = {
    "README.md": """# OSSO-DIGITAL — Email Automation System

Backend-first automation system designed to reduce email overload by eliminating redundancy, spam and irrelevant notifications before the user opens the inbox.

## Core idea
Configure once. Forget forever.

## What this system does
- Reduces repeated emails from the same sender
- Prioritizes important communication
- Cleans promotional and social noise
- Runs automatically on a VPS (24/7)

## Stack
- Python (automation backend)
- VPS (DigitalOcean)
- Mobile App (control panel)
- IMAP / Email APIs

## Project status
Under active development as an OSSO-DIGITAL product.
""",

    "docs/PRODUCT_VISION.md": """# Product Vision

This product exists to eliminate email overload at the source.

Instead of categorizing noise, it removes it.
The inbox should only contain signal.

No more manual cleaning.
""",

    "docs/ARCHITECTURE.md": """# System Architecture

1. Mobile App (iOS / Android)
2. Python Backend (VPS, 24/7)
3. Email Providers (IMAP / APIs)

The mobile app only controls preferences.
All automation runs server-side.
""",

    "docs/MVP.md": """# MVP Scope

- Email deduplication
- Promotion and spam reduction
- Priority inbox logic
- Safe deletion with logs

No AI required for MVP.
""",

    "docs/ROADMAP.md": """# Roadmap

Phase 1
- Core automation engine
- Rule-based classification

Phase 2
- Mobile control panel
- Logs & metrics

Phase 3
- Learning layer (optional AI)
- SaaS packaging
""",

    "backend/README.md": """# Backend

This backend runs continuously on a VPS and manages all email automation logic.
""",

    "backend/app/__init__.py": "",
    "backend/app/main.py": '''"""
OSSO-DIGITAL Email Automation
Main entry point
"""
''',
    "backend/app/config.py": "# Environment & configuration loader\n",
    "backend/app/email_client.py": "# IMAP email client abstraction\n",
    "backend/app/rules_engine.py": "# Rule-based decision engine\n",
    "backend/app/deduplicator.py": "# Deduplication logic\n",
    "backend/app/classifier.py": "# Email classification\n",
    "backend/app/cleaner.py": "# Email cleanup executor\n",
    "backend/app/logger.py": "# Logging system\n",

    "backend/storage/.gitkeep": "",
    "backend/storage/README.md": "# Persistent decisions and logs\n",

    "backend/requirements.txt": "python-dotenv\nimaplib2\n",

    "backend/.env.example": """EMAIL_PROVIDER=
EMAIL_USER=
EMAIL_PASSWORD=
IMAP_SERVER=
""",

    "mobile/README.md": """# Mobile App

This app is a control panel for the backend automation.
No emails are stored on the device.
""",

    "mobile/ui-mockups/.gitkeep": "",

    "scripts/.gitkeep": ""
}

def create_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    print("🦴 OSSO-DIGITAL PROJECT BOOTSTRAP")
    print(f"📁 Root: {ROOT}")
    print(f"⏱ Generated at: {NOW}\n")

    for file, content in FILES.items():
        create_file(ROOT / file, content)

    print("✅ Project structure fully generated")
    print("🚀 Ready for development, GitHub and VPS")

if __name__ == "__main__":
    main()
