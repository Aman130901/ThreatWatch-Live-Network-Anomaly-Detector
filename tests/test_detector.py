from rich.console import Console

from core.sniffer import PacketSniffer
from core.analyzer import PacketAnalyzer
from core.detector import ThreatDetector

console = Console()

analyzer = PacketAnalyzer()
detector = ThreatDetector()


def callback(packet):

    data = analyzer.analyze(packet)

    if data is None:
        return

    alerts = detector.detect(data)

    for alert in alerts:

        console.print(
            f"[bold red]🚨 {alert['severity']}[/bold red] - {alert['type']}"
        )


sniffer = PacketSniffer(callback)
sniffer.start()