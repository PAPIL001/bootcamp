# Default Dict Generator using functools.partial
from functools import partial
from collections import defaultdict

# Create a defaultdict of lists
default_dict = partial(defaultdict, list)

# Test the default dict generator
my_dict = default_dict()
my_dict["a"].append(1)
my_dict["b"].append(2)

print(my_dict)  # Expected: defaultdict(<class 'list'>, {'a': [1], 'b': [2]})
