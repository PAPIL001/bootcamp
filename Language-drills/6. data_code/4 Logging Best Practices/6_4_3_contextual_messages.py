import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("contextual")

user = {"name": "Alice"}
logger.debug(f"User: {user['name']}")

# Output: User: Alice
