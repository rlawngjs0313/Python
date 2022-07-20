import sys
from collections import deque
sys.setrecursionlimit(1000000)

def BFS(node):
    global cnt
    global graph
    cnt += 1
    visited = [node]
    queue = deque()
    queue.append(node)

    while queue:
        A = queue.popleft()
        for i in range(len(graph[A])):
            if graph[A][i] not in visited:
                visited.append(graph[A][i])
                queue.append(graph[A][i])

    for i in visited:
        L1.remove(i)
    if L1:
        BFS(L1[0])
            
        

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
cnt = 0
L1 = list(range(1, N+1))

for i in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])

BFS(1)
print(cnt)