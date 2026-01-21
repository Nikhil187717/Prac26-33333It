import socket
import requests

# ---------------- PORT SCANNING ----------------
def port_scanner():
    target = input("Enter target IP or hostname: ")
    ports = [21, 22, 23, 80, 443, 3306]

    print("\n--- Port Scanning Results ---")
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")

            s.close()
        except Exception as e:
            print("Error scanning port", port, ":", e)


# ---------------- BANNER GRABBING ----------------
def banner_grabbing():
    host = input("Enter target host: ")
    port = int(input("Enter port number: "))

    print("\n--- Banner Grabbing Result ---")
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))
        banner = s.recv(1024)
        print("Banner Information:")
        print(banner.decode(errors="ignore"))
        s.close()
    except Exception as e:
        print("Unable to grab banner:", e)


# ---------------- DIRECTORY ENUMERATION ----------------
def directory_enum():
    url = input("Enter website URL (https://example.com): ")
    directories = ["admin", "login", "backup", "test", "uploads"]

    print("\n--- Directory Enumeration Results ---")
    for directory in directories:
        full_url = url.rstrip("/") + "/" + directory
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                print(f"[FOUND] {full_url}")
            else:
                print(f"[NOT FOUND] {full_url}")
        except requests.exceptions.RequestException:
            print(f"[ERROR] {full_url}")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n" + "=" * 50)
        print(" SIMPLE PENETRATION TESTING TOOL ")
        print("=" * 50)
        print("1. Port Scanning")
        print("2. Banner Grabbing")
        print("3. Directory Enumeration")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            banner_grabbing()
        elif choice == "3":
            directory_enum()
        elif choice == "4":
            print("Exiting program. Stay ethical! 🛡️")
            break
        else:
            print("Invalid choice. Try again.")


# ---------------- PROGRAM START ----------------
if __name__ == "__main__":
    main()
