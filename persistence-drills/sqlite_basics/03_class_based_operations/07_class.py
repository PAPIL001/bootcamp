import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add(self, name, price):
        self.cur.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()
        print(f"Inserted product: {name}, ₹{price}")

    def update(self, product_id, new_price):
        self.cur.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
        self.conn.commit()
        print(f"Product ID {product_id} price updated to ₹{new_price}")

    def delete(self, product_id):
        self.cur.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()
        print(f"Deleted product with ID {product_id}")

    def list(self):
        self.cur.execute("SELECT * FROM products")
        for row in self.cur.fetchall():
            print(f"ID: {row[0]}, Name: {row[1]}, Price: ₹{row[2]}")

p = Product()
p.add("Banana", 15.0)
p.list()
