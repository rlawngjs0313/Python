N = int(input())
L1 = list(map(int, input().split()))
DP = [L1[0]]

for i in L1[1:]:
    DP.append(max(DP[-1]+i, i))

print(max(DP))