from pydantic import BaseModel, Field

class Settings(BaseModel):
    timeout: int = Field(..., description="Timeout in seconds")

print(Settings.schema())
# Output: Tooltip for timeout shown in IDEs with schema metadata
