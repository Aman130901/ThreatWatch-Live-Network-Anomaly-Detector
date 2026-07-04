"""
ThreatWatch Live Dashboard
"""

from collections import Counter
from rich.table import Table


class Dashboard:

    def __init__(self):

        self.total_packets = 0
        self.total_alerts = 0

        self.protocol_counter = Counter()
        self.ip_counter = Counter()

        self.latest_alert = "None"

    def update(self, packet):

        self.total_packets += 1

        self.protocol_counter[packet["protocol"]] += 1

        self.ip_counter[packet["src_ip"]] += 1

    def add_alert(self, alert):

        self.total_alerts += 1
        self.latest_alert = alert["type"]

    def generate_table(self):

        table = Table(title="🛡 ThreatWatch IDS Dashboard")

        table.add_column("Metric", style="cyan", width=25)
        table.add_column("Value", style="green")

        table.add_row("Packets Captured", str(self.total_packets))
        table.add_row("TCP", str(self.protocol_counter["TCP"]))
        table.add_row("UDP", str(self.protocol_counter["UDP"]))
        table.add_row("ICMP", str(self.protocol_counter["ICMP"]))
        table.add_row("Alerts", str(self.total_alerts))
        table.add_row("Latest Alert", self.latest_alert)

        if self.ip_counter:
            ip = self.ip_counter.most_common(1)[0][0]
        else:
            ip = "-"

        table.add_row("Most Active IP", ip)

        return table