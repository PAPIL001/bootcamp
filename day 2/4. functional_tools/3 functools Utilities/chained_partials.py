# Chained Partials
from functools import partial

# Create a custom print function
custom_print = partial(print, sep=" - ", end="!\n")

# Test the chained partial
custom_print("Hello", "world")  # Expected: Hello - world!
