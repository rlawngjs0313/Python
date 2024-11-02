import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def BFS(Lis,queue,color):
    queue = deque(queue)
    while queue:
        node = queue.popleft()
        if Lis[node[0]][node[1]] == color:
            for i,j in [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]:
                if (0<=i<N and 0<=j<N) and Lis[i][j] == color:
                    queue.append((i,j))
            Lis[node[0]][node[1]] = ''


N = int(input())
L1, L2 = [], []
for _ in range(N):
    tempL1,tempL2 = [],[]
    for i in input().rstrip():
        if i == 'G':
            tempL2.append('R')
        else:
            tempL2.append(i)
        tempL1.append(i)
    L1.append(tempL1)
    L2.append(tempL2)

result = 0
for i in range(N):
    for j in range(N):
        if L1[i][j] != '':
            BFS(L1,[(i,j)],L1[i][j])
            result += 1
print(f"{result} ")
result = 0
for i in range(N):
    for j in range(N):
        if L2[i][j] != '':
            BFS(L2,[(i,j)],L2[i][j])
            result += 1
print(f"{result}")