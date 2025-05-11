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
    host = Prompt.ask("[bold green]Enter IP or domain to ping[/bold green]").strip()

    # Validate input
    if not (is_valid_ip(host) or is_valid_domain(host)):
        console.print("[bold red][!] Invalid IP or domain format![/bold red]")
        return

    # Ask user for number of packets
    packet_count = Prompt.ask("[bold green]Number of packets to send[/bold green]", default="4", type=int)

    # Check if the system is Windows or Unix-based (Linux/macOS)
    if os.name == "nt":  # For Windows
        cmd = f"ping -n {packet_count} {host}"
    else:  # For Linux/macOS
        cmd = f"ping -c {packet_count} {host}"

    console.print(Panel.fit(f"[bold green]Pinging {host} with {packet_count} packets...[/bold green]"))

    # Execute the ping command
    os.system(cmd)

    console.print(f"[bold blue]Ping completed for {host}.[/bold blue]")

if __name__ == "__main__":
    run()
