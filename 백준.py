import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())

for i in range(N):
    cnt = 0
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    if n == 0:
        sys.stdin.readline()
        data = []
    else:
        data = list(map(int, sys.stdin.readline().rstrip().rstrip("]").lstrip("[").split(",")))
    for j in p:
        if j == "R":
            cnt += 1
        if j == "D":
            if data == []:
                sys.stdout.write("error" + '\n')
                break
            else:
                if cnt == 0 or cnt % 2 == 0:
                    data.pop(0)
                else:
                    data.pop(-1)
    else:
        if cnt == 0 or cnt % 2 == 0:
            sys.stdout.write(str(data).replace(" ", "") + '\n')
        else:
            sys.stdout.write(str(list(reversed(data))).replace(" ", "") + '\n')