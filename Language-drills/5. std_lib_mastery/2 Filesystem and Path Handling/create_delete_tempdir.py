import os, shutil
from pathlib import Path

os.makedirs("temp_dir/sub", exist_ok=True)
Path("temp_dir/file.txt").write_text("test")
shutil.rmtree("temp_dir")
print("Temporary directory deleted.")
# Temporary directory deleted.
