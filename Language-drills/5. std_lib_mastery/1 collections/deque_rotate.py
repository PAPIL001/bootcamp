from collections import deque

dq = deque([1, 2, 3, 4])
dq.rotate(2)
print(list(dq))
# [3, 4, 1, 2]
