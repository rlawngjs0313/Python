N = int(input())
L1 = sorted(list(map(int, input().split())))
result = 0

for i in range(len(L1)):
    s, e = i, N
    while s < e:
        m = (s+e) // 2
        if L1[i] >= 0.9*L1[m]:
            s = m+1
        else:
            e = m
    result += e-i-1

print(result)