from multiprocessing import Process

def compute():
    print("Computing in process")

p = Process(target=compute)
p.start()
p.join()
# Output:
# Computing in process
