import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def search(self, name_fragment):
        self.cur.execute("SELECT * FROM products WHERE name LIKE ?", (f"%{name_fragment}%",))
        for row in self.cur.fetchall():
            print(f"ID: {row[0]}, Name: {row[1]}, Price: ₹{row[2]}")

p = Product()
p.search("apple")
