import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect("store.db")
        self.cur = self.conn.cursor()

    def total_value(self):
        self.cur.execute("SELECT SUM(price) FROM products")
        result = self.cur.fetchone()[0]
        return result or 0.0

if __name__ == "__main__":
    p = Product()
    total = p.total_value()
    print(f"Total value of all products: ₹{total}")
