from pydantic import BaseModel

class Config(BaseModel):
    """This model represents app configuration."""
    debug: bool

print(Config.__doc__)
# Output: This model represents app configuration.
