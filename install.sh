#!/bin/bash

echo "🗡️ MYSŌNINJA ULTIMATE - Installation"
echo "🔮 Created by MysteryAK & Knightdale"
echo "==========================================="

# Install dependencies
echo "📦 Installing dependencies..."
pkg update && pkg upgrade -y
pkg install -y python python-pip git curl wget nmap nikto php openssh

# Install ngrok for phishing links
echo "🌐 Installing ngrok..."
pkg install -y ngrok || pip install pyngrok

# Install Python packages
echo "🐍 Installing Python packages..."
pip install flask requests beautifulsoup4

# Setup Zphisher
echo "🎣 Setting up Zphisher..."
if [ ! -d "zphisher" ]; then
    git clone https://github.com/htr-tech/zphisher.git
    chmod +x zphisher/zphisher.sh
fi

# Create directories
mkdir -p web_data static

echo "✅ Installation complete!"
echo "🌐 Ngrok: Installed for public phishing links"
echo "🚀 Launch: python src/mysoninja_web_controlled.py"
echo "🌑 Access: http://127.0.0.1:5000"
echo ""
echo "📝 Ngrok Setup:"
echo "   1. Get free account: https://ngrok.com"
echo "   2. Run: ngrok authtoken YOUR_TOKEN"
echo "   3. Public URLs will appear automatically!"
