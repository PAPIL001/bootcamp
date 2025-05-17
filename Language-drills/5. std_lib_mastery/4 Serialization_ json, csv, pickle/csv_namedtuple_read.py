import csv
from collections import namedtuple

# Assume data.csv content:
# name,age
# Alice,25
# Bob,30

Person = namedtuple("Person", ["name", "age"])

with open("data.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        p = Person(*row)
        print(p)
        # Person(name='Alice', age='25')
        # Person(name='Bob', age='30')
