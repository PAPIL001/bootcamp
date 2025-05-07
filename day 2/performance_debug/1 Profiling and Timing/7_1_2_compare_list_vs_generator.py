

import timeit

list_time = timeit.timeit('[x*x for x in range(1000000)]', number=100)
generator_time = timeit.timeit('(x*x for x in range(1000000))', number=100)

print(f"List comprehension time: {list_time:.6f} seconds")  # Expected Output: List comprehension time: <some_time> seconds
print(f"Generator expression time: {generator_time:.6f} seconds")  # Expected Output: Generator expression time: <some_time> seconds
