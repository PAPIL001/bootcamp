from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., title="Product Name", example="Apple iPhone")

print(Product.schema())
# Output: Schema includes title and example metadata
