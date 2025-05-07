# partial Function
from functools import partial

# Fix the base of int(x, base) to base 2
base_2 = partial(int, base=2)

# Test the partial function
print(base_2("1010"))  # Expected: 10
