import nmap

# Create Nmap scanner object
scanner = nmap.PortScanner()

# ---------------- PACKET ANALYSIS FUNCTION ----------------
def analyze_packets(target):
    print("\nStarting Network Packet Analysis using Nmap...")
    print("-" * 60)

    # Perform TCP SYN scan (packet-based probing)
    scanner.scan(hosts=target, arguments='-sS -sV')

    for host in scanner.all_hosts():
        print("\nHost:", host)
        print("State:", scanner[host].state())

        for protocol in scanner[host].all_protocols():
            print("\nProtocol:", protocol.upper())

            ports = scanner[host][protocol].keys()
            for port in ports:
                port_info = scanner[host][protocol][port]

                print(f"Port        : {port}")
                print(f"State       : {port_info['state']}")
                print(f"Service     : {port_info['name']}")
                print(f"Version     : {port_info.get('version', 'N/A')}")
                print("-" * 30)


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    target_ip = input("Enter target IP or hostname: ")
    analyze_packets(target_ip)
