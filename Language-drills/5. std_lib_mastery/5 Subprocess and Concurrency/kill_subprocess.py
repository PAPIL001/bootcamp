import subprocess
import time

proc = subprocess.Popen(["python", "-c", "import time; time.sleep(5)"])
time.sleep(1)
proc.terminate()
print("Process terminated:", proc.poll() is not None)
# Output:
# Process terminated: True
