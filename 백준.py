from collections import deque
import sys

data = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline())
L1 = data
L2 = deque([])

for i in range(N):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == "L":
        if L1 == []:
            continue
        L2.appendleft(L1.pop())
        continue
    if cmd[0] == "D":
        if L2 == deque():
            continue
        L1.append(L2.popleft())
        continue
    if cmd[0] == "B":
        if L1 == []:
            continue
        L1.pop()
        continue
    if cmd[0] == "P":
        L1.append(cmd[1])
        continue
L1.append(list(L2))
L1 = str(L1).replace("[", "").replace("]", "").replace("'", "").replace(", ", "")
sys.stdout.write(L1)