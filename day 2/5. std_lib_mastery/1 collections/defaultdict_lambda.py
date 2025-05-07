from collections import defaultdict

d = defaultdict(lambda: "N/A")
d["name"] = "Alice"
print(d["name"])    # Alice
print(d["age"])     # N/A
