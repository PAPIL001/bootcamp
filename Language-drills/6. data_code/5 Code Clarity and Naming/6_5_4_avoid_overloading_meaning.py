

def calculate_average_temperature(temperatures):
    return sum(temperatures) / len(temperatures)

# Example usage
temperatures = [22.5, 24.0, 21.3, 23.5]
print(f"Average Temperature: {calculate_average_temperature(temperatures)}")  # Expected Output: Average Temperature: 22.825
