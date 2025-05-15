import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def add(self, name, price):
        if not isinstance(name, str):
            print("Invalid name type")
            return
        if not isinstance(price, (int, float)) or price <= 0:
            print("Invalid price")
            return

        self.cur.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()
        print(f"Inserted product: {name}, ₹{price}")

p = Product()
p.add("Pineapple", 60.0)
p.add("BadProduct", -5)
