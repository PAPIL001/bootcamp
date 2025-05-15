import json

class Node:
    def __init__(self, id: int, label: str):
        self.id = id
        self.label = label

    def to_dict(self):
        return {"id": self.id, "label": self.label}

class Edge:
    def __init__(self, from_node: int, to_node: int, weight: float = 1.0):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def to_dict(self):
        return {
            "from": self.from_node,
            "to": self.to_node,
            "weight": self.weight
        }

class Graph:
    def __init__(self):
        self.nodes: dict[int, Node] = {}
        self.edges: list[Edge] = []

    def add_node(self, id: int, label: str):
        self.nodes[id] = Node(id, label)

    def add_edge(self, from_node: int, to_node: int, weight: float = 1.0):
        self.edges.append(Edge(from_node, to_node, weight))

    def to_json(self) -> str:
        return json.dumps({
            "nodes": [node.to_dict() for node in self.nodes.values()],
            "edges": [edge.to_dict() for edge in self.edges]
        }, indent=4)

    @classmethod
    def from_json(cls, json_str: str) -> "Graph":
        data = json.loads(json_str)
        graph = cls()
        for node_data in data["nodes"]:
            graph.add_node(node_data["id"], node_data["label"])
        for edge_data in data["edges"]:
            graph.add_edge(edge_data["from"], edge_data["to"], edge_data.get("weight", 1.0))
        return graph

g = Graph()
g.add_node(1, "A")
g.add_node(2,"B")
g.add_node(3, "C")
g.add_node(4,"D")
g.add_edge(1,2,3.3)
g.add_edge(2,3)

# Serialize
json_data = g.to_json()
print("Serialized Graph JSON:")
print(json_data)

# Deserialize
g2 = Graph.from_json(json_data)
print("Deserialized Graph JSON:")
for node_id, node in g2.nodes.items():
    print(f"Node {node_id}: {node.label}")
for edge in g2.edges:
    print(f"Edge from {edge.from_node} to {edge.to_node} with weight {edge.weight}")