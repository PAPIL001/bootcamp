def process(line):
    if "error" in line.lower():
        print(f"Filtered line: {line}")
        return [("formatters", line)]
    else:
        print(f"Ignored line: {line}")
        return []
