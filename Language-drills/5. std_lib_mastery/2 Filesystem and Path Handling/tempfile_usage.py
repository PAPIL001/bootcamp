import tempfile

with tempfile.NamedTemporaryFile(mode="w+", delete=True) as tf:
    tf.write("temp data")
    tf.seek(0)
    print(tf.read())
# temp data
