#!/bin/bash
# EC2 Setup Script - Run this on your EC2 instance first

set -e

echo "🚀 Setting up Flask application on EC2..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install -y python3 python3-pip python3-venv git

# Create app directory
mkdir -p ~/flask-app
cd ~/flask-app

# Clone repository (replace with your repo URL)
# git clone https://github.com/YOUR_USERNAME/flask-cicd-demo.git .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup systemd service
sudo cp deploy/flask-app.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable flask-app
sudo systemctl start flask-app

echo "✅ Setup complete! App running on port 5000"
echo "🔗 Access: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):5000"
