import sqlite3


def insert_product(name, price):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO products (name, price)
    VALUES (?, ?)
    ''', (name, price))

    print(f"Inserted product: {name}, ₹{price}")
    conn.commit()
    conn.close()


# Insert some products
insert_product('Apple', 30.5)
insert_product('Orange', 25.0)
