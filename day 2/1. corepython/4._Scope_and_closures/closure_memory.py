def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

triple = make_multiplier(3)
print(triple(10))
