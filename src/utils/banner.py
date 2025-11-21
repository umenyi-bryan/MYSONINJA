#!/usr/bin/env python3
"""
冥忍 MYSŌNINJA - Terminal Banner
DEMON SLAYER EDITION - FORGED IN DARKNESS 🥶
"""

import random
import time
import sys
import os

# Try to import colorama, fallback to basic colors if not available
try:
    from colorama import init, Fore, Back, Style
    COLORAMA_AVAILABLE = True
    init()
except ImportError:
    COLORAMA_AVAILABLE = False
    # Basic color codes for fallback
    class Fore:
        RED = '\033[91m'
        LIGHTRED_EX = '\033[91m'
        WHITE = '\033[97m'
        LIGHTWHITE_EX = '\033[97m'
        LIGHTCYAN_EX = '\033[96m'
        LIGHTBLUE_EX = '\033[94m'
        LIGHTYELLOW_EX = '\033[93m'
        LIGHTMAGENTA_EX = '\033[95m'
    
    class Style:
        BRIGHT = '\033[1m'
        NORMAL = '\033[0m'
        DIM = '\033[2m'

class DemonSlayerBanner:
    def __init__(self):
        self.colors = [Fore.RED, Fore.LIGHTRED_EX, Fore.WHITE, Fore.LIGHTWHITE_EX]
        self.neon_effects = [Style.BRIGHT, Style.NORMAL]
        self.samurai_art = []
        self.slogans = [
            "FORGED IN THE ABYSS - TEMPERED IN SHADOWS",
            "WHERE DEMONS FEAR TO TREAD", 
            "DARKNESS OBEYS OUR COMMAND",
            "THE NIGHT IS OUR DOMAIN",
            "SOULS SHATTER AT OUR TOUCH",
            "ETERNAL HUNT - INFINITE POWER",
            "FROM DARKNESS WE RISE - IN SHADOWS WE REIGN",
            "THE COLD NEVER BOTHERED US ANYWAY 🥶"
        ]
        
    def create_samurai_art(self):
        """Create the epic samurai demon slayer ASCII art"""
        self.samurai_art = [
            r"                                                                                ",
            r"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ",
            r"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ",
            r"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ",
            r"    ⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀    ",
            r"    ⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀    ",
            r"    ⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀    ",
            r"    ⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀    ",
            r"    ⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⡀⠀⠀⠀    ",
            r"    ⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣇⠀⠀⠀    ",
            r"    ⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⡄⠀⠀    ",
            r"    ⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀⠀    ",
            r"    ⢀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⠀⠀    ",
            r"    ⠘⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀    ",
            r"    ⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀    ",
            r"    ⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀    ",
            r"                                                                                "
        ]
        
    def print_banner(self):
        """Display the epic banner with animations"""
        self.create_samurai_art()
        
        # Random neon color for the banner
        banner_color = random.choice([Fore.LIGHTRED_EX, Fore.RED, Fore.LIGHTMAGENTA_EX])
        text_color = random.choice([Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTBLUE_EX])
        accent_color = Fore.LIGHTYELLOW_EX
        
        print("\n" + "="*90)
        
        # Animated samurai art
        for line in self.samurai_art:
            colored_line = banner_color + line
            print(colored_line)
            time.sleep(0.05)
        
        print("\n")
        
        # Main title with blood effect
        title = "冥忍 MYSŌNINJA"
        title_line = banner_color + Style.BRIGHT + " " * 25 + "🗡️  " + title + "  🗡️" + " " * 25
        print(title_line)
        
        # Subtitle
        subtitle = "QUANTUM RED TEAM WARFARE PLATFORM"
        subtitle_line = text_color + Style.BRIGHT + " " * 30 + subtitle + " " * 30
        print(subtitle_line)
        
        print("\n")
        
        # Creators section
        creators = "FORGED BY MYSTERYAK & KNIGHTDALE"
        creators_line = accent_color + Style.BRIGHT + " " * 28 + "⚔️  " + creators + "  ⚔️" + " " * 28
        print(creators_line)
        
        # Random slogan
        slogan = random.choice(self.slogans)
        slogan_line = Fore.LIGHTRED_EX + Style.BRIGHT + " " * 25 + "🥶  " + slogan + "  🥶" + " " * 25
        print(slogan_line)
        
        # Demon slayer badge
        badge = "DEMON SLAYER EDITION"
        badge_line = Fore.LIGHTMAGENTA_EX + Style.BRIGHT + " " * 33 + "😈 " + badge + " 😈" + " " * 33
        print(badge_line)
        
        print("\n" + "="*90)
        print(Style.NORMAL + Fore.WHITE)
        
    def print_mini_banner(self):
        """Compact version for smaller terminals"""
        banner_color = Fore.LIGHTRED_EX
        text_color = Fore.LIGHTCYAN_EX
        
        print("\n" + "═" * 70)
        print(banner_color + Style.BRIGHT + " " * 20 + "🗡️ 冥忍 MYSŌNINJA 🗡️" + " " * 20)
        print(text_color + " " * 15 + "QUANTUM RED TEAM WARFARE PLATFORM" + " " * 15)
        print(Fore.LIGHTYELLOW_EX + " " * 18 + "FORGED BY MYSTERYAK & KNIGHTDALE" + " " * 18)
        print(Fore.LIGHTMAGENTA_EX + " " * 22 + "DEMON SLAYER EDITION" + " " * 22)
        print(Fore.LIGHTRED_EX + " " * 15 + "🥶 " + random.choice(self.slogans) + " 🥶" + " " * 15)
        print("═" * 70 + Style.NORMAL + Fore.WHITE + "\n")

def show_banner():
    """Main function to display the banner"""
    banner = DemonSlayerBanner()
    banner.print_banner()

def show_mini_banner():
    """Display compact banner"""
    banner = DemonSlayerBanner()
    banner.print_mini_banner()

if __name__ == "__main__":
    show_banner()
