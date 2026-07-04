# 🛡️ ThreatWatch — Live Network Anomaly Detector

Modern networks are constantly exposed to threats like port scans, SYN floods, and ICMP-based attacks  often invisible to the naked eye until real damage is done. ThreatWatch is a lightweight, Python-based Intrusion Detection System (IDS) that brings live network visibility directly to your terminal.

Built on top of Scapy for packet capture and Rich for an interactive, real-time dashboard, ThreatWatch continuously monitors traffic on a chosen network interface, analyzes each packet, and applies a set of configurable detection rules to flag suspicious behavior as it happens. Detected threats are logged in multiple formats (CSV, JSON, and plain text) and summarized in an automatically generated HTML report at the end of each session giving you both real-time awareness and a persistent cord for later analysis.

Designed with simplicity and extensibility in mind, ThreatWatch is well suited for students and security enthusiasts learning how intrusion detection works under the hood, as well as for anyone who wants a quick, no-frills way to keep an eye on their own network traffic. Its modular architecture separating packet capture, analysis, detection, logging, and reporting into distinct components makes it easy to extend with new detection rules, alerting integrations, or a richer UI in the future.

---

## ✨ Features

- **Live packet capture** on any network interface using Scapy
- **Real-time terminal dashboard** showing packet counts, protocol breakdown, and active alerts
- **Threat detection engine** for common attack patterns:
  - Possible SYN flood attacks
  - Possible ICMP flood attacks
  - Possible port scans
  - Abnormally large packets
- **Multi-format logging** — every alert is written to CSV, JSON, and a plain-text log file
- **Automatic HTML report generation** on exit, summarizing the session
- **Configurable thresholds** for tuning detection sensitivity to your environment

---

## 📸 Screenshots

Screenshots of the live dashboard and generated reports are available in the [`screenshots/`](./screenshots) folder.

---

## 🏗️ Architecture

ThreatWatch follows a simple, modular pipeline:

```
 Network Interface
        │
        ▼
 ┌───────────────┐
 │ PacketSniffer │  (core/sniffer.py)   – captures raw packets via Scapy
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ PacketAnalyzer│  (core/analyzer.py)  – extracts IP/TCP/UDP/ICMP metadata
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ ThreatDetector│  (core/detector.py)  – applies detection rules & thresholds
 └───────┬───────┘
         ▼
 ┌────────────────────────────┐
 │ Dashboard  │  ThreatLogger │  (core/dashboard.py, core/logger.py)
 │ (live UI)  │ (CSV/JSON/log)│
 └────────────────────────────┘
         ▼
 ┌───────────────┐
 │ ReportGenerator│ (core/reporter.py) – writes reports/report.html on exit
 └───────────────┘
```

Each stage is decoupled, so individual components (e.g. the detection engine) can be modified or extended without touching the rest of the pipeline.

---

## 📁 Project Structure

```
ThreatWatch-Live-Network-Anomaly-Detector/
├── main.py                  # Entry point — wires up the full pipeline
├── requirements.txt         # Python dependencies
├── config/
│   └── settings.py          # Thresholds, log paths, app-wide settings
├── core/
│   ├── sniffer.py            # Live packet capture (Scapy)
│   ├── analyzer.py           # Packet parsing & feature extraction
│   ├── detector.py           # Threat detection rules
│   ├── logger.py             # CSV / JSON / log-file logging
│   ├── dashboard.py          # Live Rich-based terminal dashboard
│   └── reporter.py           # HTML report generation
├── docs/
│   └── architecture.md       # Extended architecture notes
├── screenshots/              # Dashboard & report screenshots
├── logs/                     # Generated at runtime (alerts.csv, alerts.json, threatwatch.log)
├── reports/                  # Generated at runtime (report.html)
└── tests/                    # Manual test/demo scripts
```

---

## ⚙️ Requirements

- Python 3.9+
- Root/administrator privileges (required for live packet capture)
- A supported network interface

Key dependencies (see `requirements.txt` for the full pinned list):

