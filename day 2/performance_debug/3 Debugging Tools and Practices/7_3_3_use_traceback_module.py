# Use traceback Module: Print detailed error trace using traceback.format_exc().
import traceback

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print("An error occurred:", traceback.format_exc())

# Example usage
divide(5, 0)

# Expected Output:
# An error occurred: Traceback (most recent call last):
#   File "<stdin>", line 7, in divide
# ZeroDivisionError: division by zero
