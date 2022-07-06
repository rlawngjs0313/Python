N = int(input())
L1 = []
result = []
data = tuple(map(int, input().split()))
L1.append(data)
result.append(1)
for i in range(N-1):
    data = tuple(map(int, input().split()))
    L1.append(data)
    result.append(1)
    for j in range(len(L1)-1):
        if L1[j][0] > data[0] and L1[j][1] > data[1]:
            result[-1] += 1
        elif L1[j][0] < data[0] and L1[j][1] < data[1]:
            result[j] += 1
for i in result:
    print(i, end=" ")