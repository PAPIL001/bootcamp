class Book:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title == other.title

    def __hash__(self):
        return hash(self.title)

book_set = {Book("1984"), Book("1984")}
print(len(book_set))  # 1
