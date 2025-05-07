# Add Error IDs: Include error codes in log messages for easier tracing.
import logging

# Set up logger
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def process_data(data):
    try:
        if data == 0:
            raise ValueError("Data cannot be zero")
    except ValueError as e:
        logger.error(f"Error ID: 1001 - {e}")

# Example usage
process_data(0)

# Expected Output:
# ERROR:__main__:Error ID: 1001 - Data cannot be zero
