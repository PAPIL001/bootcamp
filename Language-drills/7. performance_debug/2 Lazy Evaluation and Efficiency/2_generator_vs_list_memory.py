
import sys

# List comprehension
my_list = [x*x for x in range(10000)]
print(f"List memory usage: {sys.getsizeof(my_list)} bytes")  # Expected Output: List memory usage: <size> bytes

# Generator expression
my_generator = (x*x for x in range(10000))
print(f"Generator memory usage: {sys.getsizeof(my_generator)} bytes")  # Expected Output: Generator memory usage: <size> bytes
