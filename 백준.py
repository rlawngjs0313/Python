import sys
from heapq import heappop, heappush

N = int(input())
L1 = []
result = 0

if N == 1:
    print(0)
    exit()

for i in range(N):
    heappush(L1, int(sys.stdin.readline()))

while len(L1) != 1:
    temp = heappop(L1) + heappop(L1)
    heappush(L1, temp)
    result += temp

print(result)