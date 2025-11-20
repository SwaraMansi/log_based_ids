🚨 Log-Based Intrusion Detection System (IDS)

A lightweight, extensible, and Python-based Intrusion Detection System (IDS) designed to monitor system logs and detect suspicious activities including brute-force login attempts, port scanning behavior, and unauthorized admin access.
This project demonstrates practical cybersecurity skills such as log analysis, threat detection, regex-based pattern matching, alert generation, and automation — making it perfect for internships, projects, and portfolios.

 Features
✔ Brute Force Attack Detection

Identifies repeated failed login attempts commonly used in SSH or system-level brute forcing.

✔ Port Scan Detection

Detects attackers probing open ports by checking unusual or missing identification messages.

✔ Unauthorized Admin Access Detection

Flags suspicious sudo authentication failures.

✔ Structured Alerts in JSON

All generated alerts are safely stored inside:

reports/alerts.json

✔ Fully Rule-Based (Regex Driven)

New attack signatures can be added easily using regular expressions.

✔ Beginner-Friendly + Industry-Relevant

Simple to run, easy to extend, and very useful for cybersecurity learning.
