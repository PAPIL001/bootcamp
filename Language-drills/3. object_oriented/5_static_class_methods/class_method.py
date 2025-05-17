class Book:
    books = []

    @classmethod
    def add_book(cls, title):
        cls.books.append(title)

Book.add_book("1984")
print(Book.books)  # ['1984']
