import sys
sys.setrecursionlimit(1000000)

cnt = 0

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if graph[y][x] == 0:
        return
    graph[y][x] = 0

    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

T = int(sys.stdin.readline())
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0]*M for k in range(N)]
    for j in range(K):
        data = list(map(int, sys.stdin.readline().split()))
        graph[data[1]][data[0]] = 1
    
    for j in range(M):
        for k in range(N):
            if graph[k][j] == 1:
                dfs(j, k)
                cnt += 1
    sys.stdout.write(f"{cnt}" + "\n")
    cnt = 0