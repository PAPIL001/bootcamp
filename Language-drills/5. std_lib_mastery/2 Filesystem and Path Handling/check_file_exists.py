from pathlib import Path

Path("demo.txt").write_text("exists check")
p = Path("demo.txt")
print(p.exists(), p.is_file())
# True True
