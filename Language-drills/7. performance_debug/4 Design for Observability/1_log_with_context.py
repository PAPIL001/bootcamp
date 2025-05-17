# Log with Context: Log user ID and function name in each message.
import logging

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def user_action(user_id, action):
    logger.info(f"User ID: {user_id} - Action: {action} - Function: {user_action.__name__}")

# Example usage
user_action(123, "login")

# Expected Output:
# INFO:__main__:User ID: 123 - Action: login - Function: user_action
