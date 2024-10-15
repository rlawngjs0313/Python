import sys

def add (L1:list, result:list):
    while L1[0][1] in result:
        L1.pop(0)
    return L1[0][1]

N = int(input())
L1, L2, L3, L4 = [], [], [], []
result = []

for _ in range(N):
    X, A, B, C, D = map(int, sys.stdin.readline().split())
    L1.append((A, X))
    L2.append((B, X))
    L3.append((C, X))
    L4.append((D, X))

result.append(add(sorted(L1, key=lambda x:(-x[0], x[1])), result))
result.append(add(sorted(L2, key=lambda x:(-x[0], x[1])), result))
result.append(add(sorted(L3, key=lambda x:(-x[0], x[1])), result))
result.append(add(sorted(L4, key=lambda x:(-x[0], x[1])), result))

print(*result)