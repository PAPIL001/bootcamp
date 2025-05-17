import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger("formatted")

logger.info("Formatted log message")

# Output: <timestamp> - INFO - Formatted log message
