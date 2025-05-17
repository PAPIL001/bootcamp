

def is_valid_email(email):
    return "@" in email

def has_permission(user_role):
    return user_role == "admin"

# Example usage
email = "example@mail.com"
print(is_valid_email(email))  # Expected Output: True

user_role = "admin"
print(has_permission(user_role))  # Expected Output: True
