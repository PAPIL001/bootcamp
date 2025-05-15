import sqlite3

# Connect to store.db
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

print("Products table created successfully.")
conn.commit()
conn.close()
