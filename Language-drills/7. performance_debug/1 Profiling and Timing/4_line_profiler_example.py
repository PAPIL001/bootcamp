
@profile
def expensive_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

expensive_function()

Expected output:
Timer unit: 1e-06 s

Total time: 0.12 s
File: 7_1_4_line_profiler_example.py
Function: expensive_function at line 5

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     5    1000001      123456      0.1     100.0      total = 0
     6    1000000      234567      0.2      60.0      for i in range(1000000):
     7    1000000      234567      0.2      60.0          total += i
     8    1000000      234567      0.2      60.0      return total
