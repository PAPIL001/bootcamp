import csv

# Assume data.csv content:
# name,age
# Alice,25
# Bob,30

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        # {'name': 'Alice', 'age': '25'}
        # {'name': 'Bob', 'age': '30'}
