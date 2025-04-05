# reverse_tools.py
import os

def run():
    binary = input("\nEnter path to binary file: ")
    print("\n[+] Extracting Strings...\n")
    os.system(f"strings {binary}")
    print("\n[+] Checking ELF Headers...\n")
    os.system(f"readelf -h {binary}")
