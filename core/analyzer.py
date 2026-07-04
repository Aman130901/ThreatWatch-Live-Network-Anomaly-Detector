"""
Packet Analyzer
ThreatWatch v2.0
"""

from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime


class PacketAnalyzer:

    def analyze(self, packet):

        if not packet.haslayer(IP):
            return None

        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "protocol": "OTHER",
            "size": len(packet),
            "ttl": packet[IP].ttl,
            "src_port": None,
            "dst_port": None,
            "flags": None
        }

        if packet.haslayer(TCP):
            data["protocol"] = "TCP"
            data["src_port"] = packet[TCP].sport
            data["dst_port"] = packet[TCP].dport
            data["flags"] = str(packet[TCP].flags)

        elif packet.haslayer(UDP):
            data["protocol"] = "UDP"
            data["src_port"] = packet[UDP].sport
            data["dst_port"] = packet[UDP].dport

        elif packet.haslayer(ICMP):
            data["protocol"] = "ICMP"

        return data