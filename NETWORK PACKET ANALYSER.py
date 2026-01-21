from scapy.all import sniff, IP, TCP, UDP, ICMP

# ---------------- PACKET ANALYSIS FUNCTION ----------------
def analyze_packet(packet):
    print("\n" + "=" * 60)

    # Check for IP packet
    if IP in packet:
        ip_layer = packet[IP]
        print("Protocol   :", ip_layer.proto)
        print("Source IP  :", ip_layer.src)
        print("Dest IP    :", ip_layer.dst)

        # TCP Packet
        if TCP in packet:
            tcp_layer = packet[TCP]
            print("Protocol   : TCP")
            print("Source Port:", tcp_layer.sport)
            print("Dest Port  :", tcp_layer.dport)

        # UDP Packet
        elif UDP in packet:
            udp_layer = packet[UDP]
            print("Protocol   : UDP")
            print("Source Port:", udp_layer.sport)
            print("Dest Port  :", udp_layer.dport)

        # ICMP Packet
        elif ICMP in packet:
            print("Protocol   : ICMP")

    else:
        print("Non-IP Packet Captured")

# ---------------- START PACKET CAPTURE ----------------
print("Starting packet capture... (Press Ctrl+C to stop)")
sniff(prn=analyze_packet, count=20)
