n, m = map(int, input().split())
L1 = [[1]*m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        L1[i][j] = (L1[i-1][j]+L1[i][j-1]+L1[i-1][j-1])%1000000007

print(L1[-1][-1])