import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N,Q = map(int,input().split())
L1 = []
D1 = {}
for _ in range(N):
    a,b = map(int,input().split())
    L1.append(a)
    D1[a] = b
L1.sort()

for _ in range(Q):
    result = 0
    u,v,x,y = map(int,input().split())
    for i in L1[bisect_left(L1,u):bisect_right(L1,v)]:
        if x <= D1[i] <= y:
            result += 1
    print(result)