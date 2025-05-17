# Use pdb.set_trace(): Pause execution in a function and inspect local variables.
import pdb

def calculate(a, b):
    result = a + b
    pdb.set_trace()  # Execution will pause here, allowing you to inspect variables.
    return result

# Example usage
calculate(5, 7)

# Expected Output:
# (PDB will pause execution at pdb.set_trace() and allow inspection of local variables)
# You can inspect:
# a = 5
# b = 7
# result = 12
