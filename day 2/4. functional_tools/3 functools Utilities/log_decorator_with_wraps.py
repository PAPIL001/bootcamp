# Log Decorator with wraps
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully")
        return result
    return wrapper

# Test the log decorator with wraps
@log_decorator
def test_function(x, y):
    return x + y

print(test_function(3, 4))  
# Expected output:
# Calling test_function
# test_function executed successfully
# 7
