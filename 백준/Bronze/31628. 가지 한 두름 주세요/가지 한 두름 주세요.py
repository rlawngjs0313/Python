from collections import defaultdict

L1 = list(list(map(str, input().split())) for _ in range(10))
for i in range(10):
    D1, D2 = defaultdict(int), defaultdict(int)
    for j in range(10):
        D1[L1[i][j]] += 1
        D2[L1[j][i]] += 1
    if len(D1.keys()) == 1 or len(D2.keys()) == 1:
        print(1)
        exit()
else:
    print(0)