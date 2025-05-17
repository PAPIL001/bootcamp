try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner value error")
        raise
except Exception:
    print("Outer caught exception")
