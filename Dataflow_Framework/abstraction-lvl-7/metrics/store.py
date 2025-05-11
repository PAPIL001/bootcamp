# metrics/store.py
from collections import defaultdict
import threading

class MetricsStore:
    def __init__(self):
        self.metrics = defaultdict(lambda: {"count": 0, "time": 0, "errors": 0})
        self.trace = []
        self.lock = threading.Lock()

    def record(self, processor_name, time_taken, error=False):
        with self.lock:
            self.metrics[processor_name]["count"] += 1
            self.metrics[processor_name]["time"] += time_taken
            if error:
                self.metrics[processor_name]["errors"] += 1

    def get_metrics(self):
        with self.lock:
            return dict(self.metrics)

    def add_trace(self, trace_data):
        with self.lock:
            self.trace.append(trace_data)
            if len(self.trace) > 1000:
                self.trace.pop(0)

    def get_trace(self):
        with self.lock:
            return list(self.trace)

    def get_errors(self):
        with self.lock:
            return {name: data for name, data in self.metrics.items() if data["errors"] > 0}
