import os
import shutil
from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.print(Panel.fit("[bold green]Launching Metasploit Framework Console...[/bold green]"))

    # Check if msfconsole is available in PATH
    if shutil.which("msfconsole") is None:
        console.print("[bold red][!] Metasploit is not installed or not in your PATH.[/bold red]")
        console.print("Install it from [cyan]https://docs.rapid7.com/metasploit/[/cyan] or run:\n[bold]sudo apt install metasploit-framework[/bold]")
        return

    try:
        os.system("msfconsole")
    except Exception as e:
        console.print(f"[red][!] Failed to launch msfconsole:[/red] {e}")
