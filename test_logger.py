from core.logger import ThreatLogger

logger = ThreatLogger()

packet = {
    "src_ip": "192.168.1.10",
    "dst_ip": "8.8.8.8"
}

alert = {
    "type": "Possible Port Scan",
    "severity": "HIGH"
}

logger.log(packet, alert)

print("Threat Logged Successfully!")