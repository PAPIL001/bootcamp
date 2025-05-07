# Verbose Exceptions: Print exception type and message with except Exception as e: print(type(e), e).
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print(f"Exception type: {type(e)}")
        print(f"Exception message: {e}")

# Example usage
divide(5, 0)

# Expected Output:
# Exception type: <class 'ZeroDivisionError'>
# Exception message: division by zero
