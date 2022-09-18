import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
max = data[0]

for i in range(1, N):
    if (max + data[0]) >= data[i]:
        max += data[0]
    else:
        max = data[i]

print(max)