# Use islice: Skip first 3 and take next 4 elements
from itertools import islice

result = list(islice(range(10), 3, 7))
print(result)  # Expected: [3, 4, 5, 6]
