class BookShelf:
    def __init__(self, books):
        self.books = books

    def __getitem__(self, index):
        return self.books[index]

shelf = BookShelf(["1984", "Animal Farm"])
print(shelf[1])  # Animal Farm
