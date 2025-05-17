from dataclasses import dataclass

@dataclass
class Item:
    title: str

@dataclass
class Book(Item):
    author: str

b = Book("1984", "Orwell")
print(b)  # Book(title='1984', author='Orwell')
