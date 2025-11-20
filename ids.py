# ids.py - Main Intrusion Detection System script

import re
import json
from datetime import datetime
from config import LOG_FILE, PATTERNS

REPORT_FILE = "reports/alerts.json"

def save_alert(alert):
    """Save the detected alert into alerts.json"""
    with open(REPORT_FILE, "a") as file:
        file.write(json.dumps(alert) + "\n")

def analyze_log():
    print("🔍 Starting Log-Based Intrusion Detection System...")

    with open(LOG_FILE, "r", errors="ignore") as f:
        for line in f:

            # --------- Brute Force Detection ---------
            match = re.search(PATTERNS["bruteforce"], line)
            if match:
                ip = match.group(1)
                alert = {
                    "type": "Brute Force Attempt",
                    "ip": ip,
                    "time": str(datetime.now()),
                    "log": line.strip()
                }
                save_alert(alert)

            # --------- Port Scanning Detection ---------
            match = re.search(PATTERNS["portscan"], line)
            if match:
                ip = match.group(1)
                alert = {
                    "type": "Port Scan Attempt",
                    "ip": ip,
                    "time": str(datetime.now()),
                    "log": line.strip()
                }
                save_alert(alert)

            # --------- Unauthorized Sudo Access Detection ---------
            if re.search(PATTERNS["sudo_fail"], line):
                alert = {
                    "type": "Unauthorized Admin Access",
                    "time": str(datetime.now()),
                    "log": line.strip()
                }
                save_alert(alert)

    print("✔ IDS Analysis Complete! Alerts saved in reports/alerts.json")

if __name__ == "__main__":
    analyze_log()
