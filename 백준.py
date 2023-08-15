N = int(input())
DP = [0, 1]

for i in range(N-1):
    DP.append(DP[-1]+DP[-2])

print(DP[-1])