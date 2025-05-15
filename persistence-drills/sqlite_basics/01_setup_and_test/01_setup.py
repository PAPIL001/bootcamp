import sqlite3

def setup_database():
    conn = sqlite3.connect('store.db')
    print("Database created and connected.")
    conn.close()

if __name__ == "__main__":
    setup_database()
