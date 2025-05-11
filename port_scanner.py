import socket
import threading
import re
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def is_valid_ip(ip):
    """Validate if the given string is a valid IP address."""
    regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(regex, ip) is not None

def scan_port(target, port):
    """Scan a single port on the target."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        console.print(f"[bold green][+] Port {port} is open[/bold green]")
    sock.close()

def run():
    target = Prompt.ask("[bold green]Enter target IP[/bold green]").strip()

    # Validate the IP address
    if not is_valid_ip(target):
        console.print("[bold red][!] Invalid IP format![/bold red]")
        return

    # Get port range from the user
    start_port = Prompt.ask("[bold green]Enter start port[/bold green]", default="1", type=int)
    end_port = Prompt.ask("[bold green]Enter end port[/bold green]", default="1024", type=int)

    # Display the target and port range being scanned
    console.print(Panel.fit(f"[bold green]Scanning {target} from port {start_port} to port {end_port}...[/bold green]"))

    # Create threads to scan multiple ports concurrently
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    console.print(f"[bold blue]Port scanning completed for {target}.[/bold blue]")

if __name__ == "__main__":
    run()
