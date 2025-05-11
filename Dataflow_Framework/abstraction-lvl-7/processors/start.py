# processors/start.py

def process(line):
    line = line.strip()
    if line:
        print(f"Starting processing: {line}")
        return [("filters", line)]
    return []
