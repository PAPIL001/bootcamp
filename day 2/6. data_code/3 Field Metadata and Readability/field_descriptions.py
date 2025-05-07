from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(..., description="User's email address")

print(User.schema())
# Output: Schema includes description for the 'email' field
