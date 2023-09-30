#1475 구현 24:55

from collections import deque

N = input()
L1 = deque([])
for i in N:
    L1.append(i)
result = 0

while L1 != deque([]):
    result += 1
    L2 = [1 for _ in range(10)]
    for _ in range(len(L1)):
        if L2[int(L1[0])] != 0:
            L2[int(L1[0])] -= 1
            L1.popleft()
        elif L1[0] == "6" and L2[9] != 0:
            L1.popleft()
            L2[9] -= 1
        elif L1[0] == "9" and L2[6] != 0:
            L1.popleft()
            L2[6] -= 1
        else:
            temp = L1.popleft()
            L1.append(temp)


print(result)