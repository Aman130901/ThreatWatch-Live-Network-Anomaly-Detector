from core.sniffer import PacketSniffer

def callback(packet):
    print(packet.summary())

sniffer = PacketSniffer(callback)
sniffer.start()