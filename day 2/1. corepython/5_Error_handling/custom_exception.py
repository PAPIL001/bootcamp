class InvalidAgeError(Exception):
    pass

age = -1
if age < 0:
    raise InvalidAgeError("Age cannot be negative")
