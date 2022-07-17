N, K = map(int, input().split())
L1 = list(range(1, N+1))
cnt = 0
result = []

while len(L1) != 0:
    cnt += 1
    if cnt == K:
        cnt = 0
        result.append(L1.pop(0))
    else:
        L1.append(L1.pop(0))

print(str(result).replace('[', '<').replace(']', '>'))