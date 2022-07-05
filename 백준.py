M, N = map(int, input().split())
a = [False] + [True] * (N + 1)
m = int(N**0.5)

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, N + 1, i):
            a[j] = False

for i in range(M, N + 1):
    if i == 1:
        continue
    if a[i] == True:
        print(i)