import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = deque([N])

for i in range(N-1,0,-1):
    L1.appendleft(i)
    for _ in range(i):
        L1.appendleft(L1.pop())

for i in list(L1):
    print(f"{i} ")