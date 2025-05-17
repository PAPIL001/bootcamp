

def calculate_score(grades):
    total_score = sum(grades)
    return total_score / len(grades)

# Example usage
grades = [85, 90, 78, 92]
print(f"Average Score: {calculate_score(grades)}")  # Expected Output: Average Score: 86.25
