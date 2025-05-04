N = int(input())
A = list(map(int, input().split()))
AR = A[::-1]

dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
        if AR[i] > AR[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2.reverse()
result = [a+b-1 for a, b in zip(dp1, dp2)]

print(max(result))