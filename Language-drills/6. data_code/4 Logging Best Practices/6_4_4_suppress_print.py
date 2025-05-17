import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("suppress_print")

logger.info("Replace print with logger.info")

# Output: Replace print with logger.info
