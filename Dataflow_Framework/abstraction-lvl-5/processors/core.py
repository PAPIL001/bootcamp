def trim(line: str):
    yield ("next", line.strip())

def pretty_print(line: str):
    print(f">> {line}")
    yield ("done", line)
