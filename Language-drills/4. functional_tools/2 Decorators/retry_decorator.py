# Retry Mechanism Decorator
def retry_decorator(retries):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retrying...")
            return None
        return wrapper
    return decorator

# Test the decorator
@retry_decorator(3)
def test_function():
    print("Trying to run...")
    raise ValueError("An error occurred")

test_function()
# Expected output:
# Trying to run...
# Error: An error occurred. Retrying...
# Trying to run...
# Error: An error occurred. Retrying...
# Trying to run...
# Error: An error occurred. Retrying...
