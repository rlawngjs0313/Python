import sys
from collections import deque
input = sys.stdin.readline()

def BFS(node):
    result = [0]*(100001)
    queue = deque()
    queue.append(node)

    while queue:
        A = queue.popleft()
        if A == K:
            print(result[A])
            break
        for i in (A-1, A+1, 2*A):
            if 0 <= i <= 100000 and not result[i]:
                result[i] = result[A] + 1
                queue.append(i)

N, K = map(int, input.split())
BFS(N)