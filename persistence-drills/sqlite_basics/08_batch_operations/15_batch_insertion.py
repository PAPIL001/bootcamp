import sqlite3

class Product:
    def __init__(self):
        self.conn = sqlite3.connect("store.db")
        self.cur = self.conn.cursor()

    def batch_insert(self, products):
        try:
            with self.conn:
                self.cur.executemany("INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)", products)
            print(f"Inserted {len(products)} products in batch.")
        except Exception as e:
            print("Batch insert failed:", e)

if __name__ == "__main__":
    p = Product()
    batch = [
        ("Banana", 10.0, 2),
        ("Mango", 50.0, 2),
        ("Grapes", 40.0, 2)
    ]
    p.batch_insert(batch)
