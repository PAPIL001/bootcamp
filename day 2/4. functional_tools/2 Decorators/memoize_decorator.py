# Memoization Decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# Test the decorator
@memoize
def slow_function(x):
    print(f"Calculating {x}...")
    time.sleep(1)
    return x * 2

print(slow_function(4))  # Expected: Calculating 4... 8
print(slow_function(4))  # Expected: 8 (from cache)
