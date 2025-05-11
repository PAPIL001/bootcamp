def tag_error(line: str):
    if "error" in line.lower():
        yield ("errors", line)
    else:
        yield ("general", line)

def tag_warn(line: str):
    if "warn" in line.lower():
        yield ("warnings", line)
    else:
        yield ("general", line)
