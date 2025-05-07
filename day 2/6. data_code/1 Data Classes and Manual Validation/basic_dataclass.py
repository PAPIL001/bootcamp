from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User(name="Alice", age=25)
print(u1)
# Output: User(name='Alice', age=25)
