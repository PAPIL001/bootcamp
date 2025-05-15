import sqlite3
import csv

class Product:
    def __init__(self):
        self.conn = sqlite3.connect("store.db")
        self.cur = self.conn.cursor()

    def export_to_csv(self, filename="products.csv"):
        self.cur.execute("SELECT id, name, price FROM products")
        rows = self.cur.fetchall()
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "price"])
            writer.writerows(rows)
        print(f"Exported {len(rows)} products to {filename}")

if __name__ == "__main__":
    p = Product()
    p.export_to_csv()
