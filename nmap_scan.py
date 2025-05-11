import os
import re
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def is_valid_ip(ip):
    """Validate if the given string is a valid IP address."""
    regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(regex, ip) is not None

def is_valid_domain(domain):
    """Validate if the given string is a valid domain name."""
    regex = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(regex, domain) is not None

def run():
    target = Prompt.ask("\nEnter target IP/domain", default="localhost")

    # Validate target
    if not (is_valid_ip(target) or is_valid_domain(target)):
        console.print("[bold red][!] Invalid IP or domain format![/bold red]")
        return

    console.print(Panel.fit(f"[bold green]Running Nmap on {target}...[/bold green]"))

    # Build Nmap command
    nmap_command = f"nmap -sV -T4 {target}"
    
    try:
        # Execute Nmap scan
        os.system(nmap_command)
        console.print(f"[bold blue]Scan completed for {target}.[/bold blue]")
    except Exception as e:
        console.print(f"[bold red][!] Error occurred while running Nmap:[/bold red] {e}")
