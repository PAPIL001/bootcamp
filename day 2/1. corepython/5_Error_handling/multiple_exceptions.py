try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Value error")
except ZeroDivisionError:
    print("Division error")
  
