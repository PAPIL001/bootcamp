from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableUser:
    name: str
    age: int

u4 = ImmutableUser(name="Diana", age=40)
print(u4)
# Output: ImmutableUser(name='Diana', age=40)

try:
    u4.age = 50
except Exception as e:
    print(e)
# Output: cannot assign to field 'age'
