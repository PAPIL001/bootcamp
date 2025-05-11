# pipeline.py
import yaml
import importlib
from processor_types import ProcessorFn

def load_pipeline(config_path: str) -> list[ProcessorFn]:
    with open(config_path) as f:
        config = yaml.safe_load(f)

    processors = []
    for step in config.get("pipeline", []):
        dotted_path = step["type"]
        try:
            module_path, func_name = dotted_path.rsplit(".", 1)
            module = importlib.import_module(module_path)
            processor = getattr(module, func_name)
            if not callable(processor):
                raise TypeError(f"{dotted_path} is not callable")
            processors.append(processor)
        except (ImportError, AttributeError, TypeError) as e:
            raise ImportError(f"Failed to import processor '{dotted_path}': {e}")
    return processors
