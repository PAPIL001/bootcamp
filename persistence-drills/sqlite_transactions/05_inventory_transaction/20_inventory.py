import sqlite3
from datetime import datetime

conn = sqlite3.connect("store.db")
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE products ADD COLUMN inventory INTEGER DEFAULT 0")
    print("Inventory column added successfully.")
except sqlite3.OperationalError as e:
    print(f"Error adding column: {e}")

conn.commit()

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    inventory INTEGER DEFAULT 0
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS inventory_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    change INTEGER,
    timestamp TEXT
)
""")

cur.execute("INSERT OR IGNORE INTO products (id, name, price, inventory) VALUES (10, 'Monitor', 15000, 5)")
conn.commit()

def update_inventory(product_id, change):
    try:
        with conn:
            # Update inventory count
            cur.execute("UPDATE products SET inventory = inventory + ? WHERE id = ?", (change, product_id))
            # Log the change
            cur.execute("INSERT INTO inventory_log (product_id, change, timestamp) VALUES (?, ?, ?)",
                        (product_id, change, datetime.now().isoformat()))
        print(f"Inventory updated for Product ID {product_id}, Change: {change}")
    except Exception as e:
        print("Inventory transaction failed:", e)

update_inventory(10, -2)
