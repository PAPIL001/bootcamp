# Avoid Temporary Lists: Use sum(x for x in range(1000000)) instead of sum([...]).
result = sum(x for x in range(1000000))
print(f"Sum: {result}")  # Expected Output: Sum: <sum_value>
