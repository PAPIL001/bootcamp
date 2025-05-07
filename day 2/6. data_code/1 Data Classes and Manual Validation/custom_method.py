from dataclasses import dataclass

@dataclass
class AdultCheckUser:
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18

u5 = AdultCheckUser(name="Eve", age=20)
print(u5.is_adult())
# Output: True
