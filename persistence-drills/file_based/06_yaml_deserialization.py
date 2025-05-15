import yaml

class Car:
    def __init__(self, make: str, model: str, year: int, features: list[str]):
        self.make = make
        self.model = model
        self.year = year
        self.features = features

    @classmethod
    def from_yaml(cls, yaml_string: str) -> "Car":
        data = yaml.safe_load(yaml_string)
        return cls(**data)

with open("car.yaml") as f:
    yaml_string = f.read()

# Deserialize from YAML string
car = Car.from_yaml(yaml_string)
print("Deserialized Car object:")
print(vars(car))
