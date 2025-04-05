from banner import show_banner
from progress import loading_bar
from alert_bot import send_telegram
from log_utils import save_log
from usage_tracker import notify

def main_menu():
    print("\n[1] Port Scanner")
    print("[2] Whois Lookup")
    print("[3] Ping Host")
    print("[4] Nmap Scan")
    print("[5] Metasploit Console")
    print("[6] Reverse Engineering Tools")
    print("[7] Web Exploitation")
    print("[8] Exit")

    choice = input("\nSelect an option > ")
    
    if choice == '1':
        import port_scanner; port_scanner.run()
    elif choice == '2':
        import whois_lookup; whois_lookup.run()
    elif choice == '3':
        import pinger; pinger.run()
    elif choice == '4':
        import nmap_scan; nmap_scan.run()
    elif choice == '5':
        import metasploit_launcher; metasploit_launcher.run()
    elif choice == '6':
        import reverse_tools; reverse_tools.run()
    elif choice == '7':
        import web_exploit; web_exploit.run()
    elif choice == '8':
        print("\nExiting... fsociety out.\n")
        exit()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    from rich.console import Console
    console = Console()
    show_banner()
    loading_bar()
    notify()  # Usage tracking
    while True:
        main_menu()
