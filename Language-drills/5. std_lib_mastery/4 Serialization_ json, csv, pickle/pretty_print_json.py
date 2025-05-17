import json

data = {"name": "Alice", "age": 25}
print(json.dumps(data, indent=2, sort_keys=True))
# {
#   "age": 25,
#   "name": "Alice"
# }
