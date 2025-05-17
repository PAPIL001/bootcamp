try:
    with open('nonexistent.txt') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
# Output: File not found
