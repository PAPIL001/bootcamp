import sqlite3


def delete_product(product_id):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM products WHERE id = ?
    ''', (product_id,))

    print(f"Product ID {product_id} deleted.")
    conn.commit()
    conn.close()


delete_product(2)
