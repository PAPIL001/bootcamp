
from contextlib import suppress
with suppress(FileNotFoundError):
    open("nofile.txt")
print("Continued")  # Output: Continued
