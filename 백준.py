N = int(input())
L1 = [0] * (N+1)

for i in range(2, N+1):
    L1[i] = L1[i-1] + 1

    if i % 2 == 0:
        L1[i] = min(L1[i], L1[i//2]+1)
    if i % 3 == 0:
        L1[i] = min(L1[i], L1[i//3]+1)

print(L1[N])