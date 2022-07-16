import sys

N = int(sys.stdin.readline())
St1 = []

for i in range(N):
    data = list(sys.stdin.readline().split())
    if data[0] == "push":
        St1.append(data[1])
    elif data[0] == "pop":
        if len(St1) == 0:
            print(-1)
        else:
            print(St1.pop())
    elif data[0] == "size":
        print(len(St1))
    elif data[0] == "empty":
        if len(St1) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == "top":
        if len(St1) == 0:
            print(-1)
        else:
            print(St1[-1])