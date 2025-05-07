from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

b = Book("1984", "Orwell")
print(b)  # Book(title='1984', author='Orwell')
