# Fail Loud, Then Gracefully: Raise the actual error after logging it.
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        raise  # Re-raise the exception after logging

# Example usage
divide(5, 0)

# Expected Output:
# ERROR:__main__:Error occurred: division by zero
# Traceback (most recent call last):
#   File "<stdin>", line 10, in divide
# ZeroDivisionError: division by zero
