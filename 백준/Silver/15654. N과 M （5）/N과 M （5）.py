import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int,input().split())
L1 = list(map(int, input().split()))
L1.sort()

for i in permutations(L1,M):
    print(*i)