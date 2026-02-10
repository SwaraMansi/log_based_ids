#!/usr/bin/env python3
# startup.py - Wrapper to run IDS and keep the app alive

import subprocess
import time
import json
from datetime import datetime

def run_ids():
    """Run the IDS analysis"""
    print("🔍 Starting Log-Based Intrusion Detection System...")
    result = subprocess.run(['python', 'ids.py'], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    return result.returncode

if __name__ == "__main__":
    # Run IDS once
    exit_code = run_ids()
    
    if exit_code == 0:
        print("✔ IDS Analysis Complete!")
        
        # Print alerts
        try:
            with open('reports/alerts.json', 'r') as f:
                alerts = json.load(f)
                print(f"\n📊 Total alerts detected: {len(alerts)}")
                for alert in alerts:
                    print(f"  - {alert['type']}")
        except:
            pass
    
    # Keep the process alive for Railway
    while True:
        time.sleep(60)
