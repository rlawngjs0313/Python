import sys

# 마주보는 면이 1개만 존재하는가
# DFS로 첫번째의 면부터 탐색하면서 탐색 횟수와 탐색 시작한 면의 숫자, x, y 좌표를 이용
# 마주보는 면을 result에 저장함

def DFS(x, y, direction, newDirect, cnt, num):
    if cnt == 2 and direction == newDirect: # 마주보는 면인가?
        result[num].append(graph[x][y]) # 그렇다면 저장
        return

    visit[x][y] = 1 # 방문했다는 표시

    for i in range(4): # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx > 5 or ny < 0 or ny > 5: # 범위에 벗어났는가?
            continue
        if graph[nx][ny] == 0: # 0이 아닌 수 인가?
            continue
        if visit[nx][ny] == 1: # 방문했던 노드인가?
            continue
        # 모두 아니라면 (새로운 면)
        if direction == i: # 지금 탐색이 그 방향의 첫번째인가?
            cnt += 1 # 그렇다면 2번째로
        visit[nx][ny] = 1 # 탐색한 노드 방문 처리
        DFS(nx, ny, direction, i, cnt, num) # 새로 탐색한 것을 기준으로 재탐색

        if direction == i: # result에 적었다면
            cnt -= 1 # 다시 초기화

    return 0 # 모두 방문했을 경우 빠져나옴


graph, result = [], [[] for _ in range(7)] # initial

dx = [0, 0, 1, -1] # 우, 좌
dy = [1, -1, 0, 0] # 하, 상
for _ in range(6): # 데이터 수집
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

for x in range(6): # 데이터 하나 하나 체크
    for y in range(6):
        if graph[x][y] != 0: # 만약 면이라면
            for i in range(4): # 기준 잡고 상하좌우 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > 5 or ny < 0 or ny > 5: # 범위를 벗어났는가?
                    continue
                if graph[nx][ny] == 0: # 면이 아닌가?
                    continue

                visit = [[0] * 6 for _ in range(6)] # 방문 처리를 위해
                visit[x][y] = 1 # 처음 면 방문 처리
                DFS(nx, ny, i, i, 1, graph[x][y]) # 그 이후 DFS로 탐색

possible = True
for item in result[1:]: # result를 살피면서 모두 짝이 있는지 확인
    if len(item) != 1: # 만약 짝이 두개거나 아예 없는 경우
        possible = False # 만들 수 없음

if possible: # 만약 만들 수 있다면
    print(result[1][0]) # 1과 마주한 면을 출력
else: # 그게 아니면
    print(0) # 0 출력
