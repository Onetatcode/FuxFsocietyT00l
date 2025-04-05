#!/bin/bash
echo "[*] Installing system tools..."

sudo apt update
sudo apt install -y nmap metasploit-framework dirb nikto binutils

echo "[*] Installing Python dependencies..."
pip3 install -r requirements.txt

echo "[+] Setup complete. You can now run ./fsociety"