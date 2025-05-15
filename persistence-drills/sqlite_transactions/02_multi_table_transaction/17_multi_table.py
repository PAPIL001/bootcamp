import sqlite3

conn = sqlite3.connect("store.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customer_name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS order_details (id INTEGER PRIMARY KEY, order_id INTEGER, product TEXT, quantity INTEGER)")

try:
    with conn:
        cur.execute("INSERT INTO orders (id, customer_name) VALUES (?, ?)", (1, "Geetha"))
        cur.execute("INSERT INTO order_details (order_id, product, quantity) VALUES (?, ?, ?)", (1, "Apple", 3))
    print("Inserted order and order_details in a transaction.")
except Exception as e:
    print("Transaction failed:", e)
