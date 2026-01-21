import nmap

scanner = nmap.PortScanner()

# ---------------- PORT SCAN ----------------
def port_scan(target):
    print("\nRunning Port Scan...")
    scanner.scan(target, arguments='-F')

    for host in scanner.all_hosts():
        print("\nHost:", host)
        print("State:", scanner[host].state())

        for proto in scanner[host].all_protocols():
            print("Protocol:", proto)

            ports = scanner[host][proto].keys()
            for port in ports:
                state = scanner[host][proto][port]['state']
                print(f"Port {port} : {state}")


# ---------------- SERVICE VERSION SCAN ----------------
def service_scan(target):
    print("\nRunning Service Version Scan...")
    scanner.scan(target, arguments='-sV')

    for host in scanner.all_hosts():
        print("\nHost:", host)

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()

            for port in ports:
                service = scanner[host][proto][port]['name']
                version = scanner[host][proto][port].get('version', 'N/A')
                print(f"Port {port} : {service} {version}")


# ---------------- OS DETECTION ----------------
def os_detection(target):
    print("\nRunning OS Detection...")
    scanner.scan(target, arguments='-O')

    for host in scanner.all_hosts():
        if 'osmatch' in scanner[host]:
            for os in scanner[host]['osmatch']:
                print("OS Detected:", os['name'])
        else:
            print("OS Detection failed")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n" + "=" * 50)
        print(" BASIC PENETRATION TESTING USING NMAP ")
        print("=" * 50)
        print("1. Port Scan")
        print("2. Service Version Detection")
        print("3. OS Detection")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        target = input("Enter target IP or hostname: ")

        if choice == "1":
            port_scan(target)
        elif choice == "2":
            service_scan(target)
        elif choice == "3":
            os_detection(target)
        elif choice == "4":
            print("Exiting program. Use ethically! 🛡️")
            break
        else:
            print("Invalid choice")


# ---------------- PROGRAM START ----------------
if __name__ == "__main__":
    main()
