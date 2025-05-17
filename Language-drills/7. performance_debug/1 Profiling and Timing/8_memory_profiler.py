
from memory_profiler import profile

@profile
def expensive_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

expensive_function()

Expected output:

Line #    Mem usage    Increment   Line Contents
================================================
     5     10.5 MiB     0.0 MiB     @profile
     6     10.6 MiB     0.1 MiB     def expensive_function():
     7     10.7 MiB     0.1 MiB         total = 0
     8     11.1 MiB     0.4 MiB         for i in range(1000000):
     9     11.5 MiB     0.4 MiB             total += i
    10     11.6 MiB     0.1 MiB         return total
