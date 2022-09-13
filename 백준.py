import sys

n = int(sys.stdin.readline())
S = 1
L = 2
cnt = 2
if n < 3:
    sys.stdout.write(str(n))
else:
    while cnt < n:
        S, L = L, S+L
        cnt += 1
    sys.stdout.write(str(L % 10007))