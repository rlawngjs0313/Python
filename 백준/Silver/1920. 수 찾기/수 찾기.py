import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = list(map(int,input().split()))
L1.sort()
M = int(input())

for i in list(map(int,input().split())):
    if bisect_left(L1,i) == bisect_right(L1,i):
        print(f'0\n')
    else:
        print(f'1\n')