import sys

T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    if (x1, y1) == (x2, y2) and r1 == r2:
        if r1 == 0:
            sys.stdout.write("1" + '\n')
        else:
            sys.stdout.write("-1" + '\n')
    elif d > r1+r2 or d < abs(r1-r2):
        sys.stdout.write("0" + '\n')
    elif d == (r1+r2) or d == (abs(r1-r2)):
        sys.stdout.write("1" + '\n')
    elif d < r1+r2 or d > abs(r1-r2):
        sys.stdout.write("2" + '\n')