from fastapi import FastAPI
from .storage import get_last_decisions

app = FastAPI(title="OSSO-DIGITAL Email Automation API")


@app.get("/")
def status():
    return {
        "status": "running",
        "engine": "OSSO-DIGITAL",
        "mode": "automation"
    }


@app.get("/decisions")
def decisions(limit: int = 50):
    return get_last_decisions(limit)
