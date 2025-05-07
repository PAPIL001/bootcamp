from collections import namedtuple

Book = namedtuple("Book", ["title", "class"], rename=True)
b = Book("1984", "Fiction")
print(b)  # Book(title='1984', _1='Fiction')
