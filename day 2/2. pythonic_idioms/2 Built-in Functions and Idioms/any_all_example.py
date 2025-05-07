lst = [1, -2, 3]
print(any(x < 0 for x in lst))  # Output: True
print(all(x > 0 for x in lst))  # Output: False
