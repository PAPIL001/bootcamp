class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
print(isinstance(book, Book))  # Output: True
