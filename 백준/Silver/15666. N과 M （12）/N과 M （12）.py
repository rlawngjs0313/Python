import sys
from itertools import product
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
L1 = list(map(int, input().split()))
result = defaultdict(int)

for i in product(L1, repeat=M):
    for j in range(1,M):
        if i[j-1] > i[j]:
            break
    else:
        result[i] = 1

for i in sorted(list(result.keys())):
    print(*i)