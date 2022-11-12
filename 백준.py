import sys, bisect

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
sortedA = [A[0]]
dp = [0 for _ in range(N)]
length = 1

for i, j in zip(A[1:], range(1, N+1)):
    Idx = bisect.bisect_left(sortedA, i)
    if Idx == length:
        sortedA.append(i)
        length += 1
    else:
        sortedA[Idx] = i
    dp[j] = Idx

print(length)