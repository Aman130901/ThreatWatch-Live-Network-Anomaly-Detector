"""
ThreatWatch v2.0
Main Application
Author: Aman Sonkar
"""

import argparse

from rich.console import Console
from rich.live import Live

from core.sniffer import PacketSniffer
from core.analyzer import PacketAnalyzer
from core.detector import ThreatDetector
from core.logger import ThreatLogger
from core.dashboard import Dashboard
from core.reporter import ReportGenerator

console = Console()

# Initialize components
analyzer = PacketAnalyzer()
detector = ThreatDetector()
logger = ThreatLogger()
dashboard = Dashboard()
reporter = ReportGenerator()


def process_packet(packet):
    """
    Process every captured packet.
    """

    data = analyzer.analyze(packet)

    if data is None:
        return

    # Update Dashboard Statistics
    dashboard.update(data)

    # Detect Threats
    alerts = detector.detect(data)

    # Process Alerts
    for alert in alerts:

        dashboard.add_alert(alert)

        logger.log(data, alert)

        console.print(
            f"[bold red]🚨 [{alert['severity']}] {alert['type']}[/bold red]"
        )


def main():

    parser = argparse.ArgumentParser(
        description="ThreatWatch - Live Network Anomaly Detector"
    )

    parser.add_argument(
        "-i",
        "--interface",
        help="Network interface (eth0, wlan0, enp0s3...)",
        default=None,
    )

    args = parser.parse_args()

    console.print(
        "\n[bold cyan]🛡 ThreatWatch v2.0[/bold cyan]"
    )

    console.print(
        "[green]Starting Intrusion Detection System...[/green]\n"
    )

    try:

        with Live(
            dashboard.generate_table(),
            refresh_per_second=2,
            console=console,
        ) as live:

            def callback(packet):

                process_packet(packet)

                live.update(
                    dashboard.generate_table()
                )

            sniffer = PacketSniffer(
                callback=callback,
                interface=args.interface
            )

            sniffer.start()

    except KeyboardInterrupt:

        console.print(
            "\n[yellow]Stopping ThreatWatch...[/yellow]"
        )

    finally:

        reporter.generate(dashboard)

        console.print(
            "[bold green]✓ HTML Report Generated[/bold green]"
        )

        console.print(
            "[green]Saved to reports/report.html[/green]"
        )

        console.print(
            "[bold cyan]Thank you for using ThreatWatch![/bold cyan]"
        )


if __name__ == "__main__":
    main()