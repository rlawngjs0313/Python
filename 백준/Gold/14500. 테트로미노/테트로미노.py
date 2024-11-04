import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
L1 = [list(map(int, input().split())) for _ in range(N)]
exe = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(0,1),(1,0),(1,1)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(1,0),(1,1),(1,2),(0,2)],
    [(0,0),(1,0),(0,1),(0,2)],
    [(0,1),(1,1),(2,1),(2,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(0,1),(2,0)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(1,0),(1,1),(2,1)],
    [(0,1),(0,2),(1,1),(1,0)],
    [(0,1),(1,1),(1,0),(2,0)],
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,0),(1,0),(2,0),(1,1)],
    [(1,0),(1,1),(0,1),(1,2)],
    [(0,1),(1,1),(1,0),(2,1)]]
result = 0

def BF(exe):
    result = 0
    for a in range(N):
        for b in range(M):
            temp = 0
            for i,j in exe:
                if 0<=i+a<N and 0<=j+b<M:
                    temp += L1[i+a][j+b]
                else:
                    break
            else:
                result = max(result, temp)
    return result

for i in exe:
    result = max(result,BF(i))

print(f"{result}\n")