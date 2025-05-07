# Store Functions in List
funcs = [abs, str, hex]
print([f(-42) for f in funcs])  # Expected: [42, '-42', '-0x2a']
