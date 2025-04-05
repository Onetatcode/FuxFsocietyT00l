import base64

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key)) for c in data)

def run():
    data = input("Payload to obfuscate: ").strip()
    key = input("XOR key: ").strip()

    if not data or not key:
        print("[!] Invalid input")
        return

    xor_out = xor_encrypt(data, key)
    b64_out = base64.b64encode(xor_out.encode()).decode()

    print("\\n[+] XOR + Base64 Payload:\\n")
    print(b64_out)
