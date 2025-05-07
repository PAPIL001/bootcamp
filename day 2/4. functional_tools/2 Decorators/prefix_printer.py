# Decorator with Arguments
def prefix_printer(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix}: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Test the decorator
@prefix_printer("Calling")
def test_function():
    print("Function executed")

test_function()  
# Expected output:
# Calling: test_function
# Function executed
