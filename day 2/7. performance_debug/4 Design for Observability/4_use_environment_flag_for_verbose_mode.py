# Use Environment Flag for Verbose Mode: Enable debug logs only when DEBUG=True.
import logging
import os

# Set up logger
logging.basicConfig(level=logging.DEBUG if os.getenv("DEBUG") == "True" else logging.INFO)
logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"Processing data: {data}")
    return data * 2

# Set environment variable for debugging
os.environ["DEBUG"] = "True"

# Example usage
process_data(5)

# Expected Output (if DEBUG=True):
# DEBUG:__main__:Processing data: 5

# Set environment variable for no debugging
os.environ["DEBUG"] = "False"

# Example usage (when DEBUG=False)
process_data(5)

# Expected Output (if DEBUG=False):
# No debug output, only info level or higher
