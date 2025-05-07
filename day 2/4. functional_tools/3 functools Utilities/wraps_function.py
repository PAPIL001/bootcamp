# Function Metadata with wraps
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def sample_function(x, y):
    """This function adds two numbers."""
    return x + y

# Test the decorator with wraps
print(sample_function(3, 4))  # Expected: 7
print(sample_function.__name__)  # Expected: sample_function
print(sample_function.__doc__)  # Expected: This function adds two numbers.
