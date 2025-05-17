def manual():
    raise StopIteration("Done")

try:
    manual()
except StopIteration as e:
    print("Caught:", e)
