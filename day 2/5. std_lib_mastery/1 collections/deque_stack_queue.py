from collections import deque

dq = deque()
dq.append("a")       # queue end
dq.appendleft("b")   # stack top
dq.pop()             # removes 'a'
print(list(dq))
# ['b']
