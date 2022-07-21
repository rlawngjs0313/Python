import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P2 = sorted(P)
result = 0
temp = 0

for i in range(len(P2)):
    temp = P2[i] + temp
    result += temp

sys.stdout.write(str(result))