@echo off
REM Windows Batch Script - Deploy to local Windows service or cloud

echo.
echo ========================================
echo  Log-Based IDS Deployment Options
echo ========================================
echo.
echo Choose your deployment platform:
echo.
echo 1. Docker (Recommended - requires Docker Desktop)
echo    Command: docker build -t log-based-ids:latest .
echo             docker run -v %%cd%%\reports:/app/reports log-based-ids:latest
echo.
echo 2. AWS EC2 Linux Instance
echo    Command: .\deploy-aws.sh <instance-ip> <pem-key>
echo.
echo 3. Generic Linux Server (SSH)
echo    Command: bash deploy-linux.sh user@hostname
echo.
echo 4. Heroku Cloud Platform
echo    Command: bash deploy-heroku.sh
echo.
echo 5. Local Windows Task Scheduler
echo    Run: python ids.py
echo    Then create a scheduled task in Task Scheduler
echo.
echo 6. Python Directly
echo    Command: python ids.py
echo.
echo ========================================
echo.

REM Run directly if requested
if "%1"=="run" (
    echo Running IDS locally...
    python ids.py
    if %errorlevel% == 0 (
        echo.
        echo ✔ IDS executed successfully!
        echo ✔ Check reports\alerts.json for results
    )
)
