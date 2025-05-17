user = {"name": "Alice"}
print(user.get("name"))
print(user.get("age"))
user.setdefault("age", 25)
print(user)
