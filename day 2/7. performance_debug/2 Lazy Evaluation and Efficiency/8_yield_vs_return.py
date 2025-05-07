
def generate_numbers():
    for i in range(100):
        yield i

# Example usage: Instead of appending to a list, use a generator
for number in generate_numbers():
    print(number)
