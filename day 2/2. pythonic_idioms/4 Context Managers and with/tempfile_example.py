
import tempfile
with tempfile.TemporaryFile(mode='w+') as tmp:
    tmp.write("Temp data")
    tmp.seek(0)
    print(tmp.read())  # Output: Temp data
