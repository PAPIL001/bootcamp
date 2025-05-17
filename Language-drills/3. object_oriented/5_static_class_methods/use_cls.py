class Book:
    def __init__(self, title):
        self.title = title

    @classmethod
    def from_string(cls, data):
        return cls(data)

b = Book.from_string("1984")
print(b.title)  # 1984
