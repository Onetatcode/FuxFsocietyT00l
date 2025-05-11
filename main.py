from banner import show_banner
from progress import loading_bar
from alert_bot import send_telegram
from log_utils import save_log
from usage_tracker import notify
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import os

console = Console()

TOOLS = {
    "1": ("Port Scanner", "port_scanner"),
    "2": ("Whois Lookup", "whois_lookup"),
    "3": ("Ping Host", "pinger"),
    "4": ("Nmap Scan", "nmap_scan"),
    "5": ("Metasploit Console", "metasploit_launcher"),
    "6": ("Reverse Engineering Tools", "reverse_tools"),
    "7": ("Web Exploitation", "web_exploit"),
    "8": ("Exit", None),
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_menu():
    console.print("\n[bold cyan]Main Menu[/bold cyan]")
    for key, (name, _) in TOOLS.items():
        console.print(f"[{key}] {name}")

def execute_tool(tool_module):
    try:
        mod = __import__(tool_module)
        mod.run()
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] Failed to run {tool_module}: {e}")

def main_menu():
    while True:
        clear_screen()
        show_banner()
        print_menu()
        choice = Prompt.ask("\n[bold green]Select an option[/bold green]", choices=TOOLS.keys())

        if choice == "8":
            console.print("\n[bold yellow]Exiting... fsociety out.[/bold yellow]")
            send_telegram("User exited fsociety tool.")
            break

        tool_name, tool_module = TOOLS[choice]
        console.print(Panel.fit(f"[bold magenta]Running:[/bold magenta] {tool_name}"))
        send_telegram(f"User ran: {tool_name}")
        execute_tool(tool_module)

if __name__ == "__main__":
    try:
        clear_screen()
        show_banner()
        loading_bar()
        notify()  # usage tracker ping
        send_telegram("fsociety CLI launched.")
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[red]Interrupted by user. Exiting...[/red]")
    except Exception as main_error:
        console.print(f"[bold red]Critical Error:[/bold red] {main_error}")
