# Expose Metrics: Create a dictionary with counters, timers, etc., updated during execution.
import logging
import time

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

metrics = {
    "processed_items": 0,
    "execution_time": 0.0
}

def process_item(item):
    start_time = time.time()
    # Simulate processing an item
    time.sleep(0.5)
    end_time = time.time()
    
    metrics["processed_items"] += 1
    metrics["execution_time"] += end_time - start_time
    logger.info(f"Metrics: {metrics}")

# Example usage
process_item("item1")
process_item("item2")

# Expected Output:
# INFO:__main__:Metrics: {'processed_items': 1, 'execution_time': 0.5002}
# INFO:__main__:Metrics: {'processed_items': 2, 'execution_time': 1.0004}
