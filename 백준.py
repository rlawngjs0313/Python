import sys

N = int(input())
L1 = []

for _ in range(N):
    L1.append(list(map(int, sys.stdin.readline().split())))

DP = [0 for _ in range(N+1)]
for i in range(N+1):
    for j in range(i+L1[i][0], N+1):
        if DP[j] < DP[i] + L1[i][1]:
            DP[j] = DP[i] + L1[i][1]

print(DP[-1])