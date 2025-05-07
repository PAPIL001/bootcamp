
import timeit

execution_time = timeit.timeit('sum(range(10000))', number=1000)
print(f"Execution time: {execution_time:.6f} seconds")  # Expected Output: Execution time: <some_time> seconds
