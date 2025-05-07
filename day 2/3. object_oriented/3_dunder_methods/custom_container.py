class Library:
    def __init__(self):
        self.books = []

    def add(self, title):
        self.books.append(title)

    def __contains__(self, title):
        return title in self.books

lib = Library()
lib.add("1984")
print("1984" in lib)  # True
