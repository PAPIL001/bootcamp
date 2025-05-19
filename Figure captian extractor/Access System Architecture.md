# Figure Caption Extraction and Access System

## Overview

This document details the proposed architecture for the Figure Caption Extraction and Access System. The system is designed to extract metadata (title, abstract, figure captions, figure URLs, and entities from captions) from scientific publications, store this data efficiently, and provide a secure and user-friendly API for accessing it. The initial focus is on PubMed Central (PMC), with a design that allows for future expansion to other data sources.

---

## Architectural Diagram

```
+---------------------+       +---------------------+       +---------------------+
| Ingestion Service   |------>| Data Storage        |<------| API Service         |
|                     |       | (DuckDB initially)  |       |                     |
| - Fetches Data      |       |                     |       | - Handles Requests  |
| - Extracts Metadata |       |                     |       | - Authenticates     |
| - Stores Data       |       |                     |       | - Formats Response  |
| - CLI for Batch     |       +---------------------+       |                     |
+---------------------+                                     +---------------------+
          ^
          |
+---------------------+
| Configuration       |
| Management          |
| - Data Sources      |
| - API Keys          |
| - Logging Level     |
+---------------------+
          ^
          |
+---------------------+       +---------------------+
| Operational Tools   |------>| Logging Service     |
| - Docker            |       | - Centralized Logs  |
| - Batch Scripts     |       | - Configurable Level|
| - Monitoring        |       +---------------------+
+---------------------+
```

---

## Component Details

### 1. Ingestion Service (`src/ingestion/`)

**Responsibilities**:

* Fetch raw publication data
* Extract metadata
* Store data in storage backend

**Key Modules**:

* **Fetchers** (`src/ingestion/fetchers/`)

  * `pubmed_central.py`: Fetches from PMC (via E-utilities or BioC-PMC API)
  * Future support: `pubmed.py`, others

* **Extractors** (`src/ingestion/extractors/`)

  * `article_extractor.py`: Parses XML/BioC, extracts title, abstract, figures
  * `entity_extractor.py`: Uses PubTator 3 API for entity recognition

* **CLI** (`src/cli/ingestion_cli.py`)

  * Trigger batch ingestion
  * Supports file input and retry logic

**Tech Stack**: Python, `requests`, `lxml`, `bioc`

---

### 2. API Service (`src/api/`)

**Responsibilities**:

* Expose REST API for metadata queries

**Key Modules**:

* `app.py`: API entry point (Flask or FastAPI)
* `endpoints/`:

  * `/papers`: GET, query metadata
  * `/papers/upload`: POST, upload IDs for ingestion
* `models/`: Pydantic models for validation
* Supports API key authentication, JSON and CSV responses

**Tech Stack**: Python, Flask or FastAPI, Pydantic

---

### 3. Data Storage (`src/storage/`)

**Responsibilities**:

* Persist extracted metadata

**Key Modules**:

* `interfaces.py`: Abstract storage interface
* `duckdb_handler.py`: DuckDB-based implementation
* Future: `postgres_handler.py`

**Tech Stack**: Python, DuckDB

---

### 4. Configuration Management (`src/config.py`, `config/config.yaml`)

**Responsibilities**:

* Load system-wide settings

**Key Modules**:

* `config.py`: Loads YAML and env vars
* `config.yaml`: Stores API keys, data source settings, logging, etc.

**Tech Stack**: Python, PyYAML

---

### 5. Logging Service (`src/logger.py`)

**Responsibilities**:

* Centralize logging

**Key Modules**:

* `logger.py`: Sets up logging level, format, output (console/file)

**Tech Stack**: Python's logging module

---

### 6. Operational Tools (`operationalization/`)

**Responsibilities**:

* Facilitate deployment and monitoring

**Key Files**:

* `Dockerfile`, `docker-compose.yml`: Container setup
* `Makefile`: Commands for build/test/run
* `runbook.md` or `README.md`: Deployment instructions

---

## Data Flow

1. CLI or scheduler initiates an ingestion job with PMC IDs.
2. Ingestion Service fetches and extracts metadata (title, abstract, captions, URLs).
3. Entity Extractor processes figure captions for entity recognition.
4. Metadata is saved to DuckDB.
5. User sends API request with key.
6. API Service fetches data and returns JSON/CSV.
7. All components log activity.
8. Configuration settings are propagated system-wide.

---

## Future Considerations

* **Scalability**: Move to PostgreSQL, scale API horizontally
* **Error Handling**: Improve retry logic, resilience
* **Security**: Enhance input validation, add rate limiting
* **Caching**: Speed up frequent API responses
* **Async Processing**: Use Celery for background ingestion

---

## Summary

This modular, extensible architecture supports efficient ingestion and retrieval of figure captions and metadata from PMC. It includes robust logging, configuration, and API components to ensure usability and future scalability.
