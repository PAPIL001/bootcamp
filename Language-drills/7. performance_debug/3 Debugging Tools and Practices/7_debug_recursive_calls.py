# Debug Recursive Calls: Log call stack depth using an argument like level or indent.
def factorial(n, level=0):
    print(f"{'  ' * level}factorial({n})")
    if n == 1:
        return 1
    return n * factorial(n-1, level+1)

# Example usage
factorial(5)

# Expected Output:
# factorial(5)
#   factorial(4)
#     factorial(3)
#       factorial(2)
#         factorial(1)
