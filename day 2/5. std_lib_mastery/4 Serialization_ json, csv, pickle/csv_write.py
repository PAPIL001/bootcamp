import csv

data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)

# Output file out.csv will contain:
# name,age
# Alice,25
# Bob,30
