import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
D1 = defaultdict(int)

result = 0
for _ in range(N):
    a,b,c = map(int,input().split())
    if D1[a] != 0:
        D1[b] = D1[a]
        D1[c] = D1[a]
    elif D1[b] != 0:
        D1[a] = D1[b]
        D1[c] = D1[b]
    elif D1[c] != 0:
        D1[a] = D1[c]
        D1[b] = D1[c]
    else:
        result += 1
        D1[a] = result
        D1[b] = result
        D1[c] = result

print(f"{result}\n")