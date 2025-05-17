from dataclasses import dataclass

@dataclass
class ComparableUser:
    name: str
    age: int

u7a = ComparableUser("Grace", 22)
u7b = ComparableUser("Grace", 22)
print(u7a == u7b)
# Output: True
