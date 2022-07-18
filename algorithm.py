# DFS
def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if graph[y][x] == 0:
        return
    graph[y][x] = 0
    # 탐색한 노드 지우기

    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    # 상하좌우 탐색
M = "X축"
N = "Y축"
graph = "트리, 그래프"