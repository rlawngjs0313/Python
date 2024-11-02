import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = list(map(int, input().split()))
D1 = defaultdict(int)
result = 0

start, end = 0, 0
while end < N:
    if len(D1) < 3:
        D1[L1[end]] += 1
        end += 1
    else:
        D1[L1[start]] -= 1
        if D1[L1[start]] == 0:
            D1.pop(L1[start])
        start += 1
    if len(D1) < 3:
        result = max(result,end-start)
    
print(f"{result}\n")