from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="David", age=35)
print(user.dict())
# Output: {'name': 'David', 'age': 35}
print(user.json())
# Output: {"name": "David", "age": 35}