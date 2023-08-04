import sys

N, K = map(int, input().split())
DP = [0 for _ in range(K+1)]

for _ in range(N):
    value = int(sys.stdin.readline())
    for i in range(K+1):
        if i-value == 0:
            DP[i] += 1
        elif i-value > 0:
            DP[i] += DP[i-value]
print(DP[-1])