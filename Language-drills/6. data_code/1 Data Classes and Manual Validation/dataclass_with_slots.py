from dataclasses import dataclass

@dataclass(slots=True)
class SlottedUser:
    name: str
    age: int

u8 = SlottedUser("Henry", 33)
print(u8)
# Output: SlottedUser(name='Henry', age=33)
