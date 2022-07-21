import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
L1 = [0]
temp = 0

for i in data:
    temp += i
    L1.append(temp)

for i in range(M):
    index = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(str(L1[index[1]] - L1[index[0]-1]) + '\n')