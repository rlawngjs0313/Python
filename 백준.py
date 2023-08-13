import sys
N = int(input())

DP1 = [0, 0, 0]
DP2 = [0, 0, 0]
for i in range(N):
    R, G, B = map(int, sys.stdin.readline().split())
    DP2[0] = min(R+DP1[1], R+DP1[2])
    DP2[1] = min(G+DP1[0], G+DP1[2])
    DP2[2] = min(B+DP1[0], B+DP1[1])
    if i != N-1:
        DP1[:] = DP2[:]
print(min(DP2))