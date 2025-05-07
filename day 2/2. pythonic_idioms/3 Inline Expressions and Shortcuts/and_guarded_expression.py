is_admin = True
def delete_user(user_id):
    print(f"Deleted user {user_id}")
is_admin and delete_user(42)  # Output: Deleted user 42
