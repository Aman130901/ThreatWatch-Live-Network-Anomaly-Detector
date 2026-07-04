from core.sniffer import PacketSniffer
from core.analyzer import PacketAnalyzer

analyzer = PacketAnalyzer()


def callback(packet):

    result = analyzer.analyze(packet)

    if result:
        print(result)


sniffer = PacketSniffer(callback)
sniffer.start()