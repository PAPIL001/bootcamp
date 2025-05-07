class Book:
    def describe(self):
        return "Generic Book"

class Novel(Book):
    def describe(self):
        return "Fictional Novel"

books = [Book(), Novel()]
for b in books:
    print(b.describe())
# Output:
# Generic Book
# Fictional Novel
