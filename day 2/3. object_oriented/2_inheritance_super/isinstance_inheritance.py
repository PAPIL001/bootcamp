class Book:
    pass

class Novel(Book):
    pass

n = Novel()
print(isinstance(n, Novel))  # True
print(isinstance(n, Book))   # True
# Output:
# True
# True
