N = int(input())
L1 = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(2, L1[i]+1):
        if L1[i] == j:
            cnt += 1
        elif L1[i] % j == 0:
            break
print(cnt)