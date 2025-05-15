import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def add(self, name, price):
        try:
            with self.conn:
                self.cur.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
                print(f"Inserted product: {name}, ₹{price}")
        except sqlite3.Error as e:
            print("Transaction failed:", e)

p = Product()
p.add("Watermelon", 35.0)
