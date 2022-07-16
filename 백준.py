import sys

N = int(input())
D1 = {}
for i in list(map(int, sys.stdin.readline().split())):
    if i in D1.keys():
        D1[i] += 1
    else:
        D1[i] = 1
M = int(input())
L1 = map(int, sys.stdin.readline().split())
for i in L1:
    if i in D1.keys():
        sys.stdout.write(f"{D1[i]}" + " ")
    else:
        sys.stdout.write("0" + " ")