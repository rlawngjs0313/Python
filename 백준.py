import sys

N = int(input())
L1 = [0]
DP = [0 for _ in range(N+1)]

for _ in range(N):
    L1.append(int(sys.stdin.readline()))

if N == 1:
    print(L1[-1])
    exit()

DP[1] = L1[1]
DP[2] = DP[1] + L1[2]

for i in range(3, N+1):
    DP[i] = max(DP[i-3]+L1[i-1], DP[i-2]) + L1[i]

print(DP[-1])