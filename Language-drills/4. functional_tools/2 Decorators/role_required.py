# Access Control Decorator
def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                print("Access Denied: Incorrect role")
                return
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

# Test the decorator
@role_required("admin")
def access_controlled_function(user_role):
    print(f"Function executed by {user_role}")

access_controlled_function("user")  # Expected: Access Denied: Incorrect role
access_controlled_function("admin")  # Expected: Function executed by admin
