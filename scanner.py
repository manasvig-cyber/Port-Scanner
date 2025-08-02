import socket
import threading
from concurrent.futures import ThreadPoolExecutor

print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            try:
                # Send proper HTTP request for port 80/8080
                if port in [80, 8080]:
                    request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
                    sock.sendall(request.encode())
                else:
                    sock.sendall(b"Hello\r\n")

                # Read and clean the banner
                banner = sock.recv(1024).decode(errors='ignore').strip().split('\n')[0]
            except:
                banner = "No banner"

            with print_lock:
                print(f"[+] Port {port} is open - {banner}")
        sock.close()

    except Exception as e:
        with print_lock:
            print(f"[!] Error on port {port}: {e}")

def scan_ports(ip, start_port, end_port):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

def main():
    print("=== Python Port Scanner ===")
    ip = input("Enter IP address to scan (e.g., scanme.nmap.org): ").strip()

    try:
        start_port = int(input("Enter start port (e.g. 1): "))
        end_port = int(input("Enter end port (e.g. 1024): "))
    except ValueError:
        print("Please enter valid port numbers.")
        return

    print(f"\n[*] Scanning {ip} from port {start_port} to {end_port}...\n")
    scan_ports(ip, start_port, end_port)

if __name__ == "__main__":
    main()

