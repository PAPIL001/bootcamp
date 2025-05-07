class Book:
    def __init__(self, title=None):
        self.title = title

    def __bool__(self):
        return bool(self.title)

b = Book("1984")
print(bool(b))  # True

empty = Book()
print(bool(empty))  # False
