from dataclasses import dataclass

@dataclass(order=True)
class Book:
    title: str

b1 = Book("Animal Farm")
b2 = Book("Brave New World")
print(b1 < b2)  # True
