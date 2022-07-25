import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
L1 = deque(list(range(1, N+1)))
result = []

while len(L1) != 0:
    for i in range(K-1):
        data = L1.popleft()
        L1.append(data)
    result.append(L1.popleft())
print(str(result).replace("[", "<").replace("]", ">"))