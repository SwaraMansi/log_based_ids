# Deployment Guide for Log-Based IDS

## Option 1: Docker (Recommended)

### Prerequisites
- Docker installed on your system

### Local Deployment

1. Build the Docker image:
```bash
docker build -t log-based-ids:latest .
```

2. Run the container:
```bash
docker run -v %cd%/reports:/app/reports log-based-ids:latest
```

Or use Docker Compose:
```bash
docker-compose up
```

### Cloud Deployment

#### AWS ECR + ECS
```bash
# Push to AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
docker build -t log-based-ids:latest .
docker tag log-based-ids:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/log-based-ids:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/log-based-ids:latest
```

#### Google Cloud Run
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/log-based-ids
gcloud run deploy log-based-ids \
  --image gcr.io/PROJECT_ID/log-based-ids \
  --platform managed
```

#### Azure Container Registry
```bash
az acr build --registry <registry-name> --image log-based-ids:latest .
az container create --resource-group <group> \
  --name log-based-ids \
  --image <registry-name>.azurecr.io/log-based-ids:latest
```

#### DigitalOcean
```bash
doctl compute app create app.yaml
```

---

## Option 2: Linux Server (Manual)

1. SSH into your server
```bash
ssh user@server-ip
```

2. Install Python:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

3. Clone repository:
```bash
git clone https://github.com/SwaraMansi/log_based_ids.git
cd log_based_ids
```

4. Run manually:
```bash
python3 ids.py
```

5. Setup automated scheduling with cron (every hour):
```bash
0 * * * * /usr/bin/python3 /path/to/ids.py
```

---

## Option 3: GitHub Actions (CI/CD)

Create `.github/workflows/ids-scan.yml`:

```yaml
name: Log-Based IDS Scanner

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Run IDS
        run: python ids.py
      - name: Upload alerts
        uses: actions/upload-artifact@v3
        with:
          name: security-alerts
          path: reports/alerts.json
```

---

## Option 4: Heroku Deployment

1. Install Heroku CLI
2. Create `Procfile`:
```
web: python ids.py
```

3. Deploy:
```bash
heroku login
heroku create log-based-ids
git push heroku main
```

---

## Monitoring & Alerts

Configure your chosen platform to:
- Monitor log file sources
- Send alerts when threats are detected
- Store reports in persistent storage
- Setup notifications (Email, Slack, PagerDuty)

---

## Environment Variables

- `LOG_FILE`: Path to log file (default: `sample_logs/auth.log`)
- `REPORT_FILE`: Path to save alerts (default: `reports/alerts.json`)
