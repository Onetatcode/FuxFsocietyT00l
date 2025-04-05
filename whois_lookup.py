# whois_lookup.py
import whois

def run():
    domain = input("\nEnter domain (e.g. example.com): ")
    info = whois.whois(domain)
    print("\n--- WHOIS Info ---")
    print(info)
