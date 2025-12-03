from datetime import datetime

def generate_readme():
    return f"""
# 🔐 HakGyver — Cybersecurity Portfolio (Auto-Updated)

**Last update:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC

This README updates automatically using **Python + GitHub Actions**.
"""

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(generate_readme())
