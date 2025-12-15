#!/usr/bin/env python3
# installer.py

import os
import sys
import subprocess
import shutil

def run_command(cmd):
    """Run shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def install_base_finder():
    print("""
    ┌─────────────────────────────────┐
    │      BASE FINDER INSTALLER      │
    │      GitHub: @KL_MODDER        │
    └─────────────────────────────────┘
    """)
    
    # Check if git exists
    code, _, _ = run_command("which git")
    if code != 0:
        print("[!] Git not found. Installing git...")
        run_command("pkg install git -y")
    
    # Clone repository
    print("[*] Cloning repository...")
    if os.path.exists("base-finder"):
        print("[*] Updating existing installation...")
        os.chdir("base-finder")
        run_command("git pull")
    else:
        run_command("git clone https://github.com/niketh-ai/base-finder.git")
        os.chdir("base-finder")
    
    # Install dependencies
    print("[*] Installing dependencies...")
    run_command("pip install requests beautifulsoup4 colorama")
    
    # Make executable
    os.chmod("scanner.py", 0o755)
    
    # Install to PATH
    print("[*] Installing to system PATH...")
    termux_bin = "/data/data/com.termux/files/usr/bin"
    shutil.copy("scanner.py", os.path.join(termux_bin, "base-finder"))
    os.chmod(os.path.join(termux_bin, "base-finder"), 0o755)
    
    print("\n[+] Installation complete!")
    print("\nUsage:")
    print("  base-finder https://example.com")
    print("\nUpdate with:")
    print("  cd ~/base-finder && git pull")

if __name__ == "__main__":
    install_base_finder()
