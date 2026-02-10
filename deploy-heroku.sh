#!/bin/bash
# Deploy to Heroku Platform-as-a-Service
# Prerequisites: heroku CLI installed, logged in

echo "🚀 Deploying Log-Based IDS to Heroku..."

# Create Procfile
cat > Procfile << 'EOF'
worker: python ids.py
EOF

# Create Heroku app (if not exists)
HEROKU_APP="log-based-ids-$(date +%s)"
heroku create "$HEROKU_APP" || true

# Deploy
git add .
git commit -m "Deploy Log-Based IDS"
git push heroku main

# Setup schedulers
heroku addons:create scheduler:standard
heroku run "python ids.py"

echo "✔ Deployed to Heroku: $HEROKU_APP"
echo "📊 View logs: heroku logs --tail --app $HEROKU_APP"
