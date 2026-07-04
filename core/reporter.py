"""
ThreatWatch HTML Report Generator
"""

from datetime import datetime
from pathlib import Path


class ReportGenerator:

    def generate(self, dashboard):

        Path("reports").mkdir(exist_ok=True)

        html = f"""
<!DOCTYPE html>
<html>
<head>
<title>ThreatWatch Report</title>

<style>

body {{
    font-family: Arial;
    background:#f4f4f4;
    padding:40px;
}}

table {{
    border-collapse:collapse;
    width:60%;
}}

td,th {{
    border:1px solid #ccc;
    padding:10px;
}}

th {{
    background:#1f77b4;
    color:white;
}}

</style>

</head>

<body>

<h1>ThreatWatch IDS Report</h1>

<p><b>Generated:</b> {datetime.now()}</p>

<table>

<tr><th>Metric</th><th>Value</th></tr>

<tr><td>Total Packets</td><td>{dashboard.total_packets}</td></tr>

<tr><td>TCP</td><td>{dashboard.protocol_counter["TCP"]}</td></tr>

<tr><td>UDP</td><td>{dashboard.protocol_counter["UDP"]}</td></tr>

<tr><td>ICMP</td><td>{dashboard.protocol_counter["ICMP"]}</td></tr>

<tr><td>Total Alerts</td><td>{dashboard.total_alerts}</td></tr>

<tr><td>Latest Alert</td><td>{dashboard.latest_alert}</td></tr>

</table>

</body>
</html>
"""

        with open("reports/report.html", "w") as file:
            file.write(html)

        print("\nReport generated: reports/report.html")