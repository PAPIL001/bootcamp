import json

safe_data = {"task": "serialize", "status": True}
json_str = json.dumps(safe_data)
print(json.loads(json_str))  # {'task': 'serialize', 'status': True}
