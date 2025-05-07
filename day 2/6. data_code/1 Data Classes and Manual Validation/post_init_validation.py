from dataclasses import dataclass

@dataclass
class ValidatedUser:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative.")

try:
    u3 = ValidatedUser(name="Charlie", age=-5)
except ValueError as e:
    print(e)
# Output: Age cannot be negative.
