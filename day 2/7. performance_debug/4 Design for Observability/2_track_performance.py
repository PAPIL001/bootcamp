# Track Performance: Add timing to log output to trace slow functions.
import logging
import time

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def slow_function():
    start_time = time.time()
    time.sleep(2)  # Simulating a slow function
    end_time = time.time()
    logger.info(f"slow_function executed in {end_time - start_time:.4f} seconds")

# Example usage
slow_function()

# Expected Output:
# INFO:__main__:slow_function executed in 2.0001 seconds
