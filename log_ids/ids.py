# ids.py - Main Intrusion Detection System script

import re
import json
from datetime import datetime
from config import LOG_FILE, PATTERNS

REPORT_FILE = "reports/alerts.json"


def save_alert(alerts):
    """Save all alerts as a valid JSON array"""
    with open(REPORT_FILE, "w") as file:
        json.dump(alerts, file, indent=4)


def analyze_log():
    print("🔍 Starting Log-Based Intrusion Detection System...")

    alerts = []   # store all alerts here

    with open(LOG_FILE, "r", errors="ignore") as f:
        for line in f:

            # --------- Brute Force Detection ---------
            match = re.search(PATTERNS["bruteforce"], line)
            if match:
                ip = match.group(1)
                alerts.append({
                    "type": "Brute Force Attempt",
                    "ip": ip,
                    "time": str(datetime.now()),
                    "log": line.strip()
                })

            # --------- Port Scanning Detection ---------
            match = re.search(PATTERNS["portscan"], line)
            if match:
                ip = match.group(1)
                alerts.append({
                    "type": "Port Scan Attempt",
                    "ip": ip,
                    "time": str(datetime.now()),
                    "log": line.strip()
                })

            # --------- Unauthorized Sudo Access Detection ---------
            if re.search(PATTERNS["sudo_fail"], line):
                alerts.append({
                    "type": "Unauthorized Admin Access",
                    "time": str(datetime.now()),
                    "log": line.strip()
                })

    # Save all alerts properly in JSON array format
    save_alert(alerts)

    print("✔ IDS Analysis Complete! Alerts saved in reports/alerts.json")


if __name__ == "__main__":
    analyze_log()
