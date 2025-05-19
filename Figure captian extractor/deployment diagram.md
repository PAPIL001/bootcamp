# Figure Caption Extraction and Access System

## Overview

This document details the proposed architecture for the Figure Caption Extraction and Access System. The system is designed to extract metadata (title, abstract, figure captions, figure URLs, and entities from captions) from scientific publications, store this data efficiently, and provide a secure and user-friendly API for accessing it. The initial focus is on PubMed Central (PMC), with a design that allows for future expansion to other data sources.

---

## Deployment Diagram

```
+---------------------+      +---------------------+      +-----------------------+
|       User          |----->|      CLI Tool       |----->|      API Service      |
+---------------------+      +---------------------+      +-----------------------+
                                        ^                    ^       |
                                        |                    |       |
                                        |                    |       v
+-----------------------+      +---------------------+      +-----------------------+
|    Ingestion Jobs     |----->|   Ingestion Service   |----->|     Data Storage      |
+-----------------------+      +---------------------+      +-----------------------+
                                        |                    |  (SQLite/PostgreSQL)
                                        |
                                +---------------------+
                                | Configuration       |
                                +---------------------+
```

### Explanation

* Users interact with the system through the CLI Tool or API Service.
* CLI Tool uses the API Service to retrieve data.
* Ingestion Jobs run the Ingestion Service to fetch data from NCBI APIs.
* The Ingestion Service stores the data in Data Storage.
* API Service queries the Data Storage in response to requests.
* Configuration settings are shared across all components.

---

## Docker Deployment

This system can be deployed using Docker, which simplifies the setup and management of the application and its dependencies.

### Prerequisites

* Docker installed on your system:

  * [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
  * [Docker Desktop for macOS](https://docs.docker.com/desktop/install/mac-install/)
  * [Docker Engine for Linux](https://docs.docker.com/engine/install/)
* Basic understanding of Docker (images, containers, etc.)

### Steps

1. **Clone the repository**:

```bash
git clone <[repository_url](https://github.com/PAPIL001/bootcamp/tree/main/Figure%20captian%20extractor)>
cd figure_caption_extractor
```

2. **Build the Docker image**:

```bash
docker build -t figure_caption_extractor .
```

* `-t figure_caption_extractor`: Tags the image.
* `.`: Current directory contains the Dockerfile.

3. **Run the Docker container**:

```bash
docker run -p 8000:8000 figure_caption_extractor
```

* `-p 8000:8000`: Maps port 8000 of container to host.
* `figure_caption_extractor`: Name of the Docker image.

> The API will now be available at `http://localhost:8000`.

### Docker Compose (Optional)

If a `docker-compose.yaml` is present, run:

```bash
docker-compose up -d
```

* `-d`: Detached mode (runs in background).

Ensure `config/config.yaml` aligns with `docker-compose.yaml`, especially database settings.

### Configuration

Use environment variables to configure the container:

```bash
docker run -p 8000:8000 -e API_KEY=your_secure_api_key figure_caption_extractor
```

In `config.yaml`, refer to the variable:

```yaml
api:
  key: ${API_KEY}
```

> Avoid hardcoding secrets in the Dockerfile.

### Persistent Data

To retain data (e.g., SQLite DB):

```bash
docker run -p 8000:8000 -v figure_caption_data:/app/paper_data figure_caption_extractor
```

* `-v figure_caption_data:/app/paper_data`: Mounts a volume.
* Update your config path accordingly:

```yaml
path: "/app/paper_data/paper_data.db"
```

With Docker Compose:

```yaml
volumes:
  figure_caption_data:
```

### Accessing the API

* Local: `http://localhost:8000`
* Remote: `http://<server_ip>:8000`

Refer to the API Usage section in the main README for endpoints.

---

## Summary

This system architecture and deployment plan enable scalable, secure, and efficient extraction and access of scientific metadata, especially focused on figures and their captions. It leverages Docker for ease of setup and supports both CLI-based and API-based interactions.
