from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")

data = {"user_id": 123}
user = User(**data)
print(user)
# Output: id=123
