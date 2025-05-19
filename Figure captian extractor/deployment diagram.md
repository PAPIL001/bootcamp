Deployment Diagram+---------------------+      +---------------------+      +-----------------------+
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
Explanation:Users interact with the system either through the CLI Tool or the API Service.The CLI Tool uses the API Service to retrieve data.Ingestion Jobs are scheduled or triggered to run the Ingestion Service.The Ingestion Service fetches data from NCBI APIs and stores it in the Data Storage.The API Service retrieves data from the Data Storage in response to user requests.The Configuration component provides settings to all other components.