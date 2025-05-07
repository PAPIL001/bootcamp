class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
book.rating = 4.8
print(book.rating)  # Output: 4.8
