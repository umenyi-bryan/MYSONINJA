#!/bin/bash
# 冥忍 MYSŌNINJA - Quick War Room Starter

echo -e "\e[91m"
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║ 🗡️  冥忍 MYSŌNINJA - DEMON SLAYER WAR ROOM  🗡️               ║"
echo "║ FORGED BY MYSTERYAK & KNIGHTDALE                            ║"  
echo "║ 🥶 INITIATING DEMON SLAYING SEQUENCE... 🥶                  ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo -e "\e[0m"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "\e[91m💀 Python3 not found! Please install Python 3.7+\e[0m"
    exit 1
fi

# Start the war room
python3 start_warroom.py
