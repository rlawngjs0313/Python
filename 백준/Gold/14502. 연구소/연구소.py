import sys
from collections import deque
from copy import deepcopy

def BFS(L1, queue):
    localqueue = deque(queue)
    while localqueue != deque([]):
        node = localqueue.popleft()
        L1[node[0]][node[1]] = 2
        for i,j in [(node[0]+1,node[1]), (node[0]-1,node[1]), (node[0],node[1]+1), (node[0],node[1]-1)]:
            if (0<=i<N and 0<=j<M) and (L1[i][j] == 0 and (i,j) not in localqueue):
                localqueue.append((i,j))
    cnt = 0
    for i in L1:
        cnt += i.count(0)
    return cnt

def blocking(L1, cnt):
    global result
    if cnt == 3:
        result = max(BFS(L1,queue),result)
        return 0
    else:
        for i in range(N):
            for j in range(M):
                if L1[i][j] == 0:
                    L1[i][j] = 1
                    blocking(deepcopy(L1),cnt+1)
                    L1[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
Lis = []
queue = []
result = 0

for i in range(N):
    word = list(map(int, sys.stdin.readline().split()))
    Lis.append(word)
    for j in range(len(word)):
        if word[j] == 2:
            queue.append((i,j))

blocking(Lis[:],0)
print(result)