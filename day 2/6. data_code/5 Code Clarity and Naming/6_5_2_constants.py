
MAX_RETRIES = 3

def connect_to_server():
    retries = 0
    while retries < MAX_RETRIES:
        print(f"Attempt {retries + 1}")
        retries += 1

connect_to_server()  # Expected Output: Attempt 1, Attempt 2, Attempt 3
