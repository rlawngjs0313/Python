import sys
input = sys.stdin.readline

N = int(input())
L1 = list(map(int,input().split()))
L2 = []
result = [-1 for _ in range(N)]

for i,v in enumerate(L1[::-1]):
    if len(L2) == 0:
        L2.append(v)
        continue
    elif v >= L2[-1]:
        while len(L2) != 0 and v >= L2[-1]:
            L2.pop()
    if len(L2) == 0:
        L2.append(v)
        continue
    result[i] = L2[-1]
    L2.append(v)

print(*reversed(result))