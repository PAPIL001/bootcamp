from pathlib import Path

Path("output.txt").write_text("hello")
print(Path("output.txt").read_text())
# hello
