import sys
from itertools import combinations
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int,input().split())
L1 = []
L2 = []
INF = 1e10

for i in range(N):
    word = list(map(int,input().split()))
    for j in range(N):
        if word[j] == 1:
            L1.append((i,j))
        elif word[j] == 2:
            L2.append((i,j))

result = INF
for i in list(combinations(L2,M)):
    temp = [INF]*len(L1)
    for j in i:
        for k in range(len(L1)):
            temp[k] = min(temp[k],abs(j[0]-L1[k][0])+abs(j[1]-L1[k][1]))
    result = min(result,sum(temp))
print(f"{result}\n")