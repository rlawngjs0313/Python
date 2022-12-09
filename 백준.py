import sys
from collections import deque

L1 = []
N = int(sys.stdin.readline())
result = 0

for i in range(N):
    L1.append(int(sys.stdin.readline()))

if N == 1:
    print(0)
    exit()

L1.sort()
L1 = deque(L1)
temp = L1.popleft() + L1.popleft()
L2 = [temp]
L1.appendleft(temp)

while len(L1) > 2:
    if L1[0] + L1[1] >= L1[1] + L1[2]:
        tp = L1.popleft()
        temp = L1.popleft() + L1.popleft()
        L1.appendleft(tp)
    else:
        temp = L1.popleft() + L1.popleft()
    L2.append(temp)
    L1.appendleft(temp)

L2.append(sum(L1))
print(sum(L2))