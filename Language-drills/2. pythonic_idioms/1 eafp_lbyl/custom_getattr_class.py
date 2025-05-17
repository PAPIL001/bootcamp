class MyClass:
    def __getattr__(self, name):
        return f"Attribute {name} not found"
obj = MyClass()
print(obj.some_attr)  # Output: Attribute some_attr not found
