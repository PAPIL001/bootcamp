from pathlib import Path

Path("sample.txt").write_text("Hello from file")
content = Path("sample.txt").read_text()
print(content)
# Hello from file
