import time
from main import main

INTERVAL_SECONDS = 60  # roda a cada 1 minuto

if __name__ == "__main__":
    print("🔁 OSSO-DIGITAL Automation Service started")
    while True:
        try:
            main()
        except Exception as e:
            print(f"❌ Error: {e}")
        time.sleep(INTERVAL_SECONDS)
