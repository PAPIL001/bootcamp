
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    print("Elapsed:", time.time() - start)

with timer():
    for _ in range(1000000): pass
# Output: Elapsed: <some time>
