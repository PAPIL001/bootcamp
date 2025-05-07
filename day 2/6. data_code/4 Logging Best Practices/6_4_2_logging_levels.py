import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("my_logger")

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")

# Output:
# Debug message
# Info message
# Warning message
# Error message
