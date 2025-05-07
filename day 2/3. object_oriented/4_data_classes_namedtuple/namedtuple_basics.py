from collections import namedtuple

Book = namedtuple("Book", ["title", "author"])

b = Book("1984", "Orwell")
print(b.title)  # 1984
print(b.author)  # Orwell
