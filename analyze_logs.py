def analyze_logs(file_path):
    suspicious_ips = {}
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 3:
                ip = parts[0]
                status = parts[2]
                if status != "200":
                    suspicious_ips[ip] = suspicious_ips.get(ip, 0) + 1
    print("Suspicious IPs detected (non-200 responses):")
    for ip, count in suspicious_ips.items():
        print(f"{ip}: {count} times")

if __name__ == "__main__":
    file_path = input("Enter log file path: ")
    analyze_logs(file_path)