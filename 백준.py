import sys

p = zip(map(int, sys.stdin.readline().split()))

for i, j in p:
    print(i, j)