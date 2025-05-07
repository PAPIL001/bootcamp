# Basic Function Decorator
import time
from functools import wraps

def simple_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

# Test the decorator
@simple_logger
def test_function():
    print("Executing test function")

test_function()  
# Expected output:
# Function started
# Executing test function
# Function ended
