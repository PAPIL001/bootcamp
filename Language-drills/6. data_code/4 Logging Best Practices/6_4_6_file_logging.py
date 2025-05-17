import logging

logging.basicConfig(filename='log_output.txt', level=logging.INFO)
logger = logging.getLogger("file_logger")

logger.info("This will go to a file")

# Output will be written in 'log_output.txt'
