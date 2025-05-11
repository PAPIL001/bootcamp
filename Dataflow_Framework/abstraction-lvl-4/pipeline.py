import yaml
import importlib
from processor_types import StreamProcessor

def load_pipeline(config_path: str) -> list[StreamProcessor]:
    with open(config_path) as f:
        config = yaml.safe_load(f)

    processors = []
    for step in config.get("pipeline", []):
        dotted_path = step["type"]
        options = step.get("options", {})

        module_path, class_name = dotted_path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        cls_or_fn = getattr(module, class_name)

        if callable(cls_or_fn):
            processor = cls_or_fn(**options) if options else cls_or_fn()
            processors.append(processor)
        else:
            raise ImportError(f"{dotted_path} is not callable")
    return processors
