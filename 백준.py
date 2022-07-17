import sys

N = int(input())

for i in range(N):
    data = list(map(str, sys.stdin.readline().rstrip().split()))
    for j in data:
        data = list(map(str, j))
        data.reverse()
        for k in data:
            sys.stdout.write(f"{k}")
        sys.stdout.write(" ")
    sys.stdout.write("\n")