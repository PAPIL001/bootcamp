import importlib

class Router:
    def __init__(self, config):
        self.config = config
        self.processors = {}
        self._load_processors()

    def _load_processors(self):
        for node in self.config['nodes']:
            module_path = node['type']
            try:
                module = importlib.import_module(module_path)
                processor = getattr(module, 'process')
                self.processors[node['tag']] = processor
            except (ImportError, AttributeError) as e:
                print(f"Error importing {module_path}: {e}")

    def run(self, start_tag, lines):
        queue = [(start_tag, line) for line in lines]
        while queue:
            tag, line = queue.pop(0)
            processor = self.processors.get(tag)
            if not processor:
                print(f"No processor found for tag '{tag}'")
                continue
            try:
                output = processor(line)
                for next_tag, new_line in output:
                    queue.append((next_tag, new_line))
            except Exception as e:
                print(f"Error processing line '{line}' at tag '{tag}': {e}")
