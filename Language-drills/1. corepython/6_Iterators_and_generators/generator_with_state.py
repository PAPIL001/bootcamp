def running_total(lst):
    total = 0
    for n in lst:
        total += n
        yield total

for val in running_total([1, 2, 3]):
    print(val)
