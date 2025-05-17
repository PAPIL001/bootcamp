import threading

count = 0
lock = threading.Lock()

def increment():
    global count
    for _ in range(1000):
        with lock:
            count += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final count:", count)
# Output:
# Final count: 10000
