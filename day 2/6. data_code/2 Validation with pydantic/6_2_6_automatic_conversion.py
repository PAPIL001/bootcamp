from pydantic import BaseModel

class User(BaseModel):
    age: int

user = User(age="42")
print(user)
# Output: age=42