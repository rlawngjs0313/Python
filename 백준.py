M = int(input())
N = int(input())
L1 = []
for i in range(M, N+1):
    for j in range(2, i+1):
        if i == j:
            L1.append(i)
        elif i % j == 0:
            break
if L1 == []:
    print(-1)
else:
    print(sum(L1))
    print(min(L1))