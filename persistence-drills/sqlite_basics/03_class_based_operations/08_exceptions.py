import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print("Database connection error:", e)

    def add(self, name, price):
        try:
            self.cur.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
            self.conn.commit()
            print(f"Inserted product: {name}, ₹{price}")
        except sqlite3.Error as e:
            print("Insert failed:", e)

p = Product()
p.add("Grapes", 40.0)
