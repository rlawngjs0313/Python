import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
print = sys.stdout.write

def BFS(start,end):
    queue = [(start,0)]
    visited = [False for _ in range(n+1)]

    while queue:
        node,cost = queue.pop()
        for i,j in graph[node]:
            if i == end:
                return cost+j
            if not visited[i]:
                queue.append((i,cost+j))
            visited[i] = True

n = int(input())
graph = defaultdict(list)
if n == 1:
    print('0\n')
    exit()

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

L1 = []
for i in graph.keys():
    if len(graph[i]) == 1:
        heappush(L1,(-BFS(i,1),i))

_,s = heappop(L1)
result = 0
for _,i in L1:
    result = max(result,BFS(s,i))

print(f"{result}\n")