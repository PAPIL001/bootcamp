# reduce with Lambda
from functools import reduce

# Compute factorial of n using range(1, n+1)
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n+1))

# Test the reduce function
print(factorial)  # Expected: 120
