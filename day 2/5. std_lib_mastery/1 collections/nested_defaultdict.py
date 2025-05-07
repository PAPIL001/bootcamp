from collections import defaultdict

nested = defaultdict(lambda: defaultdict(int))
nested["group1"]["itemA"] += 1
nested["group1"]["itemB"] += 2
print(dict(nested))
# {'group1': {'itemA': 1, 'itemB': 2}}
