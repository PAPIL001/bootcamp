from dataclasses import dataclass

@dataclass(frozen=True)
class Book:
    title: str

b = Book("1984")
# b.title = "New Title"  # Raises: FrozenInstanceError
print(b.title)  # 1984
