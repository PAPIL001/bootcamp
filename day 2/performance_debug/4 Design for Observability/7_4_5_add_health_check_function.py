# Add Health Check Function: Write a simple function that returns system status for debugging.
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def health_check():
    # Simulate checking system health
    system_status = "System is healthy"
    logger.info(f"Health Check Status: {system_status}")
    return system_status

# Example usage
health_check()

# Expected Output:
# INFO:__main__:Health Check Status: System is healthy
