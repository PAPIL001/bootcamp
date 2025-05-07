# Print Resource Usage: Print current memory and CPU info using psutil or os.getloadavg().
import os

def print_resource_usage():
    load_avg = os.getloadavg()  # Get system load average for the last 1, 5, and 15 minutes
    print(f"System Load Average: {load_avg}")

# Example usage
print_resource_usage()

# Expected Output:
# System Load Average: (0.25, 0.30, 0.20)
