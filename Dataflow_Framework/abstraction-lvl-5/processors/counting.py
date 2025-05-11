def count_lines():
    count = 0
    def _processor(line: str):
        nonlocal count
        count += 1
        yield ("counted", f"[{count}] {line}")
    return _processor


