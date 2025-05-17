import subprocess

result = subprocess.run(["python", "-c", "exit(1)"])
print("Exit code:", result.returncode)
# Exit code: 1
