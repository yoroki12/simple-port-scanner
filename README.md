# Simple Port Scanner

A lightweight TCP port scanner built with Python, developed as a learning project to understand networking fundamentals (TCP handshake, socket programming) and concurrent programming.

## Features

- **TCP Connect Scanning** — uses raw sockets (`connect_ex()`) to detect open ports via full TCP handshake
- **Multithreading** — scans multiple ports concurrently using `ThreadPoolExecutor` for faster results
- **Service Detection** — identifies common services running on open ports (HTTP, SSH, etc.)
- **Filtered Port Detection** — distinguishes between closed ports (active refusal) and filtered ports (no response / firewall-blocked), including edge cases like `EAGAIN` errno
- **Report Generation** — saves scan results to a text file with timestamps and duration

## What I Learned

Building this project helped me understand:
- The TCP three-way handshake and how `connect_ex()` interacts with it
- The difference between open, closed, and filtered ports at the network level
- Why multithreading matters for I/O-bound tasks like network scanning
- Real-world edge cases (e.g. debugging why SMTP port 25 showed different results between this scanner and `nmap`, tracing it to an `EAGAIN` errno likely caused by ISP-level filtering)

## Installation

```bash
git clone https://github.com/yoroki12/simple-port-scanner.git
cd simple-port-scanner
python3 SimplePortScanner.py
```

No external dependencies — uses only Python's standard library (`socket`, `concurrent.futures`, `datetime`).

## Usage

Run the script and follow the prompts:

```bash
python3 SimplePortScanner.py
```

You'll be asked to enter:
- Target IP or domain
- Port range to scan

## Example Output
Port Scan Report
Target: boardleaders.rf.gd
Start time: 2026-08-14 23:06:09.064521
End time: 2026-08-14 23:07:34.686004
Duration: 0:01:25.621483

Open ports:
  Port 80: http
  Port 443: https
  Port 2049: nfs

Total open ports: 3
IP Address: 185.27.134.149


## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Only scan systems you own or have explicit permission to test (e.g. `scanme.nmap.org`, which is provided by the Nmap project specifically for testing purposes). Unauthorized port scanning may be illegal in your jurisdiction.

## Roadmap

- [ ] Command-line arguments via `argparse`
- [ ] Input validation for IP/domain
- [ ] Progress indicator for large scans
- [ ] Export results to JSON/CSV
- [ ] Banner grabbing for deeper service identification

## License

MIT
