
class DB:
    def __enter__(self):
        print("DB opened")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("DB closed")
with DB():
    print("Query running")
# Output:
# DB opened
# Query running
# DB closed
