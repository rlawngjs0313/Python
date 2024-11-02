import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

M, N, H = map(int, input().split())
L1 = []
queue = deque([])
for i in range(H):
    temp_L1 = []
    for j in range(N):
        word = list(map(int, input().split()))
        for k in range(M):
            if word[k] == 1:
                queue.append((i,j,k))
                word[k] = 0
        temp_L1.append(word)
    L1.append(temp_L1)

result = 0
while queue:
    temp = []
    boolean = False
    while queue:
        node = queue.popleft()
        if L1[node[0]][node[1]][node[2]] == 0:
            boolean = True
            L1[node[0]][node[1]][node[2]] = 1
            for i,j,k in [(node[0]+1,node[1],node[2]),(node[0]-1,node[1],node[2]),(node[0],node[1]+1,node[2]),(node[0],node[1]-1,node[2]),(node[0],node[1],node[2]+1),(node[0],node[1],node[2]-1)]:
                if (0<=i<H and 0<=j<N and 0<=k<M) and L1[i][j][k] == 0:
                    temp.append((i,j,k))
    if boolean:
        result += 1
        queue = deque(temp[:])

for i in L1:
    for j in i:
        for k in j:
            if k == 0:
                print('-1\n')
                exit()
else:
    print(f"{result-1}\n")