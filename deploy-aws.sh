#!/bin/bash
# Deploy to AWS EC2 instance
# Usage: ./deploy-aws.sh <instance-ip> <pem-key-path>

INSTANCE_IP=$1
PEM_KEY=$2

echo "🚀 Deploying Log-Based IDS to AWS EC2..."

# Copy files to EC2
scp -i "$PEM_KEY" -r ./* ec2-user@"$INSTANCE_IP":/home/ec2-user/log_ids/

# SSH and setup
ssh -i "$PEM_KEY" ec2-user@"$INSTANCE_IP" << 'EOF'
  sudo yum update -y
  sudo yum install python3 python3-pip -y
  cd /home/ec2-user/log_ids
  pip3 install -r requirements.txt
  python3 ids.py
  echo "✔ IDS deployed on AWS EC2 successfully!"
EOF

echo "📊 View alerts at: reports/alerts.json"
