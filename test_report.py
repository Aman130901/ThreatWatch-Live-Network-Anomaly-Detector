from core.dashboard import Dashboard
from core.reporter import ReportGenerator

dashboard = Dashboard()

dashboard.total_packets = 123
dashboard.total_alerts = 2
dashboard.latest_alert = "Possible Port Scan"

dashboard.protocol_counter["TCP"] = 70
dashboard.protocol_counter["UDP"] = 30
dashboard.protocol_counter["ICMP"] = 23

reporter = ReportGenerator()
reporter.generate(dashboard)

print("Done!")