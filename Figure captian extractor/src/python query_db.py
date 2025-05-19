import sqlite3

db_path = 'paper_data.sqlite'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("--- Papers Table ---")
    cursor.execute("SELECT * FROM papers")
    papers = cursor.fetchall()
    for row in papers:
        print(row)

    print("\n--- Figure Captions Table ---")
    cursor.execute("SELECT * FROM figure_captions")
    captions = cursor.fetchall()
    for row in captions:
        print(row)

    print("\n--- Entities Table ---")
    cursor.execute("SELECT * FROM entities")
    entities = cursor.fetchall()
    for row in entities:
        print(row)

    conn.close()

except sqlite3.Error as e:
    print(f"SQLite Error: {e}")