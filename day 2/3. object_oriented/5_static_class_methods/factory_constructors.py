class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def unit_circle(cls):
        return cls(1)

c = Circle.unit_circle()
print(c.radius)  # 1
