# cli.py
import argparse
import importlib
import threading
import time
import yaml
from metrics.store import MetricsStore
from web.app import app, metrics_store
import uvicorn

def start_fastapi_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

def load_processors(config):
    processors = {}
    for node in config["nodes"]:
        tag = node["tag"]
        module_path = node["type"]
        try:
            module = importlib.import_module(module_path)
            processors[tag] = module.process
        except (ImportError, AttributeError) as e:
            print(f"Error loading processor '{tag}' from '{module_path}': {e}")
    return processors

def run_pipeline(processors, input_lines, trace_enabled):
    for line in input_lines:
        queue = [("start", line.strip())]
        trace = []
        while queue:
            tag, current_line = queue.pop(0)
            processor = processors.get(tag)
            if not processor:
                print(f"No processor found for tag '{tag}'")
                continue
            try:
                start_time = time.time()
                output_lines = processor(current_line)
                duration = time.time() - start_time
                metrics_store.record(tag, duration, error=False)
                if trace_enabled:
                    trace.append(tag)
                queue.extend(output_lines)
            except Exception as e:
                print(f"[ERROR] {tag}: {e}")
                metrics_store.record(tag, 0, error=True)
        if trace_enabled and trace:
            metrics_store.add_trace(trace)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input file to process")
    parser.add_argument("config_file", help="YAML config file defining processor pipeline")
    parser.add_argument("--trace", action="store_true", help="Enable line tracing")
    args = parser.parse_args()

    with open(args.input_file) as f:
        input_lines = f.readlines()

    with open(args.config_file) as f:
        config = yaml.safe_load(f)

    processors = load_processors(config)

    # Start FastAPI server in a background thread
    dashboard_thread = threading.Thread(target=start_fastapi_server, daemon=True)
    dashboard_thread.start()
    print("🚀 FastAPI server thread started on http://127.0.0.1:8000")

    # Start pipeline
    run_pipeline(processors, input_lines, args.trace)

if __name__ == "__main__":
    main()
