from pydantic import BaseModel, conint, constr

class User(BaseModel):
    username: constr(min_length=3)
    age: conint(gt=0)

user = User(username="john_doe", age=30)
print(user)
# Output: username='john_doe' age=30