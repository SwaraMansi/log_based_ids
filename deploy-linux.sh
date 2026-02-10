#!/bin/bash
# Deploy to any Linux server via SSH
# Usage: ./deploy-linux.sh <user@host>

HOST=$1

echo "🚀 Deploying Log-Based IDS to $HOST..."

# Create directory and copy files
ssh "$HOST" "mkdir -p ~/log_ids && cd ~/log_ids && pwd"

scp -r ./* "$HOST":~/log_ids/

# Setup and run
ssh "$HOST" << 'EOF'
  cd ~/log_ids
  python3 -m pip install --user -r requirements.txt
  python3 ids.py
  echo "✔ IDS deployed to Linux server successfully!"
  
  # Setup cron job (runs every hour)
  (crontab -l 2>/dev/null; echo "0 * * * * cd ~/log_ids && python3 ids.py") | crontab -
  echo "✔ Cron job added - IDS will run hourly"
EOF

echo "📊 View alerts via: ssh $HOST 'cat ~/log_ids/reports/alerts.json'"
