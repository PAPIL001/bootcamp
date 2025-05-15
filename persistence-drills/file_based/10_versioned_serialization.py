import pickle
from typing import Optional


class BookV1:
    """Initial version of the Book class."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"BookV1(title={self.title}, author={self.author})"


class BookV2:
    """Updated version of the Book class with more attributes."""
    def __init__(self, title: str, author: str, year: Optional[int] = None):
        self.title = title
        self.author = author
        self.year = year  # New field added in V2

    def __repr__(self):
        return f"BookV2(title={self.title}, author={self.author}, year={self.year})"


def save_book(book, filename: str):
    """Save a book instance to a file."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_book(filename: str):
    """Load a book instance from a file, handling different versions."""
    with open(filename, "rb") as f:
        book = pickle.load(f)

    # Handle versioning logic
    if isinstance(book, BookV1):
        print("Loaded BookV1, before upgrading:")
        print(book)  # Print old version before upgrading
        print("Upgrading to BookV2...")
        # Upgrade BookV1 to BookV2 (set default year if not provided)
        return BookV2(book.title, book.author, year=2000)  # Default year as an example

    return book  # Return BookV2 as is

# Save version 1
book_v1 = BookV1("XYZ", "ABC")
save_book(book_v1, "book_v1.pkl")

# load older version
restored_book_v2 = load_book("book_v1.pkl")

print("\nRestored Book (Upgraded):")
print(restored_book_v2)

