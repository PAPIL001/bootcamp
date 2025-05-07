from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Alice", age=25)
print(user)
# Output: name='Alice' age=25
