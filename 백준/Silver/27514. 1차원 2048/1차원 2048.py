from collections import Counter, defaultdict


N = int(input())
L1 = list(map(int, input().split()))
D1 = defaultdict(int)
D1.update(Counter(L1))

for _ in range(N*2):
    for i in list(D1.keys()):
        if i != 0 and D1[i] > 1:
            temp = D1[i]//2
            D1[i*2] += temp
            D1[i] -= temp*2

print(max(D1.keys()))