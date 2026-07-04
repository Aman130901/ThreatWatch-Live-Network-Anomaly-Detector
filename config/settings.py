"""
ThreatWatch Configuration
Author: Aman Sonkar
"""

# -----------------------------
# Application
# -----------------------------
APP_NAME = "ThreatWatch"
VERSION = "2.0"

# -----------------------------
# Network
# -----------------------------
INTERFACE = None      # Example: "eth0" or "wlan0"
PROMISCUOUS_MODE = True

# -----------------------------
# Packet Capture
# -----------------------------
STORE_PACKETS = False
MAX_PACKET_SIZE = 1500

# -----------------------------
# Detection Thresholds
# -----------------------------
SYN_FLOOD_THRESHOLD = 50
ICMP_FLOOD_THRESHOLD = 50
PORT_SCAN_THRESHOLD = 20

# -----------------------------
# Logging
# -----------------------------
CSV_LOG = "logs/alerts.csv"
JSON_LOG = "logs/alerts.json"

# -----------------------------
# Reports
# -----------------------------
HTML_REPORT = "reports/report.html"

# -----------------------------
# Dashboard
# -----------------------------
REFRESH_RATE = 1