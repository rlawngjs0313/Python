N = int(input())
L1 = []
result = 1

for _ in range(N):
    L1.append(tuple(map(int, input().split())))
L1 = sorted(L1, key=lambda x:(x[0]))

pick = L1[0]
for i in range(N):
    if pick[0]+pick[1] < L1[i][0]:
        result += 1
    pick = L1[i]

print(result)