from typing import Callable, Dict, List, Tuple

class DAG:
    def __init__(self):
        self.nodes: Dict[str, Callable] = {}
        self.edges: Dict[str, List[Tuple[str, str]]] = {}

    def add_node(self, name: str, processor: Callable):
        self.nodes[name] = processor
        self.edges[name] = []

    def add_edge(self, source: str, target: str, tag: str = None):
        self.edges[source].append((target, tag))

    def process(self, line: str):
        self._walk("input", line)

    def _walk(self, node: str, line: str):
        if node not in self.nodes:
            return
        for tag, result in self.nodes[node](line):
            for target, edge_tag in self.edges.get(node, []):
                if edge_tag is None or edge_tag == tag:
                    self._walk(target, result)
