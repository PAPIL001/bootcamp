# Use groupby: Group list of dicts by a shared key
from itertools import groupby
from operator import itemgetter

data = [
    {"dept": "CS", "name": "Alice"},
    {"dept": "CS", "name": "Bob"},
    {"dept": "Math", "name": "Charlie"},
    {"dept": "Math", "name": "David"},
]

# Group by 'dept' (requires sorting first)
data.sort(key=itemgetter("dept"))
for key, group in groupby(data, key=itemgetter("dept")):
    print(key, list(group))

# Expected:
# CS [{'dept': 'CS', 'name': 'Alice'}, {'dept': 'CS', 'name': 'Bob'}]
# Math [{'dept': 'Math', 'name': 'Charlie'}, {'dept': 'Math', 'name': 'David'}]
