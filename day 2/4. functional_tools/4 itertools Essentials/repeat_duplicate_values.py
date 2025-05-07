# Use repeat to Duplicate Values
from itertools import repeat

repeated = list(repeat(None, 10))
print(repeated)  
# Expected: [None, None, None, None, None, None, None, None, None, None]
