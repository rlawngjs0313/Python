N = int(input())
L1 = list(map(int, input().split()))
DP = L1[:]

for i in range(N):
    for j in range(i):
        if L1[i] > L1[j]:
            DP[i] = max(DP[j]+L1[i], DP[i])
print(max(DP))