data = {'name': 'Alice'}
try:
    print(data['age'])
except KeyError:
    print("Key not found")
    
# Output: Key not found
