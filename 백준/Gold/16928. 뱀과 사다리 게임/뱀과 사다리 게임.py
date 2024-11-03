import sys
from collections import defaultdict, deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
L1 = [0 for _ in range(101)]
D1 = defaultdict(int)
for _ in range(N+M):
    i,j = map(int, input().split())
    D1[i] = j

queue = deque([1])
cnt = 1
while queue:
    temp = []
    while queue:
        node = queue.popleft()
        if not L1[node]:
            for i in range(node,node+7):
                if i < 101 and not L1[i]:
                    if i == 100:
                        print(f"{cnt}\n")
                        exit()
                    if D1[i] != 0:
                        temp.append(D1[i])
                    else:
                        temp.append(i)
            L1[node] = 1
    if L1[-1] == 0:
        cnt += 1
    queue = deque(temp)

print(f"{cnt}")