Figure Caption Extraction and Access SystemOverviewThis system extracts figure captions and associated metadata from scientific publications, specifically PubMed Central (PMC), and provides an API and CLI for accessing this data.Table of ContentsInstallationConfigurationData IngestionAPI UsageCLI UsageDeploymentLoggingDependenciesFuture ConsiderationsInstallationClone the repository:git clone <repository_url>
cd figure_caption_extractor
Create a virtual environment (recommended):python -m venv venv
source venv/bin/activate  # On Linux/macOS
.\venv\Scripts\activate # On Windows
Install the dependencies:pip install -r requirements.txt
ConfigurationCreate a configuration file:Copy the config/config.yaml.example to config/config.yaml.Edit config/config.yaml to set your desired configuration options:data_storage:
  type: "sqlite"  # or "postgresql" (future)
  path: "paper_data.duckdb" # Path to the SQLite database

api:
  key: "your_api_key" #  Replace with a strong, secure API key
  host: "0.0.0.0"
  port: 8000

pubmed_central:
  email: "your_email@example.com" # Required by NCBI

logging:
  level: "INFO" #  "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
  handler: "file" # "console" or "file"
  log_file_path: "logs/system.log"
Important: Replace "your_api_key" with a strong, unique API key.  This is essential for securing your API.The pubmed_central.email is required by the NCBI E-utilities API.  Please provide a valid email address.Data IngestionUsing the CLI ToolTo ingest data, use the ingest command of the CLI tool.You need to provide a list of paper IDs (PMCID) and the data source.Example usage:python src/cli/cli.py ingest --pmc_ids PMC1234567,PMC2345678 --source pubmed_central
--pmc_ids:  Comma-separated list of PMC IDs.--source:  Currently, only pubmed_central is supported.Batch IngestionFor batch ingestion, you can provide a file containing a list of paper IDs:python src/cli/cli.py ingest --pmc_id_file paper_ids.txt --source pubmed_central
--pmc_id_file: Path to a text file where each line contains one PMC ID.API UsageBase URLThe API base URL is: http://<host>:<port>, where:<host> is the hostname or IP address of the server running the API (default: 0.0.0.0).<port> is the port number the API is listening on (default: 8000).AuthenticationThe API uses API key authentication.You must include the api_key parameter in the query string of every request.Example: http://0.0.0.0:8000/papers?pmc_id=PMC1234567&api_key=your_api_keyEndpoints/papers:Method: GETDescription: Retrieves paper data based on PMC ID.Parameters:pmc_id (required): The PMC ID of the paper.api_key (required): Your API key.Example:http://0.0.0.0:8000/papers?pmc_id=PMC1234567&api_key=your_api_keyResponse:{
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
/papers/uploadMethod: POSTDescription: Uploads a list of PMC IDs for ingestion.Parameters:api_key (required): Your API keyRequest Body:A JSON object with a single key pmc_ids and value as a list of strings{
    "pmc_ids": ["PMC1234567", "PMC2345678", "PMC9876543"]
}
Examplecurl -X POST -H "Content-Type: application/json" \
  -d '{"pmc_ids": ["PMC1234567", "PMC2345678"]}' \
  "http://0.0.0.0:8000/papers/upload?api_key=your_api_key"
Response:{
    "message": "Ingestion process started for the provided PMC IDs."
}
Response FormatThe API returns data in JSON format by default.The system may support CSV format in the future.CLI UsageThe CLI tool provides commands for interacting with the system.Available Commandsingest: Ingests paper data from a specified source.query:  Queries the API for paper data.config:  Displays the current system configuration.Command: ingestDescription: Ingests data from a specified source.Options:--pmc_ids (str, required): Comma-separated list of PMC IDs.--pmc_id_file (str): Path to a file containing PMC IDs (one per line).--source (str, required): Data source (pubmed_central).Example:python src/cli/cli.py ingest --pmc_ids PMC1234567,PMC2345678 --source pubmed_central
Command: queryDescription: Queries the API for paper data.Options:--pmc_id (str, required): PMC ID of the paper to query.Example:python src/cli/cli.py query --pmc_id PMC1234567
Command: configDescription: Displays the current system configuration.Example:python src/cli/cli.py config
DeploymentThe system can be deployed using Docker for easy setup and management.Build the Docker image:docker build -t figure_caption_extractor .
Run the Docker container:docker run -p 8000:8000 figure_caption_extractor
This will start the API service in a container, accessible at http://localhost:8000.You can also use docker-composeLoggingThe system uses Python's logging module.Logs are written to the console or a file, depending on the configuration.The logging level can be configured in the config/config.yaml file.Log files are located in the logs directory (if file logging is enabled).DependenciesPython 3.8+DuckDBFlask or FastAPIRequestslxmlClickPyYAMLDockerFuture ConsiderationsScalability: For handling a large volume of data and API requests, consider using a more scalable database (e.g., PostgreSQL) and deploying the API service across multiple instances.Error Handling and Resilience: Implement robust error handling, retries, and monitoring to ensure system stability.Security: Implement proper input validation and consider rate limiting for the API.Caching: Implement caching mechanisms at the API level to improve response times for frequently accessed data.Asynchronous Tasks: For long-running ingestion jobs, consider using task queues (e.g., Celery) to avoid blocking.