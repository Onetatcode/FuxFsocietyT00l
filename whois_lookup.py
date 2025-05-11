import whois
import socket
from datetime import datetime

def run():
    domain = input("\nEnter domain (e.g., example.com) or IP (e.g., 192.168.1.1): ").strip()

    # Check if the input is a valid IP address
    try:
        socket.inet_aton(domain)
        is_ip = True
    except socket.error:
        is_ip = False

    # Get WHOIS information
    if is_ip:
        print(f"\n[+] Looking up WHOIS information for IP: {domain}\n")
        try:
            # Fetching the IP WHOIS info (we use a placeholder here)
            info = whois.whois(domain)
            print_whois_info(info)
        except Exception as e:
            print(f"[!] Error retrieving WHOIS info for IP: {e}")
    else:
        print(f"\n[+] Looking up WHOIS information for domain: {domain}\n")
        try:
            info = whois.whois(domain)
            print_whois_info(info)
        except Exception as e:
            print(f"[!] Error retrieving WHOIS info for domain: {e}")

def print_whois_info(info):
    """Prints WHOIS information in a more readable format."""
    
    print("\n--- WHOIS Info ---\n")
    
    # Check if information exists
    if not info:
        print("[!] No WHOIS information found.")
        return
    
    # Displaying WHOIS details
    try:
        print(f"Domain Name: {info.get('domain_name', 'N/A')}")
        print(f"Registrar: {info.get('registrar', 'N/A')}")
        print(f"Creation Date: {format_date(info.get('creation_date'))}")
        print(f"Expiration Date: {format_date(info.get('expiration_date'))}")
        print(f"Updated Date: {format_date(info.get('updated_date'))}")
        print(f"Nameservers: {', '.join(info.get('nameservers', ['N/A']))}")
        print(f"Status: {info.get('status', 'N/A')}")
        print(f"Registrant: {info.get('registrant', 'N/A')}")
        print(f"Admin: {info.get('admin', 'N/A')}")
        print(f"Tech: {info.get('tech', 'N/A')}")
    except Exception as e:
        print(f"[!] Error displaying WHOIS info: {e}")
    
def format_date(date_info):
    """Formats date information to a readable format."""
    if not date_info:
        return "N/A"
    
    if isinstance(date_info, list):
        return [d.strftime("%Y-%m-%d %H:%M:%S") if isinstance(d, datetime) else d for d in date_info]
    return date_info.strftime("%Y-%m-%d %H:%M:%S") if isinstance(date_info, datetime) else date_info

