"""
ThreatWatch Logger
"""

import csv
import json
import logging
import os
from datetime import datetime

from config.settings import CSV_LOG, JSON_LOG

# Create logger
logging.basicConfig(
    filename="logs/threatwatch.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class ThreatLogger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        if not os.path.exists(CSV_LOG):
            with open(CSV_LOG, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow([
                    "Time",
                    "Severity",
                    "Source",
                    "Destination",
                    "Threat"
                ])

    def log(self, packet, alert):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # -------------------------
        # CSV
        # -------------------------

        with open(CSV_LOG, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                alert["severity"],
                packet["src_ip"],
                packet["dst_ip"],
                alert["type"]
            ])

        # -------------------------
        # JSON
        # -------------------------

        data = []

        if os.path.exists(JSON_LOG):

            try:
                with open(JSON_LOG, "r") as file:
                    data = json.load(file)

            except Exception:
                data = []

        data.append({

            "time": timestamp,
            "severity": alert["severity"],
            "source": packet["src_ip"],
            "destination": packet["dst_ip"],
            "threat": alert["type"]

        })

        with open(JSON_LOG, "w") as file:
            json.dump(data, file, indent=4)

        # -------------------------
        # Log File
        # -------------------------

        logging.warning(
            f"{alert['severity']} | {alert['type']} | "
            f"{packet['src_ip']} -> {packet['dst_ip']}"
        )