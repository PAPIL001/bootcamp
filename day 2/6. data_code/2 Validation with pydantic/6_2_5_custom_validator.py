from pydantic import BaseModel, validator

class User(BaseModel):
    name: str

    @validator("name")
    def name_must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError("Name must start with a capital letter")
        return v

try:
    user = User(name="alice")
except Exception as e:
    print(e)
# Output: 1 validation error for User
# name
#   Name must start with a capital letter (type=value_error)