class Book:
    def describe(self):
        return "Generic Book"

class Novel(Book):
    def describe(self):
        return "Novel: " + super().describe()

n = Novel()
print(n.describe())
# Output: Novel: Generic Book
