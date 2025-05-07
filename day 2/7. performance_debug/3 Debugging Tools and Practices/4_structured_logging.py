# Structured Logging: Log function entry and exit using logger.debug(...)
import logging

# Set up logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"Entering process_data with data: {data}")
    result = data * 2
    logger.debug(f"Exiting process_data with result: {result}")
    return result

# Example usage
process_data(5)

# Expected Output:
# DEBUG:__main__:Entering process_data with data: 5
# DEBUG:__main__:Exiting process_data with result: 10
