# Class Method Decorator
def validate_args(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            raise ValueError("All arguments must be integers")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    @validate_args
    def add(self, a, b):
        return a + b

obj = MyClass()
print(obj.add(2, 3))  # Expected: 5
print(obj.add(2, "3"))  # Expected: ValueError: All arguments must be integers
