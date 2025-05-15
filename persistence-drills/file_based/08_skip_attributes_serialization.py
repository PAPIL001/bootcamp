import json

class User:
    def __init__(self, username: str, email: str, password: str, phone_number: str):
        self.username = username
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def to_safe_dict(self):
        return {
            "username" : self.username,
            "email": self.email
        }

    def to_safe_json(self) -> str:
        return json.dumps(self.to_safe_dict(), indent=4)

    def __repr__(self):
        return f"User(username={self.username}, email={self.email}, password=***, phone_numer=***)"


user = User("Papil", "papil.verma.5@gmail.com", "password123","8299383649")

print("Full User Object")
print(user)

print("\nSerialized User (Sensitive data skipped):")
print(user.to_safe_json())