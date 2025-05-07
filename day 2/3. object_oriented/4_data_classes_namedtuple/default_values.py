from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str = "Unknown"

b = Book("1984")
print(b)  # Book(title='1984', author='Unknown')
