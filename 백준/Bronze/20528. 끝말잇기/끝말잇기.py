import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = list(map(str,input().split()))

word = L1[0][0]
for i in L1:
    if i[0] != word:
        print('0\n')
        exit()
else:
    print('1\n')