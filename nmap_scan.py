# nmap_scan.py
import os

def run():
    target = input("\nEnter target IP/domain: ")
    print(f"\n[+] Running Nmap on {target}...\n")
    os.system(f"nmap -sV -T4 {target}")
