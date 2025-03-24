import socket
import argparse

def scan_ports(target, ports):
    print(f"\nScanning {target} for open ports...\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout of 1 second
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target website or IP address")
    parser.add_argument("-p", "--ports", type=str, default="20-100",
                        help="Port range to scan (e.g., 20-100)")
    
    args = parser.parse_args()
    start_port, end_port = map(int, args.ports.split("-"))
    
    scan_ports(args.target, range(start_port, end_port + 1))
