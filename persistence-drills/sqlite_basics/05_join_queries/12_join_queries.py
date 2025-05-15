import sqlite3

class Product:
    def __init__(self, db_name="store.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

        self.cur.execute("PRAGMA table_info(products)")
        columns = [row[1] for row in self.cur.fetchall()]
        if "category_id" not in columns:
            self.cur.execute("ALTER TABLE products ADD COLUMN category_id INTEGER")

        self.conn.commit()

    def seed(self):
        self.cur.execute("INSERT INTO categories (name) VALUES ('Fruits')")
        self.cur.execute("INSERT INTO categories (name) VALUES ('Vegetables')")
        self.conn.commit()

        self.cur.execute("UPDATE products SET category_id = 1 WHERE name = 'Apple'")
        self.cur.execute("UPDATE products SET category_id = 2 WHERE name = 'Carrot'")
        self.conn.commit()

    def fetch_products_with_categories(self):
        self.cur.execute('''
            SELECT p.id, p.name, p.price, c.name 
            FROM products p 
            JOIN categories c ON p.category_id = c.id
        ''')
        rows = self.cur.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Price: ₹{row[2]}, Category: {row[3]}")

p = Product()
p.seed()
p.fetch_products_with_categories()
