from collections import deque
import sys
sys.setrecursionlimit(1000000)

def BFS(list, nullspace):
    queue = deque(list)
    index = len(list) + nullspace
    end = M*N
    cnt = 0

    while queue:
        if index == end:
            return cnt
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for i in ([y, x+1], [y, x-1], [y+1, x], [y-1, x]):
                if (i[1] < 0 or i[1] >= M) or (i[0] < 0 or i[0] >= N):
                    continue
                if graph[i[0]][i[1]] == -1 or graph[i[0]][i[1]] == 1:
                    continue
                graph[i[0]][i[1]] = 1
                index += 1
                queue.append(i)
        cnt += 1
    return cnt


M, N = map(int, sys.stdin.readline().split())
graph = []
L1 = []
nullspace = 0
AllFull = False

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    if 0 not in data and -1 not in data:
        AllFull = True
    else:
        allFull = False
    graph.append(data)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            L1.append([i, j])
        elif graph[i][j] == -1:
            nullspace += 1

if AllFull:
    print(0)
else:
    result = BFS(L1, nullspace)
    for i in graph:
        if 0 in i:
            print(-1)
            break
    else:
        print(result)