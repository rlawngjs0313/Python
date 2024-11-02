import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

N, M, B = map(int, input().split())
D1 = defaultdict(int)
for _ in range(N):
    word = list(map(int, input().split()))
    for i in word:
        D1[i] += 1

result = (1e8, 0)
for i in range(257):
    temp_result = [0,0]
    for j in D1.keys():
        if i > j:
            temp_result[1] += (i-j)*D1[j]
            temp_result[0] += (i-j)*D1[j]
        elif i < j:
            temp_result[1] -= (j-i)*D1[j]
            temp_result[0] += 2*(j-i)*D1[j]
    if temp_result[1] <= B:
        result = min(result, (temp_result[0],i), key=lambda x:(x[0],-x[1]))

print(f"{result[0]} {result[1]}")