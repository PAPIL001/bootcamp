import yaml
from routing import DAG
from processors import core, tagging, counting

PROCESSOR_MAP = {
    "trim": core.trim,
    "tag_error": tagging.tag_error,
    "tag_warn": tagging.tag_warn,
    "count": counting.count_lines,
    "print": core.pretty_print,
}

def load_pipeline(config_path: str) -> DAG:
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    dag = DAG()

    # Register nodes
    for node in config["nodes"]:
        name = node["name"]
        ptype = node["type"]
        fn = PROCESSOR_MAP[ptype]
        dag.add_node(name, fn)

    # Add routing
    for edge in config["edges"]:
        dag.add_edge(edge["from"], edge["to"], edge.get("tag"))

    return dag
