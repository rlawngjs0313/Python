N = int(input())
L1 = []
for i in range(N):
    L1.append(list(map(int, input().split())))
L1.sort(key=lambda x: (x[0], x[1]))
for i in L1:
    print(i[0], i[1])