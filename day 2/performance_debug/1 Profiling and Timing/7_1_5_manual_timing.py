

def expensive_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

start_time = time.time()
expensive_function()
end_time = time.time()

print(f"Execution time: {end_time - start_time:.6f} seconds")  # Expected Output: Execution time: <some_time> seconds
