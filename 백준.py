import sys

T = int(input())

for i in range(T):
    N = int(sys.stdin.readline())
    data = []
    result = 1
    for j in range(N):
        data.append(list(map(int, sys.stdin.readline().split())))
    data.sort(key=lambda x: (x[0]))
    last = 0
    for j in range(N-1):
        if data[j+1][1] < data[last][1]:
            last = j + 1
            result += 1
    print(result)