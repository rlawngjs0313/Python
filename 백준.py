import sys
import heapq

N = int(input())
L1 = []
result = []

for i in range(N):
    L1.append(list(map(int, sys.stdin.readline().split())))

L1.sort(key=lambda x:(x[0], x[1]))
heapq.heappush(result, L1.pop(0)[1])

for i in L1:
    if i[0] < result[0]:
        heapq.heappush(result, i[1])
    else:
        heapq.heappop(result)
        heapq.heappush(result, i[1])

print(len(result))