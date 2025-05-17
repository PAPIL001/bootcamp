class Book:
    def describe(self):
        return "Generic Book"

class Novel(Book):
    def describe(self):
        return "Novel: A fictional narrative"

n = Novel()
print(n.describe())
# Output: Novel: A fictional narrative
