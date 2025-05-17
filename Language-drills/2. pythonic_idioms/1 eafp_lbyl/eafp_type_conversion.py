val = "abc"
try:
    num = int(val)
except ValueError:
    num = "Conversion failed"
print(num)  # Output: Conversion failed
