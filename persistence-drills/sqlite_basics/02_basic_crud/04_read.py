import sqlite3


def fetch_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: ₹{product[2]}")

    conn.close()


fetch_products()
