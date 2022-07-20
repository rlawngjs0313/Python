from collections import deque
import sys
sys.setrecursionlimit(1000000)

def BFS():
    visited = [1]
    queue = deque()
    queue.append(1)

    while queue:
        A = queue.popleft()
        for i in graph[A]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return visited

K = int(input())
N = int(input())
graph = [[] for _ in range(K+1)]

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])

visited = BFS()
cnt = 0

for i in range(2, K+1):
    if i in visited:
        cnt += 1

print(cnt)