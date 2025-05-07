

import random
import time

# Custom sort function (Bubble sort)
def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = random.sample(range(1, 1000), 100)

# Time built-in sorted
start_time = time.time()
sorted(arr)
end_time = time.time()
print(f"Built-in sorted execution time: {end_time - start_time:.6f} seconds")  # Expected Output: <time_value>

# Time custom sort
start_time = time.time()
custom_sort(arr)
end_time = time.time()
print(f"Custom sort execution time: {end_time - start_time:.6f} seconds")  # Expected Output: <time_value>
