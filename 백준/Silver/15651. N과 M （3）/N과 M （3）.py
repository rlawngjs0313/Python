N, M = map(int, input().split())
L1 = list(range(1, N+1))

L2 = []
def DFS(d):
    if d == M:
        print(*L2)
        return
    for i in range(N):
        L2.append(L1[i])
        DFS(d+1)
        L2.pop()

DFS(0)