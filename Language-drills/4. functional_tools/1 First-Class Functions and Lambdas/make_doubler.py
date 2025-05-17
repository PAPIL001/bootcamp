# Return Function from Function
def make_doubler():
    return lambda x: x * 2

# Create a doubler function and test
doubler = make_doubler()
print(doubler(4))  # Expected: 8
