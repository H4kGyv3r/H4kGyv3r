# fetch_htb.py
import os
import requests
import logging

logger = logging.getLogger(__name__)

def get_htb_stats():
    token = os.getenv("HTB_API_TOKEN")
    if not token:
        logger.warning("HTB_API_TOKEN not set")
        return {"error": "no_token"}

    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    try:
        # Example endpoint — adjust depending on HTB Academy docs
        url = "https://academy.hackthebox.com/api/v1/student/profile"  # example path
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        # Map the returned structure to fields you want in README
        return {
            "rank": data.get("rank") or data.get("profile", {}).get("rank", "N/A"),
            "points": data.get("points") or data.get("profile", {}).get("points", 0),
            "machines_rooted": data.get("machines_rooted") or data.get("profile", {}).get("rooted_count", 0),
            "raw": data
        }
    except Exception as e:
        logger.exception("Failed to fetch HTB stats")
        return {"error": str(e)}
