# Python 3.7+ breakpoint(): Insert breakpoint() and run script to enter debugger.
def multiply(a, b):
    result = a * b
    breakpoint()  # Execution will pause here, similar to pdb.set_trace()
    return result

# Example usage
multiply(3, 4)

# Expected Output:
# (Break will pause execution at breakpoint(), allowing inspection of local variables)
# a = 3
# b = 4
# result = 12
