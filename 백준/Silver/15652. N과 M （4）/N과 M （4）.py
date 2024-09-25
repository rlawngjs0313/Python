N, M = map(int, input().split())
L1 = list(range(1, N+1))

L2 = []
def DFS(d, c):
    if d == M:
        print(*L2)
        return
    for i in range(N):
        if L1[i] >= L1[c]:
            L2.append(L1[i])
            DFS(d+1, i)
            L2.pop()

DFS(0, 0)