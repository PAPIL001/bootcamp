def echo():
    while True:
        val = yield
        print("Received:", val)

g = echo()
next(g)
g.send("Hello")
g.send("World")
