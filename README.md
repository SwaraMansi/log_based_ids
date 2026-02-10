# 🛡️ Log-Based Intrusion Detection System (IDS)

A lightweight Intrusion Detection System (IDS) built using Python and Streamlit.  
This tool analyzes log files and detects suspicious activities such as:

- 🚨 Brute-force login attempts  
- 🔍 Port scanning activity  
- 🔐 Unauthorized sudo/admin access  

The application is deployed using Streamlit Cloud.

---

## 🌐 Live Demo

🔗 https://logbasedids-zmgnxp4pbbbzyuvzdpfyof.streamlit.app/

---

## 📌 Features

- Upload and analyze log files (.log / .txt)
- Detect common attack patterns using Regex
- Real-time threat detection
- Clean JSON-based output
- Deployed as a web app using Streamlit

---

## 🧠 How It Works

1. User uploads a log file.
2. The system scans each line.
3. Regex patterns detect suspicious activity.
4. Alerts are displayed instantly in the dashboard.

---

## 🔍 Detection Rules

| Attack Type | Detection Logic |
|------------|----------------|
| Brute Force | Multiple failed login attempts from same IP |
| Port Scan | Identification string connection attempts |
| Unauthorized Access | sudo authentication failures |

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Regular Expressions (Regex)

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/your-username/log_based_ids.git
cd log_based_ids
