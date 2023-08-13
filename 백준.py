N = int(input())
Ai = list(map(int, input().split()))

DP = [1 for _ in range(N+1)]
for i in range(N):
    for j in range(i):
        if Ai[i] > Ai[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))