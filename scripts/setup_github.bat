@echo off
setlocal
echo ===================================================
echo  Real-Time Fraud Detection Streaming Platform
echo ===================================================
git init
git branch -M main
git add .
git commit -m "feat: Real-Time Streaming Analytics Fraud Detection Platform - Kafka, PySpark Structured Streaming, Delta Lake"
set /p GH_USER="Enter GitHub username (or press enter for soniablake): "
if "%GH_USER%"=="" set GH_USER=soniablake
git remote remove origin 2>nul
git remote add origin https://github.com/%GH_USER%/real-time-fraud-detection-streaming.git
git push -u origin main
pause
