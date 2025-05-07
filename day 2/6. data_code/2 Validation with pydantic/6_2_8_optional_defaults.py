from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    nickname: Optional[str] = None

user = User(name="Emily")
print(user)
# Output: name='Emily' nickname=None