
class Resource:
    def __enter__(self):
        print("Resource acquired")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Resource released")
        if exc_type:
            print("Handled error")

with Resource():
    print(1 / 0)
# Output:
# Resource acquired
# Resource released
# Handled error
