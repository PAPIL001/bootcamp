
import itertools

def generate_lines():
    for i in range(100):
        yield f"Line {i}"

# Use islice to get the first 10 lines
for line in itertools.islice(generate_lines(), 10):
    print(line)
