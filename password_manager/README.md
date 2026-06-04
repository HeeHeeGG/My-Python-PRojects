# Password Manager API

A secure, production-style REST API for managing credentials — built with FastAPI, SQLAlchemy, and Fernet encryption.

---

## Overview

This project implements a fully functional password manager backend with encrypted storage, a structured database layer, and clean REST endpoints. It was built to demonstrate applied knowledge of API design, encryption, and database modeling in a real-world security context.

---

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| Database ORM | SQLAlchemy |
| Database | SQLite |
| Encryption | Fernet (cryptography library) |
| Data Validation | Pydantic |
| Runtime | Python 3.13 |

---

## Features

- Store, retrieve, update, and delete credentials via REST endpoints
- All passwords encrypted at rest using Fernet symmetric encryption
- SQLite database with SQLAlchemy ORM for structured, typed data access
- Pydantic models for request/response validation and schema enforcement
- Environment variable support via `.env` for secure key management
- `.gitignore` configured to prevent accidental exposure of keys or database files

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/passwords` | Store a new encrypted credential |
| `GET` | `/passwords` | Retrieve all stored credentials |
| `GET` | `/passwords/{id}` | Retrieve a specific credential by ID |
| `PUT` | `/passwords/{id}` | Update an existing credential |
| `DELETE` | `/passwords/{id}` | Delete a credential |

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/HeeHeeGG/My-Python-PRojects.git
cd My-Python-PRojects/password_manager
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the project root:

```
FERNET_KEY=your_generated_fernet_key
```

To generate a key:

```python
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
```

### Run the API

```bash
uvicorn main:app --reload
```

Then open your browser to `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

---

## Security Notes

- Encryption keys are loaded from environment variables, never hardcoded
- `.env` and the SQLite database file are excluded from version control via `.gitignore`
- Fernet encryption ensures passwords cannot be read directly from the database

---

## What I Learned

- Designing and implementing a REST API from scratch using FastAPI
- Applying symmetric encryption to sensitive data at the application layer
- Structuring a database with SQLAlchemy models and relationships
- Using Pydantic for strict input validation and clean API contracts
- Secure secret management using environment variables

---

## Author

**Chueshi Vangkowski**
[github.com/HeeHeeGG](https://github.com/HeeHeeGG)
