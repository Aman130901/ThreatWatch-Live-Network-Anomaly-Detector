"""
Packet Sniffer Module
ThreatWatch v2.0
"""

from scapy.all import sniff
from rich.console import Console

console = Console()


class PacketSniffer:

    def __init__(self, callback, interface=None):

        self.callback = callback
        self.interface = interface

    def start(self):

        console.print("[bold green]ThreatWatch Started[/bold green]")

        if self.interface:
            console.print(f"[cyan]Listening on:[/cyan] {self.interface}")
        else:
            console.print("[cyan]Listening on default interface[/cyan]")

        console.print("[yellow]Press CTRL+C to stop[/yellow]\n")

        sniff(
            iface=self.interface,
            prn=self.callback,
            store=False
        )