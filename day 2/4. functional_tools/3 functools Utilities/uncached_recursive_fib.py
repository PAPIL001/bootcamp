# Uncached Recursive Function
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Test the uncached recursive Fibonacci
print(fib(10))  # Expected: 55
