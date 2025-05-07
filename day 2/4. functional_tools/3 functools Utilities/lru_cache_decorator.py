# lru_cache Memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Test the lru_cache decorator
print(fib(10))  # Expected: 55
print(fib(10))  # Expected: 55 (cached result)
