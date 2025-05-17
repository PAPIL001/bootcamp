class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        Book.count += 1

    @staticmethod
    def total_books():
        return Book.count

    @classmethod
    def from_title(cls, title):
        return cls(title)

b = Book.from_title("1984")
print(Book.total_books())  # 1
