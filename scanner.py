import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# Lock for thread-safe printing
print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))

            if result == 0:
                try:
                    if port in [80, 8080]:
                        request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
                        sock.sendall(request.encode())
                    else:
                        sock.sendall(b"Hello\r\n")

                    banner = sock.recv(1024).decode(errors='ignore').strip().split('\n')[0]
                except:
                    banner = "No banner"

                with print_lock:
                    print(f"[+] Port {port} is open - {banner}")

    except Exception as e:
        with print_lock:
            print(f"[!] Error on port {port}: {e}")

def scan_ports(ip, start_port, end_port):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

def main():
    print("=== Python Port Scanner ===")
    host = input("Enter IP address or domain to scan (e.g., scanme.nmap.org): ").strip()

    # Try resolving host to IP
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("[!] Invalid domain or IP address. Exiting.")
        return

    try:
        start_port = int(input("Enter start port (e.g. 1): "))
        end_port = int(input("Enter end port (e.g. 1024): "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("[!] Invalid port range. Must be between 1 and 65535 and start < end.")
            return

    except ValueError:
        print("[!] Port must be an integer. Exiting.")
        return

    print(f"\n[*] Scanning {host} ({ip}) from port {start_port} to {end_port}...\n")
    scan_ports(ip, start_port, end_port)

if __name__ == "__main__":
    main()

