class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}')"

b = Book("1984")
print(str(b))   # Book: 1984
print(repr(b))  # Book('1984')
