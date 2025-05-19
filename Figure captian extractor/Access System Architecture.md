# Figure Caption Extraction and Access System Architecture

## 1. Overview

This document details the proposed architecture for the Figure Caption Extraction and Access System. The system is designed to extract metadata (title, abstract, figure captions, figure URLs, and entities from captions) from scientific publications, store this data efficiently, and provide a secure and user-friendly API for accessing it. The initial focus is on PubMed Central (PMC), with a design that allows for future expansion to other data sources.

## 2. Architectural Diagram (Conceptual)

+---------------------+       +---------------------+       +---------------------+| Ingestion Service   |------>| Data Storage        |<------| API Service         ||                     |       | (DuckDB initially)  |       |                     || - Fetches Data      |       |                     |       | - Handles Requests  || - Extracts Metadata |       |                     |       | - Authenticates     || - Stores Data       |       |                     |       | - Formats Response  || - CLI for Batch     |       +---------------------+       |                     |+---------------------+                                     +---------------------+^|+---------------------+| Configuration       || Management          || - Data Sources      || - API Keys          || - Logging Level     |+---------------------+^|+---------------------+       +---------------------+| Operational Tools   |------>| Logging Service     || - Docker            |       | - Centralized Logs  || - Batch Scripts     |       | - Configurable Level|| - Monitoring        |       +---------------------++---------------------+
## 3. Component Details

### 3.1. Ingestion Service (`src/ingestion/`)

* **Responsibility:** Fetches raw publication data, extracts relevant metadata, and stores it in the Data Storage.
* **Key Components:**
    * **Fetcher Modules (`src/ingestion/fetchers/`):**
        * `pubmed_central.py`: Handles fetching data from PMC using E-utilities and potentially BioC-PMC API.
        * `(Future: pubmed.py, etc.)`: Modules for other data sources.
    * **Extractor Modules (`src/ingestion/extractors/`):**
        * `article_extractor.py`: Contains logic to parse fetched data (XML, BioC) and extract title, abstract, captions, and figure URLs.
        * `entity_extractor.py`: Responsible for calling entity recognition services (initially PubTator 3 API) to extract entities from captions.
    * **Ingestion CLI (`src/cli/ingestion_cli.py`):** Provides command-line interface for triggering batch ingestion jobs with options for:
        * Providing a file of paper IDs.
        * Specifying data source.
    * **Batch Processing Logic:** Manages the processing of lists of paper IDs, handling potential errors and retries.
* **Technology:** Python, `requests`, `lxml`, potentially `bioc` library.

### 3.2. API Service (`src/api/`)

* **Responsibility:** Provides a RESTful API for users to query and retrieve the extracted metadata.
* **Key Components:**
    * **API Application (`src/api/app.py`):** Main application entry point (using Flask or FastAPI).
    * **Endpoints (`src/api/endpoints/`):** Defines API routes and request handlers:
        * `/papers`: Endpoint for querying papers based on IDs or other criteria. Supports `GET`.
        * `/papers/upload`: Endpoint for uploading lists of paper IDs for processing. Supports `POST`.
    * **Data Models (`src/api/models/`):** Defines the structure of the data returned by the API (using Pydantic for validation and serialization).
    * **Authentication:** Implements API key-based authentication.
    * **Response Formatting:** Handles outputting data in JSON and CSV formats based on user request.
* **Technology:** Python, Flask or FastAPI, Pydantic.

### 3.3. Data Storage (`src/storage/`)

* **Responsibility:** Persists the extracted metadata.
* **Key Components:**
    * **Storage Interface (`src/storage/interfaces.py`):** Defines an abstract interface for data storage operations, allowing for different implementations.
    * **DuckDB Handler (`src/storage/duckdb_handler.py`):** Implementation of the storage interface using DuckDB as the initial database.
    * **(Future: `postgres_handler.py`, etc.)**: Potential implementations for other database systems.
* **Technology:** Python, DuckDB.

### 3.4. Configuration Management (`src/config.py`, `config/config.yaml`)

* **Responsibility:** Manages system-wide configurations.
* **Key Components:**
    * **Configuration Loading (`src/config.py`):** Reads configuration from files (e.g., YAML) and environment variables.
    * **Configuration Files (`config/config.yaml`):** Stores settings for:
        * Data storage location.
        * API keys.
        * Default data source.
        * Logging level.
        * Batch processing parameters.
* **Technology:** Python, PyYAML.

### 3.5. Logging Service (`src/logger.py`)

* **Responsibility:** Provides centralized logging for all system components.
* **Key Components:**
    * **Logging Setup (`src/logger.py`):** Configures the logging system with options for:
        * Logging level (INFO, DEBUG, WARNING, ERROR).
        * Log format.
        * Log output (console, file).
* **Technology:** Python's built-in `logging` module.

### 3.6. Operational Tools (`operationalization/`)

* **Responsibility:** Provides tools for deploying, running, and monitoring the system.
* **Key Components:**
    * **Dockerfile:** Defines the Docker image for containerizing the application.
    * **docker-compose.yml:** Defines services for multi-container Docker setup (if needed).
    * **Makefile:** Provides convenient commands for building, running, and testing the application within Docker.
    * **Runbook (`operationalization/runbook.md` or `README.md`):** Contains instructions for deployment, usage, and basic troubleshooting.

## 4. Data Flow

1.  An ingestion job is initiated (via CLI or a scheduled process) with a list of paper IDs and a specified data source.
2.  The Ingestion Service uses the appropriate Fetcher module to retrieve the raw data for each paper.
3.  The Extractor modules parse the raw data to extract title, abstract, figure captions, and figure URLs.
4.  The Entity Extractor module is called for each figure caption to identify key entities.
5.  The extracted metadata is then passed to the Data Storage layer for persistence.
6.  A user sends a query to the API Service, providing an API key.
7.  The API Service retrieves the requested data from the Data Storage.
8.  The API Service formats the data into JSON or CSV and returns it to the user.
9.  All components log relevant information to the Logging Service.
10. The Configuration Management component provides settings to all other components as needed.

## 5. Future Considerations

* **Scalability:** For handling a large volume of data and API requests, consider using a more scalable database (e.g., PostgreSQL) and deploying the API service across multiple instances.
* **Error Handling and Resilience:** Implement robust error handling, retries, and monitoring to ensure system stability.
* **Security:** Implement proper input validation and consider rate limiting for the API.
* **Caching:** Implement caching mechanisms at the API level to improve response times for frequently accessed data.
* **Asynchronous Tasks:** For long-running ingestion jobs, consider using task queues (e.g., Celery) to avoid blocking.

This architecture provides a modular and extensible foundation for the Figure Caption Extraction and Access System, addressing the core requirements outlined in the developer hand-off brief.
