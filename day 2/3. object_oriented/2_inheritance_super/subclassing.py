class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Novel(Book):
    pass

n = Novel("1984", "George Orwell")
print(n.title, "-", n.author)
# Output: 1984 - George Orwell

