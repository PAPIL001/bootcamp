import sqlite3

conn = sqlite3.connect("store.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    holder TEXT,
    balance REAL
)
""")

cur.execute("INSERT OR IGNORE INTO accounts (account_id, holder, balance) VALUES (1, 'Alice', 1000)")
cur.execute("INSERT OR IGNORE INTO accounts (account_id, holder, balance) VALUES (2, 'Bob', 500)")
conn.commit()

def transfer(from_id, to_id, amount):
    try:
        with conn:
            cur.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_id,))
            from_balance = cur.fetchone()[0]
            if from_balance < amount:
                raise ValueError("Insufficient funds")
            cur.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_id))
            cur.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_id))
        print(f"Transferred ₹{amount} from Account {from_id} to Account {to_id}")
    except Exception as e:
        print("Transfer failed:", e)

transfer(1, 2, 200)
