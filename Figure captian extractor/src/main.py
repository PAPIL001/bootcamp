import argparse
import logging
import os
from src.data_storage import DataStorage
from src.pubmed_parser import PubMedParser
from src.entity_extractor import logger as entity_logger

root = logging.getLogger()
root.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
root.addHandler(ch)

logger = logging.getLogger(__name__)
entity_logger.setLevel(logging.DEBUG)

def main():
    # ... rest of your main.py code ...
    parser = argparse.ArgumentParser(description="Extract figure captions and entities from PubMed articles.")
    parser.add_argument('pmc_ids', nargs='+', help='List of PMC IDs to process.')
    parser.add_argument('--output_db', default='paper_data.sqlite', help='Path to the output SQLite database.')
    args = parser.parse_args()

    # Explicitly delete the database file before each run
    try:
        os.remove(args.output_db)
        logger.info(f"Existing database file '{args.output_db}' deleted.")
    except FileNotFoundError:
        logger.info(f"No existing database file '{args.output_db}' found.")
    except Exception as e:
        logger.error(f"Error deleting database file '{args.output_db}': {e}")
        return

    with DataStorage(db_path=args.output_db) as storage:
        for pmc_id in args.pmc_ids:
            logger.info(f"Processing PMC ID: {pmc_id}")
            parser = PubMedParser(pmc_id)
            article_data = parser.parse()

            if article_data:
                paper_id = storage.insert_paper_data(
                    pmc_id=article_data.get('pmc'),
                    pmid=article_data.get('pmid'),
                    title=article_data.get('title'),
                    abstract=article_data.get('abstract'),
                )
                if paper_id:
                    for caption_data in article_data.get('figure_captions', []):
                        caption_id = storage.insert_figure_caption(
                            paper_id=paper_id,
                            caption_text=caption_data.get('caption'),
                            figure_url=caption_data.get('url'),
                        )
                        if caption_id:
                            for entity in caption_data.get('entities', []):
                                storage.insert_entity(
                                    caption_id=caption_id,
                                    entity_text=entity.get('text'),
                                    entity_type=entity.get('type'),
                                )
            else:
                logger.warning(f"Could not parse data for PMC ID: {pmc_id}")

    logger.info("Processing complete.")

if __name__ == "__main__":
    main()