# src/data_storage.py
import sqlite3
import logging
import os
from typing import List, Optional, Dict

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DataStorage:
    """
    Handles data storage using SQLite.
    """

    def __init__(self, db_path: str = 'paper_data.sqlite'):
        """
        Initializes the DataStorage object.
        """
        self.db_path = db_path
        self.conn = None
        self.create_tables()

    def connect(self):
        """
        Establishes a connection to the SQLite database.
        """
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            logger.error(f"Error connecting to SQLite database: {e}")
            raise

    def __enter__(self):
        self.conn = self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_tables(self):
        """
        Creates the tables in the SQLite database if they don't exist, using AUTOINCREMENT for primary keys.
        """
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS papers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        pmc_id TEXT UNIQUE,
                        pmid TEXT UNIQUE,
                        title TEXT,
                        abstract TEXT
                    )
                    """
                )
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS figure_captions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        paper_id INTEGER,
                        caption_text TEXT,
                        figure_url TEXT,
                        FOREIGN KEY (paper_id) REFERENCES papers(id)
                    )
                    """
                )
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS entities (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        caption_id INTEGER,
                        entity_text TEXT,
                        entity_type TEXT,
                        FOREIGN KEY (caption_id) REFERENCES figure_captions(id)
                    )
                    """
                )
                conn.commit()
                logger.info("Tables 'papers', 'figure_captions', and 'entities' created (if they didn't exist).")
        except sqlite3.Error as e:
            logger.error(f"Error creating tables: {e}")
            raise

    def insert_paper_data(self, pmc_id: str, pmid: Optional[str], title: str, abstract: str) -> Optional[int]:
        """
        Inserts paper metadata into the 'papers' table.
        """
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT OR REPLACE INTO papers (pmc_id, pmid, title, abstract)
                    VALUES (?, ?, ?, ?)
                    """,
                    (pmc_id, pmid, title, abstract),
                )
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error inserting paper data: {e}")
            return None

    def insert_figure_caption(self, paper_id: int, caption_text: str, figure_url: Optional[str] = None) -> Optional[int]:
        """
        Inserts a figure caption.
        """
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO figure_captions (paper_id, caption_text, figure_url)
                    VALUES (?, ?, ?)
                    """,
                    (paper_id, caption_text, figure_url),
                )
                conn.commit()
                caption_id = cursor.lastrowid
                logger.info(f"Figure caption inserted for Paper ID: {paper_id}, Caption ID: {caption_id}")
                return caption_id
        except sqlite3.Error as e:
            logger.error(f"Error inserting figure caption: {e}")
            return None

    def insert_entity(self, caption_id: int, entity_text: str, entity_type: str):
        """
        Inserts an entity.
        """
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO entities (caption_id, entity_text, entity_type)
                    VALUES (?, ?, ?)
                    """,
                    (caption_id, entity_text, entity_type),
                )
                conn.commit()
                logger.info(f"Entity inserted for Caption ID: {caption_id}, Entity: {entity_text} ({entity_type})")
        except sqlite3.Error as e:
            logger.error(f"Error inserting entity: {e}")
            raise

    def get_paper_data(self, pmc_id: str) -> Optional[Dict]:
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT pmc_id, pmid, title, abstract
                    FROM papers
                    WHERE pmc_id = ?
                    """,
                    (pmc_id,),
                )
                row = cursor.fetchone()
                if row:
                    return {
                        'pmc_id': row[0],
                        'pmid': row[1],
                        'title': row[2],
                        'abstract': row[3],
                    }
                else:
                    return None
        except sqlite3.Error as e:
            logger.error(f"Error retrieving paper data: {e}")
            raise

    def get_figure_captions(self, pmc_id: str) -> List[Dict]:
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT id, caption_text, figure_url
                    FROM figure_captions
                    WHERE paper_id = (SELECT id FROM papers WHERE pmc_id = ?)
                    """,
                    (pmc_id,),
                )
                rows = cursor.fetchall()
                return [
                    {'id': row[0], 'caption_text': row[1], 'figure_url': row[2]}
                    for row in rows
                ]
        except sqlite3.Error as e:
            logger.error(f"Error retrieving figure captions: {e}")
            raise

    def get_entities_by_caption_id(self, caption_id: int) -> List[Dict]:
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT entity_text, entity_type
                    FROM entities
                    WHERE caption_id = ?
                    """,
                    (caption_id,),
                )
                rows = cursor.fetchall()
                return [
                    {'entity_text': row[0], 'entity_type': row[1]}
                    for row in rows
                ]
        except sqlite3.Error as e:
            logger.error(f"Error retrieving entities: {e}")
            raise

    def get_all_papers(self) -> List[Dict]:
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT pmc_id, pmid, title, abstract
                    FROM papers
                    """,
                )
                rows = cursor.fetchall()
                return [
                    {'pmc_id': row[0], 'pmid': row[1], 'title': row[2], 'abstract': row[3]}
                    for row in rows
                ]
        except sqlite3.Error as e:
            logger.error(f"Error retrieving all paper data: {e}")
            raise

    def get_all_figure_captions(self) -> List[Dict]:
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT id, paper_id, caption_text, figure_url
                    FROM figure_captions
                    """,
                )
                rows = cursor.fetchall()
                return [
                    {'id': row[0], 'paper_id': row[1], 'caption_text': row[2], 'figure_url': row[3]}
                    for row in rows
                ]
        except sqlite3.Error as e:
            logger.error(f"Error retrieving all figure captions: {e}")
            raise

    def get_all_entities(self) -> List[Dict]:
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    SELECT id, caption_id, entity_text, entity_type
                    FROM entities
                    """,
                )
                rows = cursor.fetchall()
                return [
                    {'id': row[0], 'caption_id': row[1], 'entity_text': row[2], 'entity_type': row[3]}
                    for row in rows
                ]
        except sqlite3.Error as e:
            logger.error(f"Error retrieving all entities: {e}")
            raise

if __name__ == "__main__":
    # Example usage (you might need to adapt this based on your main script's logic)
    storage = DataStorage(db_path='paper_data.sqlite')
    paper_id = storage.insert_paper_data(
        pmc_id='PMC778899', pmid='123456', title='A Sample Paper', abstract='This is a sample abstract.'
    )
    if paper_id:
        caption_id = storage.insert_figure_caption(
            paper_id=paper_id, caption_text='A sample figure caption.', figure_url='http://example.com/figure.png'
        )
        if caption_id:
            storage.insert_entity(caption_id=caption_id, entity_text='Sample Entity', entity_type='GENE')

    papers = storage.get_all_papers()
    print("All Papers:", papers)
    captions = storage.get_all_figure_captions()
    print("All Captions:", captions)
    entities = storage.get_all_entities()
    print("All Entities:", entities)