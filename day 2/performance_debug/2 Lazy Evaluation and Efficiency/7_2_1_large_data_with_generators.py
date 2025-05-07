
def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line

# Example usage (Ensure you have a large file named 'large_file.txt' to test)
for line in read_large_file('large_file.txt'):
    print(line)
