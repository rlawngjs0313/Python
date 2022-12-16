import sys  # 1700번 도전

N, K = map(int, sys.stdin.readline().split())
L1 = list(map(int, sys.stdin.readline().split()))
L2 = set(L1[:N])
result = 0

for i in range(N, K, N):
    temp = set(L1[i:i+N])
    A, B = L2.difference(temp), temp.difference(L2)
    if len(A) != 0 and len(B) != 0:
        result += len(B)
        for j, k in zip(A, B):
            L2.add(k)
            L2.remove(j)

print(result)