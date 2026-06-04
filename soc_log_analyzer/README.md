# SOC Log Analyzer API

A FastAPI-powered security log analysis tool that automatically detects brute force attacks, failed login patterns, and after-hours access events from raw log data.

---

## Overview

This project simulates a real SOC (Security Operations Center) triage workflow — ingesting raw log files and surfacing actionable threat indicators through a REST API. It was built to demonstrate practical skills in log analysis, pattern detection, and security automation relevant to DFIR and SOC operations.

---

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| Pattern Detection | Python `re` (regex) |
| Data Validation | Pydantic |
| Runtime | Python 3.13 |

---

## Features

- Detects **brute force attacks** by identifying repeated failed login attempts from the same source within a time window
- Flags **failed login events** across multiple accounts and endpoints
- Identifies **after-hours access** based on configurable time thresholds
- Accepts raw log input via API endpoints for real-time or batch analysis
- Returns structured JSON output with detected events, severity indicators, and source details

---

## Detection Logic

| Threat Type | Detection Method |
|---|---|
| Brute Force | Regex pattern matching on failed auth events; threshold-based source IP counting |
| Failed Logins | Pattern matching on authentication failure signatures across log lines |
| After-Hours Access | Timestamp parsing and comparison against configurable business hour windows |

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/analyze` | Submit raw log data for analysis |
| `GET` | `/results` | Retrieve flagged events from the last analysis |
| `GET` | `/health` | Health check endpoint |

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/HeeHeeGG/My-Python-PRojects.git
cd My-Python-PRojects/soc_log_analyzer
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive Swagger UI to submit logs and view results.

---

## Example Use Case

Submit a block of raw authentication logs to `/analyze` and receive a structured response identifying:

- Which IPs triggered brute force thresholds
- Which accounts had repeated failed login attempts
- Which access events occurred outside normal business hours

---

## SOC Relevance

This tool mirrors the triage logic used in real SOC environments when parsing Windows Event Logs, Syslog, or SIEM exports. The detection patterns map directly to MITRE ATT&CK techniques:

- **T1110** — Brute Force
- **T1078** — Valid Accounts (after-hours misuse)

---

## What I Learned

- Building detection logic with regex pattern matching against realistic log formats
- Designing a FastAPI service for security tooling and automation
- Structuring JSON responses to surface actionable threat data
- Mapping log events to real-world attacker behavior frameworks (MITRE ATT&CK)

---

## Author

**Chueshi Vangkowski**
[github.com/HeeHeeGG](https://github.com/HeeHeeGG)
