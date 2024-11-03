import sys
from collections import deque, defaultdict
input = sys.stdin.readline
print = sys.stdout.write

def BFS(A, B):
    queue = deque([(A,'')])
    visited = defaultdict(int)
    
    while queue:
        node, exe = queue.popleft()
        for i,j in [((node*2)%10000,'D'),(node-1 if 0<node else 9999,'S'),(str(node),'L'),(str(node),'R')]:
            if j == 'L':
                i = '0'*(4-len(i))+i
                i = list(i)
                i[:3],i[3] = i[1:],i[0]
                i = int(''.join(i))
            elif j == 'R':
                i = '0'*(4-len(i))+i
                i = list(i)
                i[1:],i[0] = i[:3],i[3]
                i = int(''.join(i))
            if i == B:
                return exe+j
            if visited[i] == 0:
                queue.append((i,exe+j))
                visited[i] = 1

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(f"{BFS(A,B)}\n")