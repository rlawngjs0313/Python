import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
L1 = []
queue = deque([])
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    word = input().rstrip()
    for j,val in enumerate(word):
        if val == 'I':
            queue.append((i,j))
        elif val == 'X':
            visited[i][j] = True
    L1.append(word)

result = 0
while queue:
    node = queue.popleft()
    if not visited[node[0]][node[1]]:
        if L1[node[0]][node[1]] == 'P':
            result += 1
        for i,j in [[node[0]+1,node[1]],[node[0]-1,node[1]],[node[0],node[1]+1],[node[0],node[1]-1]]:
            if (0<=i<N and 0<=j<M) and not visited[i][j]:
                queue.append((i,j))
            visited[node[0]][node[1]] = True

print(f"{result if result else 'TT'}\n")