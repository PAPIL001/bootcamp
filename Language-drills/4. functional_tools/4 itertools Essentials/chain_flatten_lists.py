# Use chain to Flatten
from itertools import chain

combined = list(chain([1, 2], [3, 4], [5]))
print(combined)  # Expected: [1, 2, 3, 4, 5]
