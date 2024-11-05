import sys
from itertools import permutations
from collections import defaultdict
input = sys.stdin.readline

M, N = map(int, input().split())
L1 = list(map(int, input().split()))
result = defaultdict(int)

for i in list(permutations(L1,N)):
    result[i] = 1

for i in sorted(list(result.keys())):
    print(*i)