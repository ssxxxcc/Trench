#!/usr/bin/env python3
"""
TRENCH - Educational Security Awareness Tool
Created by: rbbt
Purpose: Educational cybersecurity demonstrations and awareness
WARNING: FOR EDUCATIONAL PURPOSES ONLY
"""

import os
import sys
import time
import random
import hashlib
import re
from colorama import init, Fore, Back, Style
import threading

# Initialize colorama for Windows compatibility
init(autoreset=True)

class TrenchTool:
    def __init__(self):
        self.version = "1.0.0"
        self.author = "Rabbit"
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def loading_animation(self, text="Loading", duration=3):
        """Display a loading animation"""
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        end_time = time.time() + duration
        
        while time.time() < end_time:
            for char in chars:
                print(f"\r{Fore.CYAN}{char} {text}...", end="", flush=True)
                time.sleep(0.1)
        print(f"\r{Fore.GREEN}✓ {text} complete!{' ' * 20}")
    
    def display_logo(self):
        """Display the ASCII logo"""
        # Unicode art logo
        logo = """
⠀⠀⠀⠀⠀⠀⢀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣦⡀⠘⣆⠈⠛⠻⣗⠶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⠈⠳⠄⠀⠈⠙⠶⣍⡻⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠻⣮⡹⣿⣿⣷⣦⣄⣀⠀⠀⢀⣸⠃⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣮⢿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢰⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⠀⠀⠀⠀⠀⠀⠀⣷⠀⢷⠀⠀⠀⠙⢷⣿⣿⣿⣿⣟⣋⣀⣤⣴⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⢿⣿⡀⠀⠀⢀⣀⣴⣾⡟⠀⠈⣇⠀⠀⠀⠈⢻⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡏⠸⣿⣿⣶⣾⣿⡿⠟⠋⠀⠀⠀⢹⡆⠀⠀⠀⠀⠹⡽⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⠀⠀⠀⣀⡿⠛⠉⠀⠀⢿⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠑⢹⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣷⣶⣾⠏⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⡿⠃⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⢀⠀⠹⣿⣿⣿⣿⣷⣶⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⢸⣿⠀⠀⠀⠀⢀⡞⠀⠀⠈⠛⠻⠿⠿⠯⠥⠤⢄⣀⣀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⢸⡇⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠈⠙⠂⠙⠳⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⡾⠁⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⡸⠃⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠇⠀⠀⠀⠃⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠙⠻⣿⣿⣿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⢀⡖⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⢸⣿⠀⠀⠈⢿⣿⣿⣿⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⣼⠁⠼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⣼⡇⠀⠀⣠⣾⣿⣿⣿⣿⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠘⣇⠀⠀⢻⡄⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⢀⣼⠏⠀⣠⣾⣿⣿⡿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠘⠂⠀⠀⢳⠀⢳⡀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⠃⠀⠀⠀⠀⣠⣾⠃⣠⣾⣿⣿⠿⠋⢰⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⢀⣀⡴⠞⠙⠲⣷⡄⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⢀⣀⣠⣤⣶⠿⠟⠋⠀⡾⠀⠀⠀⢀⣴⠟⠁⢠⡟⢱⡿⠃⠀⠀⠸⣇⡀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠟⠁⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⣸⠇⠀⠀⠀⣤⠟⠑⠋⠉⣿⠋⠉⠉⠉⠁⣠⠞⠀⠀⠀⡇⠀⠀⢠⡿⠋⠀⠀⠈⠁⡿⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⢀⣾⣏⣤⣶⡾⠛⠉⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⣠⠞⠁⠀⠀⠀⠀⣿⠀⠀⠀⢀⡼⠃⠀⠀⠀⢸⠇⠀⣰⠟⠀⠀⠀⠀⠀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⡾⠃⠀⠀⠀⢀⡞⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣶⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣾⠇⠀⠀⠀⢀⣾⣣⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⢠⡟⠀⠀⠀⢀⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡄⢀⣀⡀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣾⠇⠀⠀⣰⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⣾⠀⣰⠟⠀⢀⣼⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⠿⠿⠿⠿⠃⠀⠀⠀⢸⣿⣶⠏⢀⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠃⢠⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⢃⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣧⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠁⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """
        
        try:
            print(Fore.RED + logo)
        except UnicodeEncodeError:
            # Fallback to simple text logo if Unicode fails
            fallback_logo = """
  TTTTTTTT RRRRRR  EEEEEEE N    N  CCCCC  H    H
     TT    R    R  E       NN   N  C      H    H
     TT    RRRRRR  EEEEE   N N  N  C      HHHHHH
     TT    R   R   E       N  N N  C      H    H
     TT    R    R  EEEEEEE N   NN  CCCCC  H    H
            """
            print(Fore.RED + fallback_logo)
        print(f"{Fore.CYAN}{'='*80}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}                    TRENCH - Educational Security Tool")
        print(f"{Fore.GREEN}                           Created by: {self.author}")
        print(f"{Fore.MAGENTA}                            Version: {self.version}")
        print(f"{Fore.CYAN}{'='*80}")
        print(f"{Fore.RED}{Style.BRIGHT}                    WARNING: FOR EDUCATIONAL PURPOSES ONLY")
        print(f"{Fore.CYAN}{'='*80}\n")
    
    def display_warning(self):
        """Display important warnings and disclaimers"""
        warnings = [
            "WARNING: This tool is for EDUCATIONAL PURPOSES ONLY",
            "WARNING: Do NOT use this tool for illegal activities",
            "WARNING: Always obtain proper authorization before testing",
            "WARNING: The author is not responsible for misuse",
            "WARNING: Use only on systems you own or have permission to test"
        ]
        
        print(f"{Fore.RED}{Style.BRIGHT}IMPORTANT WARNINGS:")
        for warning in warnings:
            print(f"{Fore.YELLOW}  {warning}")
        print()
    
    def display_help(self):
        """Display help information"""
        help_text = f"""
{Fore.CYAN}{Style.BRIGHT}TRENCH - Educational Security Tool Help

{Fore.GREEN}Available Commands:
{Fore.YELLOW}  1. Password Analyzer    - Analyze password strength
{Fore.YELLOW}  2. Security Demo        - Educational security demonstrations
{Fore.YELLOW}  3. Network Info         - Display local network information
{Fore.YELLOW}  4. Hash Generator       - Generate various hash types
{Fore.YELLOW}  5. Help                 - Show this help menu
{Fore.YELLOW}  6. Exit                 - Exit the program

{Fore.RED}Educational Purpose:
{Fore.WHITE}This tool demonstrates security concepts through simulation and analysis.
It does not perform actual attacks or unauthorized access attempts.

{Fore.RED}Ethical Guidelines:
{Fore.WHITE}• Only use on systems you own or have explicit permission to test
• Follow responsible disclosure practices
• Respect privacy and legal boundaries
• Use knowledge gained for defensive purposes

{Fore.CYAN}For more information, visit cybersecurity educational resources.
        """
        print(help_text)
    
    def password_analyzer(self):
        """Analyze password strength"""
        print(f"{Fore.CYAN}{Style.BRIGHT}Password Strength Analyzer")
        print(f"{Fore.YELLOW}Enter a password to analyze (input will be hidden):")
        
        import getpass
        password = getpass.getpass("Password: ")
        
        if not password:
            print(f"{Fore.RED}No password entered!")
            return
        
        self.loading_animation("Analyzing password", 2)
        
        # Analyze password strength
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 2
            feedback.append(f"{Fore.GREEN}✓ Length is adequate (8+ characters)")
        else:
            feedback.append(f"{Fore.RED}✗ Too short (less than 8 characters)")
        
        if re.search(r'[a-z]', password):
            score += 1
            feedback.append(f"{Fore.GREEN}✓ Contains lowercase letters")
        else:
            feedback.append(f"{Fore.RED}✗ Missing lowercase letters")
        
        if re.search(r'[A-Z]', password):
            score += 1
            feedback.append(f"{Fore.GREEN}✓ Contains uppercase letters")
        else:
            feedback.append(f"{Fore.RED}✗ Missing uppercase letters")
        
        if re.search(r'\d', password):
            score += 1
            feedback.append(f"{Fore.GREEN}✓ Contains numbers")
        else:
            feedback.append(f"{Fore.RED}✗ Missing numbers")
        
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 2
            feedback.append(f"{Fore.GREEN}✓ Contains special characters")
        else:
            feedback.append(f"{Fore.RED}✗ Missing special characters")
        
        # Determine strength
        if score >= 6:
            strength = f"{Fore.GREEN}STRONG"
        elif score >= 4:
            strength = f"{Fore.YELLOW}MODERATE"
        else:
            strength = f"{Fore.RED}WEAK"
        
        print(f"\n{Fore.CYAN}Password Analysis Results:")
        print(f"{Fore.WHITE}Strength: {strength}")
        print(f"{Fore.WHITE}Score: {score}/7")
        print(f"\n{Fore.CYAN}Feedback:")
        for item in feedback:
            print(f"  {item}")
        
        # Educational information
        print(f"\n{Fore.MAGENTA}Educational Tips:")
        print(f"{Fore.WHITE}• Use a mix of uppercase, lowercase, numbers, and symbols")
        print(f"{Fore.WHITE}• Avoid common words and personal information")
        print(f"{Fore.WHITE}• Consider using a passphrase with random words")
        print(f"{Fore.WHITE}• Use a password manager for unique passwords")
        print()
    
    def security_demo(self):
        """Educational security demonstrations"""
        print(f"{Fore.CYAN}{Style.BRIGHT}Security Awareness Demonstrations")
        print(f"{Fore.YELLOW}Select a demonstration:")
        print(f"{Fore.WHITE}1. Common Password Patterns")
        print(f"{Fore.WHITE}2. Social Engineering Awareness")
        print(f"{Fore.WHITE}3. Phishing Email Examples")
        print(f"{Fore.WHITE}4. Back to main menu")
        
        choice = input(f"{Fore.GREEN}Enter choice (1-4): ").strip()
        
        if choice == "1":
            self.demo_passwords()
        elif choice == "2":
            self.demo_social_engineering()
        elif choice == "3":
            self.demo_phishing()
        elif choice == "4":
            return
        else:
            print(f"{Fore.RED}Invalid choice!")
    
    def demo_passwords(self):
        """Demonstrate common password patterns"""
        print(f"{Fore.CYAN}{Style.BRIGHT}Common Password Patterns Demo")
        self.loading_animation("Loading password database", 2)
        
        weak_patterns = [
            "123456", "password", "123456789", "12345678", "12345",
            "1234567", "1234567890", "qwerty", "abc123", "Password1"
        ]
        
        print(f"\n{Fore.RED}Top 10 Most Common (Weak) Passwords:")
        for i, pwd in enumerate(weak_patterns, 1):
            print(f"{Fore.YELLOW}{i:2d}. {pwd}")
        
        print(f"\n{Fore.MAGENTA}Why these are dangerous:")
        print(f"{Fore.WHITE}• Easily guessed by attackers")
        print(f"{Fore.WHITE}• Found in common password dictionaries")
        print(f"{Fore.WHITE}• Can be cracked in seconds")
        print(f"{Fore.WHITE}• Used by millions of people")
        
        print(f"\n{Fore.GREEN}Better alternatives:")
        print(f"{Fore.WHITE}• Use random password generators")
        print(f"{Fore.WHITE}• Create passphrases: 'Coffee!Mountain$Blue7'")
        print(f"{Fore.WHITE}• Enable two-factor authentication")
        print()
    
    def demo_social_engineering(self):
        """Demonstrate social engineering awareness"""
        print(f"{Fore.CYAN}{Style.BRIGHT}Social Engineering Awareness")
        self.loading_animation("Preparing scenarios", 2)
        
        scenarios = [
            {
                "title": "Pretexting Phone Call",
                "description": "Caller claims to be from IT support, asks for password",
                "red_flags": ["Unsolicited call", "Urgency tactics", "Asking for credentials"],
                "response": "Verify identity through official channels before sharing info"
            },
            {
                "title": "Tailgating",
                "description": "Someone follows you into a secure building",
                "red_flags": ["No visible badge", "Carrying large items", "Friendly conversation"],
                "response": "Politely ask to see their badge or direct them to reception"
            },
            {
                "title": "USB Drop Attack",
                "description": "Finding a USB drive in parking lot labeled 'Salary Info'",
                "red_flags": ["Unknown device", "Enticing label", "Found in public area"],
                "response": "Never plug unknown devices into your computer"
            }
        ]
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n{Fore.YELLOW}Scenario {i}: {scenario['title']}")
            print(f"{Fore.WHITE}{scenario['description']}")
            print(f"{Fore.RED}Red Flags: {', '.join(scenario['red_flags'])}")
            print(f"{Fore.GREEN}Proper Response: {scenario['response']}")
        
        print(f"\n{Fore.MAGENTA}Remember: When in doubt, verify through official channels!")
        print()
    
    def demo_phishing(self):
        """Demonstrate phishing email awareness"""
        print(f"{Fore.CYAN}{Style.BRIGHT}Phishing Email Awareness")
        self.loading_animation("Analyzing email patterns", 2)
        
        print(f"\n{Fore.RED}Common Phishing Indicators:")
        indicators = [
            "Generic greetings ('Dear Customer')",
            "Urgent action required",
            "Suspicious sender addresses",
            "Grammar and spelling errors",
            "Requests for personal information",
            "Threatening consequences",
            "Suspicious links or attachments"
        ]
        
        for indicator in indicators:
            print(f"{Fore.YELLOW}• {indicator}")
        
        print(f"\n{Fore.GREEN}How to Verify Legitimate Emails:")
        print(f"{Fore.WHITE}• Check sender's email address carefully")
        print(f"{Fore.WHITE}• Hover over links to see actual destination")
        print(f"{Fore.WHITE}• Contact organization through official channels")
        print(f"{Fore.WHITE}• Look for personalized information")
        print(f"{Fore.WHITE}• Be suspicious of urgent requests")
        print()
    
    def network_info(self):
        """Display local network information"""
        print(f"{Fore.CYAN}{Style.BRIGHT}Local Network Information")
        self.loading_animation("Gathering network data", 2)
        
        try:
            import socket
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            
            print(f"\n{Fore.GREEN}System Information:")
            print(f"{Fore.WHITE}Hostname: {hostname}")
            print(f"{Fore.WHITE}Local IP: {local_ip}")
            
            # Get network interfaces (Windows)
            if os.name == 'nt':
                import subprocess
                result = subprocess.run(['ipconfig'], capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"\n{Fore.YELLOW}Network Interfaces:")
                    lines = result.stdout.split('\n')
                    for line in lines[:15]:  # Show first 15 lines
                        if line.strip():
                            print(f"{Fore.WHITE}{line}")
            
        except Exception as e:
            print(f"{Fore.RED}Error gathering network info: {e}")
        
        print(f"\n{Fore.MAGENTA}Educational Note:")
        print(f"{Fore.WHITE}This information is only about YOUR local system.")
        print(f"{Fore.WHITE}Never attempt to scan or access other systems without permission.")
        print()
    
    def hash_generator(self):
        """Generate various hash types"""
        print(f"{Fore.CYAN}{Style.BRIGHT}Hash Generator")
        text = input(f"{Fore.YELLOW}Enter text to hash: ").strip()
        
        if not text:
            print(f"{Fore.RED}No text entered!")
            return
        
        self.loading_animation("Generating hashes", 1)
        
        # Generate different hash types
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        sha1_hash = hashlib.sha1(text.encode()).hexdigest()
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()
        
        print(f"\n{Fore.GREEN}Hash Results for: '{text}'")
        print(f"{Fore.YELLOW}MD5:    {Fore.WHITE}{md5_hash}")
        print(f"{Fore.YELLOW}SHA1:   {Fore.WHITE}{sha1_hash}")
        print(f"{Fore.YELLOW}SHA256: {Fore.WHITE}{sha256_hash}")
        
        print(f"\n{Fore.MAGENTA}Educational Info:")
        print(f"{Fore.WHITE}• MD5 and SHA1 are considered weak for security")
        print(f"{Fore.WHITE}• SHA256 is currently considered secure")
        print(f"{Fore.WHITE}• Hashes are one-way functions")
        print(f"{Fore.WHITE}• Used for data integrity and password storage")
        print()
    
    def main_menu(self):
        """Display main menu and handle user input"""
        while True:
            print(f"{Fore.CYAN}{Style.BRIGHT}Main Menu:")
            print(f"{Fore.WHITE}1. Password Analyzer")
            print(f"{Fore.WHITE}2. Security Demonstrations")
            print(f"{Fore.WHITE}3. Network Information")
            print(f"{Fore.WHITE}4. Hash Generator")
            print(f"{Fore.WHITE}5. Help")
            print(f"{Fore.WHITE}6. Exit")
            
            choice = input(f"\n{Fore.GREEN}Select option (1-6): ").strip()
            
            if choice == "1":
                self.password_analyzer()
            elif choice == "2":
                self.security_demo()
            elif choice == "3":
                self.network_info()
            elif choice == "4":
                self.hash_generator()
            elif choice == "5":
                self.display_help()
            elif choice == "6":
                print(f"{Fore.YELLOW}Thanks for using TRENCH!")
                print(f"{Fore.GREEN}Remember: Use your knowledge responsibly!")
                break
            else:
                print(f"{Fore.RED}Invalid choice! Please select 1-6.")
            
            input(f"\n{Fore.CYAN}Press Enter to continue...")
            self.clear_screen()
            self.display_logo()
    
    def run(self):
        """Main program entry point"""
        self.clear_screen()
        self.display_logo()
        self.display_warning()
        
        print(f"{Fore.YELLOW}Welcome to TRENCH - Educational Security Tool")
        print(f"{Fore.WHITE}Type 'help' or select option 5 for guidance\n")
        
        self.main_menu()

def main():
    """Program entry point"""
    try:
        tool = TrenchTool()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Program interrupted by user.")
    except Exception as e:
        print(f"\n{Fore.RED}An error occurred: {e}")

if __name__ == "__main__":
    main()