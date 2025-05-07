from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

    def describe(self):
        return f"{self.title} by {self.author}"

b = Book("1984", "Orwell")
print(b.describe())  # 1984 by Orwell
