import streamlit as st
import re
import json
from datetime import datetime

# Attack patterns
PATTERNS = {
    "bruteforce": r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)",
    "portscan": r"Did not receive identification string from (\d+\.\d+\.\d+\.\d+)",
    "sudo_fail": r"sudo: .* : authentication failure"
}

st.set_page_config(page_title="Log-Based IDS", layout="wide")

st.title("🛡️ Log-Based Intrusion Detection System")
st.write("Upload a log file to detect suspicious activities.")

uploaded_file = st.file_uploader("Upload auth.log file", type=["log", "txt"])

def analyze_log(file):
    alerts = []

    for line in file:
        line = line.decode("utf-8")

        match = re.search(PATTERNS["bruteforce"], line)
        if match:
            alerts.append({
                "Type": "Brute Force Attack",
                "IP": match.group(1),
                "Log": line.strip(),
                "Time": str(datetime.now())
            })

        match = re.search(PATTERNS["portscan"], line)
        if match:
            alerts.append({
                "Type": "Port Scan",
                "IP": match.group(1),
                "Log": line.strip(),
                "Time": str(datetime.now())
            })

        if re.search(PATTERNS["sudo_fail"], line):
            alerts.append({
                "Type": "Unauthorized Admin Access",
                "Log": line.strip(),
                "Time": str(datetime.now())
            })

    return alerts


if uploaded_file is not None:
    results = analyze_log(uploaded_file)

    if results:
        st.success(f"Detected {len(results)} suspicious activities!")
        st.json(results)
    else:
        st.info("No suspicious activity detected.")
