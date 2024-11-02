import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
D1 = defaultdict(int)
for i in range(1,int(n**0.5)+1):
    D1[i*i] = 1
square = list(D1.keys())

if D1[n]:
    print("1\n")
else:
    for i in square:
        if D1[n-i]:
            print('2\n')
            exit()
    else:
        for i in square:
            for j in square:
                if D1[n-i-j]:
                    print('3\n')
                    exit()
    print('4\n')