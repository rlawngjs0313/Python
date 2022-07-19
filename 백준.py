import sys
import heapq

N = int(input())
L1 = []

for i in range(N):
    data = int(sys.stdin.readline())
    if data == 0:
        if len(L1) != 0:
            print(heapq.heappop(L1))
        else:
            print(0)
    else:
        heapq.heappush(L1, data)