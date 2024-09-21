N, M = map(int, input().split())
L1 = list(range(1, N+1))

visited = [False for _ in range(N)]
L2 = []
def DFS(d):
    if d == M:
        print(*L2)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            L2.append(L1[i])
            DFS(d+1)
            visited[i] = False
            L2.pop()

DFS(0)