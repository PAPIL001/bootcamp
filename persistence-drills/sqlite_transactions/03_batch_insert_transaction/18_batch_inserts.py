import sqlite3

conn = sqlite3.connect("store.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)")

records = [
    ("System started",),
    ("User logged in",),
    ("Error occurred",)
]

try:
    with conn:
        cur.executemany("INSERT INTO logs (message) VALUES (?)", records)
    print(f"Inserted {len(records)} log records in a transaction.")
except Exception as e:
    print("Transaction failed:", e)
