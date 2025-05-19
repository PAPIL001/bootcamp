# Key Components

A modular Python-based system for ingesting and querying biomedical research papers using PMC/PMID identifiers. This system fetches paper metadata, figures, and annotated entities via the BioC-PMC and PubTator3 APIs. It also offers a RESTful API and a CLI tool for convenient access and management.

---

## 🚀 Key Components and Interactions

### 1. Ingestion Service

* Accepts a list of paper IDs (PMC or PMID) as input.
* Fetches paper content in XML format using the BioC-PMC API.
* Parses XML to extract:

  * Title
  * Abstract
  * Figure captions
  * Figure URLs
* Uses the PubTator3 API to extract entities from figure captions.
* Sends extracted data to the **Data Storage** component.
* Supports batch processing, modular design, and new data sources.
* Includes retry logic and robust error handling.

### 2. Data Storage

* Stores structured extracted data using **SQLite** (default).
* Easily switchable to other DB systems (e.g., PostgreSQL).
* Defines a schema for papers, figures, and entities.
* Optimized for efficient queries.

### 3. API Service

* RESTful API for external access to data.
* Supports queries by paper IDs (PMC or PMID).
* Supports responses in JSON and CSV formats.
* Implements API key/password authentication.
* Provides standardized error handling and HTTP status codes.

### 4. CLI Tool

* Command-line interface for:

  * Submitting paper ID lists for ingestion
  * Querying the API
  * Administrative tasks (e.g., config management)
* Interfaces with the API service.

### 5. Configuration Management

* Uses YAML or INI files to manage settings:

  * Storage backend (default: SQLite)
  * API credentials
  * Data sources (default: PMC)
  * Logging levels (INFO, DEBUG, etc.)
* Loads and applies configuration system-wide.

### 6. Logging

* Comprehensive logging using Python's `logging` module.
* Logs ingestion, API requests/responses, errors, and DB operations.
* Configurable log levels: DEBUG, INFO, WARNING, ERROR.
* Logs to file and/or console.

---

## 🛠️ Technologies Used

* Python 3.x
* BioC-PMC API
* PubTator3 API
* SQLite (default DB)
* Flask or FastAPI (for API service)
* Click or argparse (for CLI tool)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/research-paper-system.git
cd research-paper-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Usage

### Ingest Papers

```bash
python cli.py ingest --ids PMC1234567 PMC7654321
```

### Query API

```bash
python cli.py query --id PMC1234567
```

### Configuration

Update `config.yaml`:

```yaml
database: sqlite:///data.db
api_key: yourapikey
source: PMC
log_level: INFO
```

---

## 🔐 Authentication

* API endpoints require API key (configurable in `config.yaml`).
* Pass via header: `Authorization: Bearer <API_KEY>`

---
