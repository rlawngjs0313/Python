import sys

N, S = map(int, sys.stdin.readline().split())
data = list(map(lambda x: abs(x-S), list(map(int, sys.stdin.readline().split()))))

for i in range(len(data)-1):
    m, n = max(data[i], data[i+1]), min(data[i], data[i+1])
    while n != 0:
        temp = m%n
        m, n = n, temp
    data[i+1] = abs(m)
print(data[-1])