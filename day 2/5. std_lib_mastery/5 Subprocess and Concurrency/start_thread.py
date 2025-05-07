import threading

def greet():
    print("Hello from thread")

t = threading.Thread(target=greet)
t.start()
t.join()
# Output:
# Hello from thread
