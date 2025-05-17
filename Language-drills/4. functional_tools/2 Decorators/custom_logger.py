# Logging Decorator with Parameters
def custom_logger(log_message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{log_message} - Before execution")
            result = func(*args, **kwargs)
            print(f"{log_message} - After execution")
            return result
        return wrapper
    return decorator

# Test the decorator
@custom_logger("LOG")
def test_function():
    print("Executing function")

test_function()
# Expected output:
# LOG - Before execution
# Executing function
# LOG - After execution
