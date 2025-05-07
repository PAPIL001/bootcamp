# Inline Function Composition
def compose(f, g):
    return lambda x: f(g(x))

# Test composition of functions
print(compose(str, abs)(-7))  # Expected: '7'
