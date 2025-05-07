import pickle

obj = {"x": [1, 2, 3], "y": "hello"}
with open("obj.pkl", "wb") as f:
    pickle.dump(obj, f)

with open("obj.pkl", "rb") as f:
    loaded = pickle.load(f)

print(loaded)  # {'x': [1, 2, 3], 'y': 'hello'}
