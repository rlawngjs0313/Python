import sys

n = int(input())
data = []

for i in range(n):
    temp = list(map(str, sys.stdin.readline().split()))
    temp[1:] = list(map(int, temp[1:]))
    data.append(temp)

data.sort(key = lambda x : (x[3], x[2], x[1]))
print(data[-1][0])
print(data[0][0])