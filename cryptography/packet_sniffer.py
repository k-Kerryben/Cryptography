
# Network Packet Sniffer
#work on  this file tomorrow.. I need to understand it better.


import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP, ICMP
import argparse
import sys

def analyze_packet(packet):
    """Analyze and display packet information"""
    
    #Check if packet has IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        #Determine protocol name
        protocol_map = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        protocol_name = protocol_map.get(protocol, f"Unknown({protocol})")
        
        #Print basic IP information
        print(f"\n[+] {ip_src} -> {ip_dst} | Protocol: {protocol_name}")
        
        #Analyze transport layer protocols
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"    TCP Port {src_port} -> {dst_port}")
            
            #Display payload if exists
            if packet[TCP].payload:
                payload = bytes(packet[TCP].payload)
                if payload:
                    print(f"    Payload: {payload[:50]}{'...' if len(payload) > 50 else ''}")
                    
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"    UDP Port {src_port} -> {dst_port}")
            
            # Display payload if exists
            if packet[UDP].payload:
                payload = bytes(packet[UDP].payload)
                if payload:
                    print(f"    Payload: {payload[:50]}{'...' if len(payload) > 50 else ''}")
                    
        elif ICMP in packet:
            icmp_type = packet[ICMP].type
            print(f"    ICMP Type: {icmp_type}")

def start_sniffer(interface=None, count=0):
    """Start packet capturing"""
    print("[*] Starting packet sniffer...")
    if interface:
        print(f"[*] Listening on interface: {interface}")
    else:
        print("[*] Listening on all interfaces")
        
    try:
        # Start sniffing
        scapy.sniff(
            iface=interface,
            prn=analyze_packet,
            count=count,  # 0 means infinite
            store=False   # Don't store packets in memory
        )
    except KeyboardInterrupt:
        print("\n[!] Stopping sniffer...")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Packet Sniffer")
    parser.add_argument(
        "-i", "--interface",
        help="Network interface to sniff (e.g., eth0, wlan0)",
        default=None
    )
    parser.add_argument(
        "-c", "--count",
        type=int,
        help="Number of packets to capture (0 for infinite)",
        default=0
    )
    
    args = parser.parse_args()
    
    # Verify we have necessary permissions
    try:
        # Test if we can capture packets
        pkts = scapy.sniff(count=1, timeout=1)
    except PermissionError:
        print("[!] Permission error: Try running with sudo")
        sys.exit(1)
    
    start_sniffer(args.interface, args.count)
