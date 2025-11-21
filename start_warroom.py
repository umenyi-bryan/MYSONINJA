#!/usr/bin/env python3
"""
冥忍 MYSŌNINJA - War Room Startup Script
ONE-CLICK DEMON SLAYER ACTIVATION
"""

import os
import sys

# Add the src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

try:
    from main import main
    print("🔥 Starting 冥忍 MYSŌNINJA War Room...")
    main()
except ImportError as e:
    print(f"💀 Import Error: {e}")
    print("💀 Current Python path:", sys.path)
    print("💀 Make sure you're running from the project root directory!")
    sys.exit(1)
except KeyboardInterrupt:
    print("\n🗡️  Demon Slayer session ended gracefully.")
except Exception as e:
    print(f"💀 Unexpected error: {e}")
    import traceback
    traceback.print_exc()
