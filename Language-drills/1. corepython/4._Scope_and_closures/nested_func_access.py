def outer():
    msg = "hello"
    def inner():
        print(msg)
    inner()

outer()
