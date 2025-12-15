#!/bin/bash
# setup.sh - Installation script for Base Finder

echo "📦 Base Finder Installation"
echo "=========================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed!"
    echo "Installing git..."
    pkg install git -y
fi

# Clone repository
echo "📥 Cloning repository..."
git clone https://github.com/niketh-ai/base-finder.git

# Navigate to directory
cd base-finder

# Install Python dependencies
echo "🔧 Installing dependencies..."
pip install -r requirements.txt

# Make scanner executable
chmod +x scanner.py

# Create symbolic link in PATH
echo "🔗 Creating system link..."
ln -sf "$(pwd)/scanner.py" /data/data/com.termux/files/usr/bin/base-finder

echo "✅ Installation complete!"
echo ""
echo "Usage:"
echo "  base-finder <url>"
echo "  Example: base-finder https://example.com"
