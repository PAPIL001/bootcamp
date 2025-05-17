from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]
top_two = Counter(numbers).most_common(2)
print(top_two)
# [(3, 3), (2, 2)]
