# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY config.py .
COPY ids.py .
COPY requirements.txt .
COPY sample_logs/ ./sample_logs/

# Create reports directory
RUN mkdir -p reports

# Install dependencies (already built-in, but keeping for consistency)
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV LOG_FILE=sample_logs/auth.log
ENV REPORT_FILE=reports/alerts.json

# Run the IDS when container starts
CMD ["python", "ids.py"]
