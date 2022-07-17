import sys
N = int(sys.stdin.readline())
L1 = []
bl = False

for i in range(N):
    data = sys.stdin.readline().rstrip()
    for j in data:
        if j == "(":
            L1.append(1)
        elif j == ")":
            if L1 == []:
                sys.stdout.write("NO" + "\n")
                bl = True
                break
            else:
                L1.pop()
    if bl:
        L1 = []
        bl = False
        continue
    if L1 == []:
        sys.stdout.write("YES" + "\n")
    else:
        sys.stdout.write("NO" + "\n")
    L1 = []
    bl = False