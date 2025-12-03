# fetch_cyberdefenders.py
import requests
import os
import logging

logger = logging.getLogger(__name__)

def get_cyberdefender_badge():
    # You gave:
    # <img src="https://cyberdefenders-storage.s3.me-central-1.amazonaws.com/profile-badges/H4kGyv3r.png" width="300" />
    # Use the public image URL directly; no API or secret needed.
    username = os.getenv("CYBERDEFENDERS_ID") or "H4kGyv3r"
    img_url = f"https://cyberdefenders-storage.s3.me-central-1.amazonaws.com/profile-badges/{username}.png"
    # Optionally check it exists:
    try:
        r = requests.head(img_url, timeout=10)
        if r.status_code in (200, 301, 302):
            return {"img_url": img_url}
        else:
            return {"error": f"status {r.status_code}", "img_url": img_url}
    except Exception as e:
        logger.exception("Failed to check cyberdefenders badge")
        return {"error": str(e)}
