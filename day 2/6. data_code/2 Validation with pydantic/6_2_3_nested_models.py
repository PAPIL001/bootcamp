from pydantic import BaseModel

class Profile(BaseModel):
    bio: str

class User(BaseModel):
    name: str
    age: int
    profile: Profile

data = {"name": "Carol", "age": 28, "profile": {"bio": "Loves Python"}}
user = User(**data)
print(user)
# Output: name='Carol' age=28 profile=Profile(bio='Loves Python')