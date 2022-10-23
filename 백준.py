import sys

N = int(input())
result = 0
init = [0,0]
L1 = []

for i in range(N):
    L1.append(list(map(int, sys.stdin.readline().split())))

L1.sort(key= lambda x: (x[1], x[0]))

for i in L1:
    if i[0] >= init[1]:
        result += 1
        init = i[:]

print(result)