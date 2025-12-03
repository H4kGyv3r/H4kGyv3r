#!/usr/bin/env python3
import os
import requests
from datetime import datetime

# Secrets / IDs from environment
HTB_TOKEN = os.getenv("HTB_API_TOKEN")
THM_API_KEY = os.getenv("THM_API_KEY")
CD_ID = os.getenv("CYBERDEFENDERS_ID")  # Example: H4kGyv3r

# README path
README_FILE = "README.md"

def fetch_htb_rank(token):
    """Fetch HTB profile info"""
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    url = "https://www.hackthebox.com/api/v4/profile/info"
    try:
        r = requests.get(url, headers=headers, timeout=10)
        data = r.json()
        rank = data.get("profile", {}).get("rank", "N/A")
        points = data.get("profile", {}).get("points", 0)
        return rank, points
    except Exception:
        return "N/A", 0

def fetch_thm_level(api_key):
    """Fetch TryHackMe stats"""
    url = f"https://tryhackme.com/api/v2/badges/public-profile?userPublicId={api_key}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        level = data.get("level", "N/A")
        rooms = data.get("roomsCompleted", 0)
        return level, rooms
    except Exception:
        return "N/A", 0

def generate_cd_badge(student_id):
    """Generate CyberDefenders badge URL"""
    return f"https://cyberdefenders-storage.s3.me-central-1.amazonaws.com/profile-badges/{student_id}.png"

def update_readme(htb_rank, htb_points, thm_level, thm_rooms, cd_badge_url):
    """Update README.md placeholders"""
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace placeholders in README
    content = content.replace("HTB-RANK-PLACEHOLDER", str(htb_rank))
    content = content.replace("HTB-POINTS-PLACEHOLDER", str(htb_points))
    content = content.replace("THM-LEVEL-PLACEHOLDER", str(thm_level))
    content = content.replace("THM-ROOMS-PLACEHOLDER", str(thm_rooms))
    content = content.replace("CYBERDEFENDERS-BADGE-URL", cd_badge_url)
    content = content.replace("LAST-UPDATE-PLACEHOLDER", datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ README.md updated successfully!")

if __name__ == "__main__":
    htb_rank, htb_points = fetch_htb_rank(HTB_TOKEN)
    thm_level, thm_rooms = fetch_thm_level(THM_API_KEY)
    cd_badge_url = generate_cd_badge(CD_ID)
    update_readme(htb_rank, htb_points, thm_level, thm_rooms, cd_badge_url)
