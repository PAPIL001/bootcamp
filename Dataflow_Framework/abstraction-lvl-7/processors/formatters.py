# processors/formatters.py

def process(line):
    formatted = f"*** {line.upper()} ***"
    print(f"Formatted line: {formatted}")
    return [("output", formatted)]
