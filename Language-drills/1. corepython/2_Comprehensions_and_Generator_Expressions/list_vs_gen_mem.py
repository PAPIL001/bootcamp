import sys

lst = [x for x in range(1000000)]
gen = (x for x in range(1000000))

print("List:", sys.getsizeof(lst))
print("Gen:", sys.getsizeof(gen))
