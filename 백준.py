import sys

N = int(input())
L1 = []

for i in range(N):
    data = list(map(str, sys.stdin.readline().rstrip().split()))
    if data[0] == 'push':
        L1.append(int(data[1]))
    elif data[0] == "pop":
        if L1 == []:
            print(-1)
        else:
            print(L1.pop(0))
    elif data[0] == "size":
        print(len(L1))
    elif data[0] == "empty":
        if L1 == []:
            print(1)
        else:
            print(0)
    elif data[0] == "front":
        if L1 == []:
            print(-1)
        else:
            print(L1[0])
    elif data[0] == "back":
        if L1 == []:
            print(-1)
        else:
            print(L1[-1])