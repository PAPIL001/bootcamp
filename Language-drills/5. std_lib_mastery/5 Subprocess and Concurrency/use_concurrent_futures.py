from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    results = executor.map(square, [1, 2, 3])
    print(list(results))
# Output:
# [1, 4, 9]
