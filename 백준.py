N = int(input())
DP0, DP1 = [0], [1]

for i in range(N-1):
    temp0, temp1 = DP0[-1], DP1[-1]
    DP0.append(temp1+temp0)
    DP1.append(temp0)

print(DP0[-1]+DP1[-1])