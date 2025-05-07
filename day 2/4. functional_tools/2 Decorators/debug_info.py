# Debug Information Decorator
def debug_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

# Test the decorator
@debug_info
def add(a, b):
    return a + b

add(2, 3)
# Expected output:
# Function add called with arguments (2, 3) and {}
# Function add returned 5
