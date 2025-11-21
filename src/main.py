#!/usr/bin/env python3
"""
冥忍 MYSŌNINJA - Main Application Entry Point
DEMON SLAYER ACTIVATION SEQUENCE
"""

import os
import sys
import time
import threading
import webbrowser

# Add the current directory to Python path
sys.path.append(os.path.dirname(__file__))

try:
    from utils.banner import show_banner, show_mini_banner
    BANNER_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  Banner module not available: {e}")
    BANNER_AVAILABLE = False

def demon_slayer_startup():
    """Epic startup sequence with banner"""
    
    # Clear screen for dramatic effect
    os.system('clear' if os.name == 'posix' else 'cls')
    
    if BANNER_AVAILABLE:
        # Show the epic banner
        show_banner()
    else:
        # Fallback basic banner
        print("\n" + "="*60)
        print("🗡️  冥忍 MYSŌNINJA - DEMON SLAYER EDITION")
        print("FORGED BY MYSTERYAK & KNIGHTDALE")
        print("="*60 + "\n")
    
    # Dramatic startup sequence
    startup_phases = [
        "ACTIVATING QUANTUM CORE...",
        "LOADING SHADOW PROTOCOLS...",
        "INITIALIZING DEMON SLAYER MODULES...",
        "SPAWNING PHISHING DEMONS...",
        "CALIBRATING AI PREDICTION ENGINE...",
        "ESTABLISHING DARK NET CONNECTIONS...",
        "PREPARING WAR ROOM DASHBOARD...",
        "READY FOR DEMON SLAYING OPERATIONS 🗡️"
    ]
    
    for phase in startup_phases:
        print(f"🌀 {phase}")
        time.sleep(0.7)
    
    print("\n" + "🔥 SYSTEM READY! COMMENCE DEMON SLAYING! 🔥\n")
    time.sleep(1)

def open_browser():
    """Open web browser automatically after delay"""
    time.sleep(3)
    try:
        webbrowser.open('http://127.0.0.1:5000')
        print("🌐 Browser opening to War Room Dashboard...\n")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
        print("🌐 Please manually navigate to: http://127.0.0.1:5000\n")

def setup_flask_app():
    """Setup and return Flask application"""
    from flask import Flask, render_template
    
    app = Flask(__name__, template_folder='templates')
    app.secret_key = 'demon_slayer_secret_key_2024'
    
    # Main dashboard route
    @app.route('/')
    def demon_dashboard():
        return render_template('demon_dashboard.html')
    
    # Phishing module routes
    @app.route('/phishing/generate', methods=['POST'])
    def generate_phishing():
        return {"status": "success", "message": "Phishing campaign started"}
    
    # Network scanning routes
    @app.route('/network/scan', methods=['POST'])
    def network_scan():
        return {"status": "success", "message": "Network scan initiated"}
    
    return app

def main():
    """Main application entry point"""
    
    # Show epic startup sequence
    demon_slayer_startup()
    
    # Create Flask app
    try:
        app = setup_flask_app()
    except ImportError as e:
        print(f"💀 FLASK NOT INSTALLED: {e}")
        print("💀 Please install Flask: pip install flask")
        return
    except Exception as e:
        print(f"💀 Error setting up Flask: {e}")
        return
    
    # Start browser in background thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Final message before server starts
    print("="*60)
    print("🗡️  冥忍 MYSŌNINJA WEB SERVER STARTING...")
    print("🌐 War Room Dashboard: http://127.0.0.1:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    # Start Flask development server
    try:
        app.run(
            host='127.0.0.1',
            port=5000,
            debug=True,
            use_reloader=False
        )
    except KeyboardInterrupt:
        print("\n🗡️  Demon Slayer session terminated. Until next time...")
    except Exception as e:
        print(f"\n💀 Error: {e}")

if __name__ == "__main__":
    main()
