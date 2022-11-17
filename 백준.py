import sys, heapq

N, K = map(int,input().split())
Data = []
backpack = []

for _ in range(N):
    Data.append([int(x) for x in sys.stdin.readline().rstrip().split()])
for _ in range(K):
    backpack.append(int(sys.stdin.readline().rstrip()))

Data.sort()
backpack.sort()

result = 0
temp = []

for i in backpack:
    while Data:
        if Data[0][0] <= i:
            heapq.heappush(temp, -Data[0][1])
            heapq.heappop(Data)
        else:
            break

    if temp:
        result += -heapq.heappop(temp)
    elif not Data:
        break

print(result)