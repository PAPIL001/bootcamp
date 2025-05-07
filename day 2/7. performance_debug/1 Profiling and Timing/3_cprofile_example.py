
def expensive_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

expensive_function()


expected output:

         4 function calls in 0.125 seconds
         1    0.000    0.000    0.125    0.125 <script_name>.py:4(expensive_function)
         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
