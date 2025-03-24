import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
L1 = list(map(int,input().split()))
L2 = []
D1 = defaultdict(int)
result = [0 for _ in range(N)]

for i,v in enumerate(reversed(L1)):
    if L2 == [] or v < L2[-1]:
        L2.append(v)
        D1[v] = N-i-1
    elif v > L2[-1]:
        for j in range(len(L2)):
            if v > L2[-1]:
                result[D1[L2[-1]]] = N-i
                L2.pop()
            else:
                break
        L2.append(v)
        D1[v] = N-i-1
print(*result)