- [`scapy`](https://pypi.org/project/scapy/) — packet sniffing and parsing
- [`rich`](https://pypi.org/project/rich/) — live terminal dashboard
- `pandas`, `numpy`, `matplotlib` — data handling and reporting support
- `psutil` — system/network utilities

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/ThreatWatch-Live-Network-Anomaly-Detector.git
cd ThreatWatch-Live-Network-Anomaly-Detector

# (Recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

> **Linux users:** Scapy requires elevated privileges to sniff packets. Run the application with `sudo` or grant the appropriate capabilities to your Python interpreter.

---

## ▶️ Usage

Run ThreatWatch on the default network interface:

```bash
sudo python3 main.py
```

Specify a network interface explicitly:

```bash
sudo python3 main.py -i eth0
```

While running, ThreatWatch displays a live dashboard with:

| Metric | Description |
|---|---|
| Packets Captured | Total packets analyzed in this session |
| TCP / UDP / ICMP | Per-protocol packet counts |
| Alerts | Total number of threats detected |
| Latest Alert | Most recently triggered alert type |
| Most Active IP | Source IP with the highest packet volume |

Press **`CTRL+C`** to stop monitoring. On exit, ThreatWatch automatically generates an HTML summary report at `reports/report.html`.

---

## 🔍 Detection Rules

Detection logic lives in `core/detector.py` and is driven by configurable thresholds in `config/settings.py`:

| Threat | Trigger Condition | Default Threshold | Severity |
|---|---|---|---|
| Large Packet | Packet size exceeds `MAX_PACKET_SIZE` | 1500 bytes | LOW |
| Possible SYN Flood | SYN packets from one source within a 10s window | 50 | HIGH |
| Possible ICMP Flood | ICMP packets from one source within a 10s window | 50 | MEDIUM |
| Possible Port Scan | Distinct destination ports contacted by one source | 20 | HIGH |

These thresholds can be tuned in `config/settings.py` to match the traffic patterns of your network.

---

## 🗂️ Logging & Reports

Every detected alert is recorded in three places:

- **`logs/alerts.csv`** — structured, spreadsheet-friendly log
- **`logs/alerts.json`** — structured JSON log for programmatic use
- **`logs/threatwatch.log`** — plain-text application log

At the end of each session, a self-contained HTML report is written to **`reports/report.html`**, summarizing total packets, protocol distribution, and alert counts.

> Log and report files are excluded from version control via `.gitignore`.

---

## 🧪 Testing

The `tests/` directory (along with the top-level `test_*.py` scripts) contains standalone scripts for exercising individual components — the sniffer, analyzer, detector, logger, and reporter — independently of the full application. These are useful for manual verification during development:

```bash
sudo python3 test_sniffer.py     # Verify raw packet capture
sudo python3 test_analyzer.py    # Verify packet parsing
python3 test_detector.py         # Verify detection rules (with a live sniffer)
python3 test_logger.py           # Verify CSV/JSON/log writing
python3 test_report.py           # Verify HTML report generation
python3 test_config.py           # Verify configuration values
```

---

## 🛠️ Configuration

All runtime behavior is centralized in `config/settings.py`:

```python
INTERFACE = None              # Default network interface (None = auto)
PROMISCUOUS_MODE = True

SYN_FLOOD_THRESHOLD = 50
ICMP_FLOOD_THRESHOLD = 50
PORT_SCAN_THRESHOLD = 20
MAX_PACKET_SIZE = 1500

CSV_LOG = "logs/alerts.csv"
JSON_LOG = "logs/alerts.json"
HTML_REPORT = "reports/report.html"

REFRESH_RATE = 1
```

---

## 🗺️ Roadmap Ideas

- Persistent baseline/anomaly scoring instead of static thresholds
- Alerting integrations (email, Slack, webhook)
- Web-based dashboard alongside the terminal UI
- Rule-based allow-listing for trusted hosts/subnets

---

## ⚠️ Disclaimer

ThreatWatch is intended for educational use and monitoring networks you own or are authorized to test. Capturing traffic on networks without permission may be illegal in your jurisdiction. Use responsibly.

---

## 👤 Author

**Aman Sonkar**
