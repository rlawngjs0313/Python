import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

R,C = map(int,input().split())
L1 = [[] for _ in range(R)]

for i in range(R):
    word = input().rstrip()
    for j in word:
        L1[i].append(j)

def BFS(a,b,cnt):
    global result
    for x,y in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
        if (0<=x<R and 0<=y<C) and not visited[L1[x][y]]:
            visited[L1[x][y]] = True
            BFS(x,y,cnt+1)
            visited[L1[x][y]] = False
    result = max(result,cnt)

result = 0
visited = defaultdict(bool)
visited[L1[0][0]] = True
BFS(0,0,1)
print(f"{result}\n")