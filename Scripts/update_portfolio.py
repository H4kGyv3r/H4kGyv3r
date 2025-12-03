# update_portfolio.py
import logging
import os
from datetime import datetime
from pathlib import Path

from fetch_htb import get_htb_stats
from fetch_thm import get_thm_badge
from fetch_cyberdefenders import get_cyberdefender_badge

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("portfolio")

def build_readme(htb, thm, cd):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    # Use direct image links for badges so GitHub will render them
    cd_img = cd.get("img_url", "")
    thm_link = thm.get("badge_url", "")
    htb_rank = htb.get("rank", "N/A")
    htb_points = htb.get("points", 0)

    md = f"""# 🔐 HakGyver — Cybersecurity Portfolio (Auto-Updated)

**Last automated update:** {timestamp}

## 📊 Live Stats

- **HackTheBox** — Rank: **{htb_rank}**, Points: **{htb_points}**
- **TryHackMe** — Badge / profile: [View]({thm_link})
- **CyberDefenders** — Badge:

<img src="{cd_img}" width="300" alt="CyberDefenders badge" />

---

## 🔧 About this automation

This README is updated automatically via GitHub Actions, which runs `scripts/update_portfolio.py` periodically. Data sources:
- HackTheBox Academy API (secret: HTB_API_TOKEN)
- TryHackMe public badge
- CyberDefenders public badge image

"""
    return md

def main():
    os.chdir(Path(__file__).parent)  # ensure relative imports work
    from fetch_htb import get_htb_stats as htb_fetch
    from fetch_thm import get_thm_badge as thm_fetch
    from fetch_cyberdefenders import get_cyberdefender_badge as cd_fetch

    htb = htb_fetch()
    thm = thm_fetch()
    cd = cd_fetch()

    readme = build_readme(htb, thm, cd)
    # Write README at repo root
    with open("../README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    logger.info("README updated.")

if __name__ == "__main__":
    main()
