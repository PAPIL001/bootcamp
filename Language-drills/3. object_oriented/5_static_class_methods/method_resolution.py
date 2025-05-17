class A:
    @staticmethod
    def show():
        return "A"

class B(A):
    pass

print(B.show())  # A
