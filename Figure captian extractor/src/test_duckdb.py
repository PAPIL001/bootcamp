import duckdb

try:
    conn = duckdb.connect('test.db')
    conn.execute("""
        CREATE SEQUENCE IF NOT EXISTS paper_id_seq;
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY,
            pmc_id VARCHAR UNIQUE
        )
    """)
    conn.execute("INSERT INTO papers (id, pmc_id) VALUES (NEXTVAL('paper_id_seq'), 'TEST123')")
    conn.commit()
    cursor = conn.execute("SELECT id FROM papers WHERE pmc_id = 'TEST123'")
    result = cursor.fetchone()
    if result:
        print(f"Inserted ID: {result[0]}")
    else:
        print("Could not retrieve ID after insertion.")
    conn.close()
except duckdb.Error as e:
    print(f"DuckDB Error: {e}")