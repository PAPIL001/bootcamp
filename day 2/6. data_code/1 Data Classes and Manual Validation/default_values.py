from dataclasses import dataclass

@dataclass
class UserWithCountry:
    name: str
    age: int
    country: str = "India"

u2 = UserWithCountry(name="Bob", age=30)
print(u2)
# Output: UserWithCountry(name='Bob', age=30, country='India')
