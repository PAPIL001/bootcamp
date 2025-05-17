from dataclasses import dataclass, field

@dataclass
class TaggedUser:
    name: str
    tags: list[str] = field(default_factory=list)

u6 = TaggedUser(name="Frank")
u6.tags.append("admin")
print(u6.tags)
# Output: ['admin']
