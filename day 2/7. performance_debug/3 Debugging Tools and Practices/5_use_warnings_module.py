# Use warnings Module: Issue a non-fatal warning using warnings.warn(...)
import warnings

def check_age(age):
    if age < 18:
        warnings.warn("Age is under 18", UserWarning)

# Example usage
check_age(15)

# Expected Output:
# UserWarning: Age is under 18
