import pickle
from typing import List


class MyCollection:
    """A custom collection class that holds multiple objects."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the collection."""
        self.items.append(item)

    def __repr__(self):
        return f"MyCollection(items={self.items})"

    def serialize(self, filename: str):
        """Serialize the collection to a file using pickle."""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize a collection from a file."""
        with open(filename, "rb") as f:
            return pickle.load(f)

# Create a collection
collection = MyCollection()
collection.add_item("XYZ")
collection.add_item("ABC")
collection.add_item("2025")

print("Before serialization:")
print(collection)

# Serialize the collection
collection.serialize("my_collection.pkl")

# Deserialize the collection
restored_collection = MyCollection.deserialize("my_collection.pkl")

print("\nAfter deserialization:")
print(restored_collection)
