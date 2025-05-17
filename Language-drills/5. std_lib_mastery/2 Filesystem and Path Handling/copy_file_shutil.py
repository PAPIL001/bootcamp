import shutil
from pathlib import Path

Path("a.txt").write_text("copy me")
shutil.copy("a.txt", "b.txt")
print(Path("b.txt").read_text())
# copy me
