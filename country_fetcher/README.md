# Country Info Fetcher

A Python command-line tool that queries the REST Countries API to retrieve and display detailed information about any country in the world.

---

## Overview

This project was built to practice real-world API consumption — handling HTTP requests, parsing JSON responses, and presenting structured data cleanly in the terminal. It uses the publicly available REST Countries API and requires no authentication or API key.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| HTTP Client | `requests` |
| API | [REST Countries](https://restcountries.com) |
| Output | Terminal / CLI |

---

## Features

- Look up any country by name
- Displays key information including:
  - Official and common name
  - Capital city
  - Region and subregion
  - Population
  - Currency name, symbol, and code
  - Languages spoken
  - Country flag (emoji)
- Handles invalid input and API errors gracefully with clear error messages

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/HeeHeeGG/My-Python-PRojects.git
cd My-Python-PRojects/country_fetcher
pip install requests
```

### Usage

```bash
python main.py
```

You will be prompted to enter a country name. Example output:

```
Country: Japan
Capital: Tokyo
Region: Asia
Population: 125,700,000
Currency: Japanese Yen (JPY) — ¥
Languages: Japanese
Flag: 🇯🇵
```

---

## API Reference

This project uses the [REST Countries API](https://restcountries.com) — a free, open API requiring no authentication.

Example request:
```
GET https://restcountries.com/v3.1/name/{country}
```

---

## Error Handling

- Invalid or misspelled country names return a clear "Country not found" message
- Network errors are caught and surfaced with a descriptive prompt
- Empty input is handled without crashing

---

## What I Learned

- Consuming a public REST API using Python `requests`
- Parsing and navigating nested JSON response structures
- Writing defensive code with proper error handling for network and input failures
- Presenting API data in a clean, readable CLI format

---

## Author

**Chueshi Vangkowski**
[github.com/HeeHeeGG](https://github.com/HeeHeeGG)
