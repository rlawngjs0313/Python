from collections import deque, defaultdict

N, K = map(int, input().split())
visited = defaultdict(int)
queue = deque([N])
cnt = 0

while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        if node == K:
            print(cnt)
            exit()
        for i in (node-1, node+1, 2*node):
            if 0 <= i <= 100000 and visited.get(i) != 1:
                queue.append(i)
        visited[node] = 1
    cnt += 1