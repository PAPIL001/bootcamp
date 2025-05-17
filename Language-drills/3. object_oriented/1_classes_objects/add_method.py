class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

book = Book("1984", "Orwell")
print(book.describe())  # Output: '1984' by Orwell
