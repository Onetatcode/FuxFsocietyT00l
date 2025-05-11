import os
import subprocess

def check_binary_exists(binary):
    """Check if the binary file exists."""
    return os.path.isfile(binary)

def run():
    # Input path to binary file
    binary = input("\nEnter the full path to the binary file: ").strip()

    if not binary:
        print("[!] No binary file provided. Exiting...\n")
        return

    # Check if binary file exists
    if not check_binary_exists(binary):
        print(f"[!] The binary file '{binary}' does not exist. Please check the path.\n")
        return

    print("\n[+] Starting reverse engineering tools...\n")

    # Extract strings from the binary
    print("[+] Extracting strings...\n")
    try:
        strings_output = subprocess.check_output(f"strings {binary}", shell=True, stderr=subprocess.PIPE).decode()
        print(strings_output)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error extracting strings: {e.stderr.decode()}\n")

    # Checking ELF headers (if it's an ELF binary)
    if binary.endswith(".elf"):
        print("\n[+] Checking ELF headers...\n")
        try:
            readelf_output = subprocess.check_output(f"readelf -h {binary}", shell=True, stderr=subprocess.PIPE).decode()
            print(readelf_output)
        except subprocess.CalledProcessError as e:
            print(f"[!] Error reading ELF headers: {e.stderr.decode()}\n")
    else:
        print(f"[!] The binary '{binary}' is not an ELF file. Skipping ELF header check.\n")

    print("\n[+] Reverse engineering complete!\n")

