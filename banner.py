from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_banner():
    banner_text = r"""
 ██████╗ ███╗   ██╗███████╗████████╗ █████╗ ████████╗███╗   ███╗███████╗███╗   ██╗
██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝████╗ ████║██╔════╝████╗  ██║
██║   ██║██╔██╗ ██║█████╗     ██║   ███████║   ██║   ██╔████╔██║█████╗  ██╔██╗ ██║
██║   ██║██║╚██╗██║██╔══╝     ██║   ██╔══██║   ██║   ██║╚██╔╝██║██╔══╝  ██║╚██╗██║
╚██████╔╝██║ ╚████║███████╗   ██║   ██║  ██║   ██║   ██║ ╚═╝ ██║███████╗██║ ╚████║
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝

                      [ Inspired by Mr. Robot and Watch Dogs ]
    """
    
    console.print(Panel(Text(banner_text, justify="center", style="bold cyan"), 
                        title="[bold red]ONETATMEN", 
                        subtitle="[green]Ethical OSINT Recon Tool", 
                        border_style="bright_magenta"))

