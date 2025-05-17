from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    user = User(name="Bob", age="not a number")
except ValidationError as e:
    print(e)
# Output: 1 validation error for User
# age
#   value is not a valid integer (type=type_error.integer)