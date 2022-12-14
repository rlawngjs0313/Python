import sys
from heapq import heappop, heappush

N = int(input())
L1 = []
L2 = []
L3 = []
result = 0

for i in range(N):
    temp = int(sys.stdin.readline())
    if temp < 0:
        heappush(L1, temp)
    elif temp > 1:
        heappush(L2, -1*temp)
    else:
        heappush(L3, temp)

while L2 != []:
    temp = -1*heappop(L2)
    if L2 != []:
        temp *= -1*heappop(L2)
        result += temp
    else:
        result += temp

while L1 != []:
    temp = heappop(L1)
    if L1 != []:
        temp *= heappop(L1)
        result += temp
    else:
        if L3 != [] and L3[0] == 0:
            heappop(L3)
        else:
            result += temp

result += sum(L3)
print(result)