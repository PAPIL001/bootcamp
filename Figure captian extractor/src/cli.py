import click
import logging
from . import extraction
from . import storage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@click.group()
def cli():
    """A CLI tool to extract and store figure captions."""
    pass

@cli.command("ingest-single")
@click.argument("pmc_id")
def ingest_single(pmc_id: str):
    """Ingests data for a single PMC ID."""
    logger.info(f"Starting ingestion for PMC ID: {pmc_id}")
    xml_content = extraction.fetch_bioc_xml(pmc_id)
    if xml_content:
        extracted_data = extraction.extract_paper_data(xml_content)
        conn = storage.connect_db()
        if conn:
            storage.create_tables(conn)
            storage.store_paper_data(conn, pmc_id, extracted_data)
            conn.close()
            logger.info(f"Ingestion complete for PMC ID: {pmc_id}")
        else:
            logger.error(f"Failed to connect to the database for PMC ID: {pmc_id}")
    else:
        logger.error(f"Failed to fetch XML for PMC ID: {pmc_id}")

if __name__ == "__main__":
    cli()