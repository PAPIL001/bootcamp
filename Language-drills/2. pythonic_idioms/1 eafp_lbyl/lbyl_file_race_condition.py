import os
if os.path.exists("nofile.txt"):
    with open("nofile.txt") as f:
        content = f.read()
else:
    content = "File not found"
print(content)  

# Output: File not found
