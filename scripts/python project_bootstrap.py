import os
from datetime import datetime

PROJECT_NAME = "osso-digital-email-automation"

FILES = {
    "README.md": """# OSSO-DIGITAL — Email Automation System

Backend-first automation system designed to reduce email overload by eliminating redundancy, spam and irrelevant notifications before the user opens the inbox.

## Core idea
Configure once. Forget forever.

## What this system does
- Reduces repeated emails from the same sender
- Prioritizes important communication
- Cleans promotional and social noise
- Runs automatically on the server

## Stack
- Python (backend automation)
- VPS (DigitalOcean, 24/7)
- Mobile App (control panel)
- IMAP / Email APIs

## Project status
Under active development as an OSSO-DIGITAL product.
""",

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

    "backend/README.md": """# Backend

This folder contains the Python backend responsible for all automation logic.

The backend runs continuously on a VPS and connects directly to email servers.
""",

    "backend/app/main.py": '''"""
OSSO-DIGITAL Email Automation
Main entry point
"""
''',

    "backend/app/config.py": "# Configuration loader\n",
    "backend/app/email_client.py": "# IMAP email client\n",
    "backend/app/deduplicator.py": "# Deduplication logic\n",
    "backend/app/rules_engine.py": "# Rules engine\n",
    "backend/app/classifier.py": "# Email classifier\n",
    "backend/app/cleaner.py": "# Cleaning engine\n",
    "backend/app/logger.py": "# Logging system\n",
    "backend/app/__init__.py": "",

    "backend/storage/README.md": "# Storage for decisions and logs\n",

    "backend/.env.example": """EMAIL_PROVIDER=
EMAIL_USER=
EMAIL_PASSWORD=
IMAP_SERVER=
""",

    "backend/requirements.txt": """python-dotenv
imaplib2
""",

    "mobile/README.md": """# Mobile App

This app is a control panel for the email automation backend.

It does not read or store emails.
"""
}

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    os.makedirs(PROJECT_NAME, exist_ok=True)
    os.chdir(PROJECT_NAME)

    for path, content in FILES.items():
        create_file(path, content)

    print(f"✅ Project '{PROJECT_NAME}' created successfully")
    print(f"📦 Structure generated at {datetime.now().strftime('%d/%m/%Y %H:%M')}")

if __name__ == "__main__":
    main()
