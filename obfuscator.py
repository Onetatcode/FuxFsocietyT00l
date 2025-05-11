import base64
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def xor_encrypt(data, key):
    """Encrypt the data using XOR cipher with the provided key."""
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def xor_decrypt(data, key):
    """Decrypt the data using XOR cipher with the provided key."""
    return xor_encrypt(data, key)  # XOR decryption is the same as encryption

def run():
    # Get user input
    data = Prompt.ask("[bold green]Payload to obfuscate[/bold green]").strip()
    key = Prompt.ask("[bold green]XOR key[/bold green]").strip()

    # Validate input
    if not data or not key:
        console.print("[bold red][!] Invalid input. Data and key are required![/bold red]")
        return

    # XOR encryption
    xor_out = xor_encrypt(data, key)
    console.print(f"[bold yellow]XOR Encryption Output:[/bold yellow]\n{xor_out}")

    # Base64 encoding
    b64_out = base64.b64encode(xor_out.encode()).decode()
    console.print(f"\n[bold cyan]Base64 Obfuscated Payload:[/bold cyan]\n{b64_out}")

    # Ask if user wants to reverse the process
    reverse = Prompt.ask("\n[bold green]Would you like to reverse the obfuscation (y/n)?[/bold green]", choices=["y", "n"], default="n")
    
    if reverse == "y":
        # Base64 decoding
        decoded_b64 = base64.b64decode(b64_out).decode()
        # XOR decryption
        decrypted_payload = xor_decrypt(decoded_b64, key)
        console.print(f"\n[bold red]Decrypted Payload (after reverse process):[/bold red]\n{decrypted_payload}")

if __name__ == "__main__":
    run()
