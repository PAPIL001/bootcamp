
try:
    with open('example.txt', 'w') as f:
        f.write("Hello")
    with open('example.txt', 'r') as f:
        print(f.read())  # Output: Hello
except FileNotFoundError:
    print("File not found")
