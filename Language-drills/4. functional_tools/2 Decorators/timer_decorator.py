# Timing Decorator
def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Test the decorator
@timer_decorator
def slow_function():
    time.sleep(2)

slow_function()  
# Expected output: (time will vary)
# Function executed in 2.000X seconds
