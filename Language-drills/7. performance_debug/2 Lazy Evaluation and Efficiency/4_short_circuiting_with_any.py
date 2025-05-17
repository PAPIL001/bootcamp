
my_list = [x for x in range(1000000)]

# Check if any number is divisible by 99
is_divisible = any(x % 99 == 0 for x in my_list)
print(f"Any number divisible by 99: {is_divisible}")  # Expected Output: True/False
