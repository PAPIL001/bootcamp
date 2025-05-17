from pathlib import Path

# Assuming some .py files exist in current dir
py_files = list(Path(".").glob("*.py"))
print([f.name for f in py_files])
# ['read_file_pathlib.py', 'list_py_files.py', ...]
