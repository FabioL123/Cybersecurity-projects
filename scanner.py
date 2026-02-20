import socket

def scan_host(ip):
    open_ports = []
    for port in range(20, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    ip = input("Enter IP address to scan: ")
    ports = scan_host(ip)
    print(f"Open ports on {ip}: {ports}")