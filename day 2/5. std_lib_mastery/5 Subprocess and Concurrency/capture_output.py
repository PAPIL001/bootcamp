import subprocess

result = subprocess.run(["echo", "Hi"], capture_output=True, text=True)
print("Captured:", result.stdout.strip())
# Captured: Hi
