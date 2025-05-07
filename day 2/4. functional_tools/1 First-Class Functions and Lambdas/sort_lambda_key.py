# Sort with Lambda Key
pairs = [(1, "b"), (2, "a")]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Expected: [(2, 'a'), (1, 'b')]
