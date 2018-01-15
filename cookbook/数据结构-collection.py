# 保存最后N个元素
from collections import deque

l1 = [1, 3, 5, 7, 22, 33, 44]

q = deque(maxlen=3)
lt = []
for i in range(len(l1)):
    q.append(l1[i])
    lt.append((l1[i]))

print(q)   # deque([22, 33, 44], maxlen=3)
print(lt)  # [1, 3, 5, 7, 22, 33, 44]

# deque 另一个重要应用是队列
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3])
q.appendleft(4)
print(q)  # deque([4, 1, 2, 3])
print(q.pop())  # 3
print(q.popleft())  # 4
print(q)  # deque([1, 2])