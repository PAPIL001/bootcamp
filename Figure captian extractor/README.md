# Figure Caption Extraction and Access System

## Overview

This system extracts figure captions and associated metadata from scientific publications, specifically from PubMed Central (PMC). It provides an API and CLI to access and manage the extracted data.

---

## Table of Contents

* [Installation](#installation)
* [Configuration](#configuration)
* [Data Ingestion](#data-ingestion)
* [API Usage](#api-usage)
* [CLI Usage](#cli-usage)
* [Deployment](#deployment)
* [Logging](#logging)
* [Dependencies](#dependencies)
* [Future Considerations](#future-considerations)

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone <[repository_url](https://github.com/PAPIL001/bootcamp/tree/main/Figure%20captian%20extractor)>
   cd figure_caption_extractor
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Create configuration file**:

   ```bash
   cp config/config.yaml.example config/config.yaml
   ```

2. **Edit `config/config.yaml` with your settings**:

   ```yaml
   data_storage:
     type: "sqlite"
     path: "paper_data.duckdb"

   api:
     key: "your_api_key"
     host: "0.0.0.0"
     port: 8000

   pubmed_central:
     email: "your_email@example.com"

   logging:
     level: "INFO"
     handler: "file"
     log_file_path: "logs/system.log"
   ```

> Replace `your_api_key` with a strong API key. The email is required for using the NCBI API.

---

## Data Ingestion

### Single Ingestion

```bash
python src/cli/cli.py ingest --pmc_ids PMC1234567,PMC2345678 --source pubmed_central
```

### Batch Ingestion

```bash
python src/cli/cli.py ingest --pmc_id_file paper_ids.txt --source pubmed_central
```

---

## API Usage

### Base URL

```
http://<host>:<port>
```

Default: `http://0.0.0.0:8000`

### Authentication

All endpoints require an `api_key` parameter.

### Endpoints

#### GET `/papers`

**Example**:

```
http://0.0.0.0:8000/papers?pmc_id=PMC1234567&api_key=your_api_key
```

**Response**:

```json
{
  "pmc_id": "PMC1234567",
  "pmid": "12345",
  "title": "Paper Title",
  "abstract": "Paper abstract...",
  "figure_captions": [
    {
      "id": 1,
      "caption_text": "Figure 1 caption",
      "figure_url": "http://example.com/fig1.jpg",
      "entities": [
        {"text": "Entity1", "type": "Gene"},
        {"text": "Entity2", "type": "Chemical"}
      ]
    },
    {
      "id": 2,
      "caption_text": "Figure 2 caption",
      "figure_url": null,
      "entities": []
    }
  ]
}
```

#### POST `/papers/upload`

**Request**:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"pmc_ids": ["PMC1234567", "PMC2345678"]}' \
  "http://0.0.0.0:8000/papers/upload?api_key=your_api_key"
```

**Response**:

```json
{
  "message": "Ingestion process started for the provided PMC IDs."
}
```

---

## CLI Usage

### Ingest Command

```bash
python src/cli/cli.py ingest --pmc_ids PMC1234567,PMC2345678 --source pubmed_central
```

### Query Command

```bash
python src/cli/cli.py query --pmc_id PMC1234567
```

### Config Command

```bash
python src/cli/cli.py config
```

---

## Deployment

### Using Docker

**Build Docker image**:

```bash
docker build -t figure_caption_extractor .
```

**Run Docker container**:

```bash
docker run -p 8000:8000 figure_caption_extractor
```

> API will be available at `http://localhost:8000`

---

## Logging

* Logging is configured in `config.yaml`
* Supports console or file output
* Logs are saved in the `logs/` directory when file logging is enabled

---

## Dependencies

* Python 3.8+
* DuckDB
* Flask or FastAPI
* requests
* lxml
* Click
* PyYAML
* Docker

---

## Future Considerations

* **Scalability**: Use PostgreSQL, multi-instance deployment
* **Resilience**: Add retries, monitoring, error handling
* **Security**: Input validation, rate limiting
* **Performance**: Add caching at API level
* **Async Processing**: Use Celery for background ingestion tasks

---

