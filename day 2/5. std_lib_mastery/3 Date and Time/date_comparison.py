from datetime import date

d1 = date(2024, 5, 1)
d2 = date(2025, 5, 6)
print("Earlier date is:", d1 if d1 < d2 else d2)
# Earlier date is: 2024-05-01
