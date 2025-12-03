# fetch_thm.py
import requests
import logging
import os

logger = logging.getLogger(__name__)

def get_thm_badge():
    # You provided a TryHackMe public badge endpoint in iframe form.
    # TryHackMe also has public badge URLs that return embeddable content.
    # We will download the badge HTML or image and return a safe embeddable image URL.
    public_id = os.getenv("THM_PUBLIC_ID") or "5187069"  # your id
    badge_url = f"https://tryhackme.com/api/v2/badges/public-profile?userPublicId={public_id}"
    try:
        resp = requests.get(badge_url, timeout=10)
        resp.raise_for_status()
        # The endpoint may return HTML/iframe — we will embed the badge as an <img> if possible,
        # otherwise link to the badge_url.
        return {"badge_url": badge_url, "html": resp.text[:1000]}
    except Exception as e:
        logger.exception("Failed to fetch TryHackMe badge")
        return {"error": str(e)}
