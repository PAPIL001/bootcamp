# Trace Function Calls: Wrap functions with decorators to log their name, args, and return value.
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def trace_function_calls(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@trace_function_calls
def add(a, b):
    return a + b

# Example usage
add(3, 4)

# Expected Output:
# INFO:__main__:Calling function add with args: (3, 4) and kwargs: {}
# INFO:__main__:add returned: 7
