# Closure with Lambda
def power_maker(n):
    return lambda x: x ** n

# Create a square function and test it
square = power_maker(2)
print(square(5))  # Expected: 25
