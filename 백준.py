import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
result = [-1] * N
L1 = []

for i in range(len(data)-1):
    if data[i] < data[i+1]:
        result[i] = data[i+1]
        while L1:
            index = L1.pop()
            if data[index] < data[i+1]:
                result[index] = data[i+1]
            else:
                L1.append(index)
                break
    else:
        L1.append(i)
print(*result)