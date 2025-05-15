import sqlite3


def update_product_price(product_id, new_price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))

    print(f"Product ID {product_id} price updated to ₹{new_price}")
    conn.commit()
    conn.close()


update_product_price(1, 550)
