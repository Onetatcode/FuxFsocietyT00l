# pinger.py
import os

def run():
    host = input("\nEnter IP or domain to ping: ")
    os.system(f"ping -c 4 {host}")
