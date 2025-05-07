import logging

debug = True
if debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("conditional")
logger.debug("This is a debug message")

# Output (if debug=True): This is a debug message
