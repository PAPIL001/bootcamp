# Use permutations and combinations
from itertools import permutations, combinations

nums = [1, 2, 3]

print("Permutations of 2:")
print(list(permutations(nums, 2)))
# Expected: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

print("Combinations of 2:")
print(list(combinations(nums, 2)))
# Expected: [(1, 2), (1, 3), (2, 3)]

print("Combinations of 3:")
print(list(combinations(nums, 3)))
# Expected: [(1, 2, 3)]
