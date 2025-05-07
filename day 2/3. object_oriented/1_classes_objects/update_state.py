class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def update_title(self, new_title):
        self.title = new_title

book = Book("Old Title", "Author")
book.update_title("New Title")
print(book.title)  # Output: New Title
