"""
Threat Detection Engine
ThreatWatch v2.0
"""

import time
from collections import defaultdict

from config.settings import (
    SYN_FLOOD_THRESHOLD,
    ICMP_FLOOD_THRESHOLD,
    PORT_SCAN_THRESHOLD,
    MAX_PACKET_SIZE,
)

# Store recent activity
syn_tracker = defaultdict(list)
icmp_tracker = defaultdict(list)
port_tracker = defaultdict(set)

TIME_WINDOW = 10  # seconds


class ThreatDetector:

    def detect(self, packet):

        alerts = []

        src = packet["src_ip"]
        now = time.time()

        # ----------------------------
        # Large Packet Detection
        # ----------------------------
        if packet["size"] > MAX_PACKET_SIZE:
            alerts.append({
                "type": "Large Packet",
                "severity": "LOW"
            })

        # ----------------------------
        # SYN Flood Detection
        # ----------------------------
        if packet["protocol"] == "TCP":

            if packet["flags"] == "S":

                syn_tracker[src].append(now)

                syn_tracker[src] = [
                    t for t in syn_tracker[src]
                    if now - t <= TIME_WINDOW
                ]

                if len(syn_tracker[src]) >= SYN_FLOOD_THRESHOLD:

                    alerts.append({
                        "type": "Possible SYN Flood",
                        "severity": "HIGH"
                    })

        # ----------------------------
        # ICMP Flood Detection
        # ----------------------------
        if packet["protocol"] == "ICMP":

            icmp_tracker[src].append(now)

            icmp_tracker[src] = [
                t for t in icmp_tracker[src]
                if now - t <= TIME_WINDOW
            ]

            if len(icmp_tracker[src]) >= ICMP_FLOOD_THRESHOLD:

                alerts.append({
                    "type": "Possible ICMP Flood",
                    "severity": "MEDIUM"
                })

        # ----------------------------
        # Port Scan Detection
        # ----------------------------
        if packet["dst_port"]:

            port_tracker[src].add(packet["dst_port"])

            if len(port_tracker[src]) >= PORT_SCAN_THRESHOLD:

                alerts.append({
                    "type": "Possible Port Scan",
                    "severity": "HIGH"
                })

        return alerts