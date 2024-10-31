import sys
from collections import defaultdict, deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
D1 = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    D1[a].append(b)
    D1[b].append(a)

path = [0 for _ in range(N+1)]
queue = deque([])
queue.append(1)

while queue:
    node = queue.popleft()
    for i in D1[node]:
        if path[i] == 0:
            path[i] = node
            queue.append(i)

for i in path[2:]:
    print(f"{i}\n")