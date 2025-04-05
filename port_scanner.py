# port_scanner.py
import socket

def run():
    target = input("\nEnter target IP: ")
    print(f"Scanning {target}...\n")
    for port in range(1, 100):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
