class Book:
    def __init__(self, title):
        self.title = title

    def __lt__(self, other):
        return self.title < other.title

b1 = Book("Animal Farm")
b2 = Book("Brave New World")
print(b1 < b2)  # True
