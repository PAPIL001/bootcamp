class Dummy:
    pass
obj = Dummy()
value = getattr(obj, 'name', 'Attribute not found')
print(value)  

# Output: Attribute not found

