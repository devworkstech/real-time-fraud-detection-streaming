param([string]$Username = "soniablake")
git init; git branch -M main; git add .
git commit -m "feat: Real-Time Streaming Analytics Fraud Detection Platform - Kafka, PySpark Structured Streaming, Delta Lake"
git remote remove origin 2>$null
git remote add origin "https://github.com/$Username/real-time-fraud-detection-streaming.git"
git push -u origin main
