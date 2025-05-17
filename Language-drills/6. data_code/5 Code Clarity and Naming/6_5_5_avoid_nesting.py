

def is_valid_age(age):
    return age >= 18

def process_user_data(age, name):
    if is_valid_age(age):
        print(f"Welcome, {name}")
    else:
        print("Invalid age")

# Example usage
process_user_data(20, "John")  # Expected Output: Welcome, John
process_user_data(16, "Jane")  # Expected Output: Invalid age
