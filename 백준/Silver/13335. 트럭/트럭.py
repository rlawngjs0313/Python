from collections import deque

n, w, L = map(int, input().split())
L1 = deque([0 for _ in range(w)])
L2 = deque(list(map(int, input().split())))
result = 0

while L2 != deque([]):
    node = L2.popleft()
    L1.popleft()
    if sum(L1)+node > L:
        L1.append(0)
        L2.appendleft(node)
    else:
        L1.append(node)
    result += 1

print(result+w)