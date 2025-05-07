# Use count to Generate IDs
from itertools import count

id_gen = count(1)
print(next(id_gen))  # Expected: 1
print(next(id_gen))  # Expected: 2
print(next(id_gen))  # Expected: 3
