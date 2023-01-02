import sys
from heapq import heapify, heappop, heappush

N = int(input())
L1 = []
result = 0

temp1 = list(map(int, sys.stdin.readline().split()))
temp2 = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    heappush(L1, [temp2[i], temp1[i]])

while L1:
    if L1[0][1] < L1[0][0]:
        x = (L1[0][0] - L1[0][1]) // 30
        if (L1[0][0] - L1[0][1]) % 30 != 0:
            x += 1
        L1[0][1] += 30*x
        result += x
    for i in L1:
        if L1[0][1] >= i[1] and L1[0][0] < i[0]:
            x = (L1[0][1] - i[1]) // 30
            if (L1[0][1] - i[1]) % 30 != 0:
                x += 1
            i[1] += 30*x
            result += x 
    heappop(L1)

print(result)