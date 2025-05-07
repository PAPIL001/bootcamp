from collections import OrderedDict

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3

for k, v in od.items():
    print(k, v)
# first 1
# second 2
# third 3
