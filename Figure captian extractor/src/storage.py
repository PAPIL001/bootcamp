import duckdb
import logging

logger = logging.getLogger(__name__)

DATABASE_FILE = "extracted_data.db"

def connect_db():
    """Connects to the DuckDB database."""
    try:
        conn = duckdb.connect(DATABASE_FILE)
        logger.info(f"Successfully connected to database: {DATABASE_FILE}")
        return conn
    except duckdb.Error as e:
        logger.error(f"Error connecting to database: {e}")
        return None
    
def create_tables(conn: duckdb.DuckDBPyConnection | None):
    """Creates the 'papers' and 'figure_captions' tables if they don't exist."""
    if conn:
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS papers (
                    paper_id TEXT PRIMARY KEY,
                    title TEXT,
                    abstract TEXT
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS figure_captions (
                    paper_id TEXT,
                    caption_index INTEGER,
                    caption_text TEXT,
                    FOREIGN KEY (paper_id) REFERENCES papers (paper_id)
                );
            """)
            logger.info("Tables 'papers' and 'figure_captions' created or already exist.")
        except duckdb.Error as e:
            logger.error(f"Error creating tables: {e}")

def store_paper_data(conn: duckdb.DuckDBPyConnection | None, paper_id: str, data: dict):
    """Stores the extracted paper data into the database."""
    if conn and paper_id and data:
        try:
            conn.execute("""
                INSERT INTO papers (paper_id, title, abstract)
                VALUES (?, ?, ?)
                ON CONFLICT (paper_id) DO UPDATE SET
                    title = EXCLUDED.title,
                    abstract = EXCLUDED.abstract;
            """, (paper_id, data.get('title'), data.get('abstract')))

            for index, caption in enumerate(data.get('figure_captions', [])):
                conn.execute("""
                    INSERT INTO figure_captions (paper_id, caption_index, caption_text)
                    VALUES (?, ?, ?);
                """, (paper_id, index, caption))

            logger.info(f"Successfully stored data for PMC ID: {paper_id}")
            conn.commit()  # Important to commit the changes
        except duckdb.Error as e:
            logger.error(f"Error storing data for PMC ID {paper_id}: {e}")
            conn.rollback() # Rollback in case of error

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    conn = connect_db()
    if conn:
        create_tables(conn)
        conn.close()