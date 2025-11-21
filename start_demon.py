#!/usr/bin/env python3
"""
冥忍 MYSŌNINJA Startup Script
DEMON SLAYER ACTIVATION SEQUENCE
"""

import os
import sys
import time
from src.utils.banner import show_banner, show_mini_banner

def demon_slayer_startup():
    """Epic startup sequence"""
    
    print("Initializing Demon Slayer Protocol...")
    time.sleep(1)
    
    # Clear screen for dramatic effect
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Show the epic banner
    show_banner()
    
    # Startup sequence
    phases = [
        "ACTIVATING QUANTUM CORE...",
        "LOADING SHADOW PROTOCOLS...",
        "INITIALIZING DEMON SLAYER MODULES...",
        "SPAWNING PHISHING DEMONS...",
        "CALIBRATING AI PREDICTION ENGINE...",
        "ESTABLISHING DARK NET CONNECTIONS...",
        "READY FOR DEMON SLAYING OPERATIONS 🗡️"
    ]
    
    for phase in phases:
        print(f"🌀 {phase}")
        time.sleep(0.8)
    
    print("\n" + "🔥 SYSTEM READY! COMMENCE DEMON SLAYING! 🔥\n")

if __name__ == "__main__":
    demon_slayer_startup()
