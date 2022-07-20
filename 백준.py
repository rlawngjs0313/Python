import sys

S = set()
M = int(sys.stdin.readline())

for i in range(M):
    data = list(sys.stdin.readline().split())
    if data[0] == "add":
        S.add(int(data[1]))
    if data[0] == "remove":
        if int(data[1]) in S:
            S.remove(int(data[1]))
    if data[0] == "check":
        if int(data[1]) in S:
            sys.stdout.write("1" + '\n')
        else:
            sys.stdout.write("0" + '\n')
    if data[0] == "toggle":
        if int(data[1]) in S:
            S.remove(int(data[1]))
        else:
            S.add(int(data[1]))
    if data[0] == "all":
        S = set(range(1, 21))
    if data[0] == "empty":
        S = set()