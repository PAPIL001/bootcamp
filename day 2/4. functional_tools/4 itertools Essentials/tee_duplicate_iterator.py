# Use tee: Duplicate an iterator and iterate independently
from itertools import tee

iterator = iter([1, 2, 3])
a, b = tee(iterator)

print(list(a))  # Expected: [1, 2, 3]
print(list(b))  # Expected: [1, 2, 3]
