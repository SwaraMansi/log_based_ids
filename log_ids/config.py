# config.py - Contains file paths and attack patterns

# Path to the log file (for practice use sample_logs/auth.log)
LOG_FILE = "sample_logs/auth.log"

# Regex patterns to detect different attacks
PATTERNS = {
    "bruteforce": r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)",
    "portscan": r"Did not receive identification string from (\d+\.\d+\.\d+\.\d+)",
    "sudo_fail": r"sudo: .* : authentication failure"
}
