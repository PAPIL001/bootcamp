# Composition of Decorators
def simple_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@simple_logger
@timer_decorator
def test_function():
    time.sleep(2)

test_function()  
# Expected output: 
# Function started
# Function executed in 2.000X seconds
# Function ended
