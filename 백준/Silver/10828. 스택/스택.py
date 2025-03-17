import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = []
for _ in range(N):
    word = list(map(str,input().split()))
    if word[0] == 'push':
        L1.append(word[1])
    elif word[0] == 'pop':
        if len(L1) != 0:
            print(f"{L1.pop()}\n")
        else:
            print('-1\n')
    elif word[0] == 'size':
        print(f"{len(L1)}\n")
    elif word[0] == 'empty':
        if len(L1) == 0:
            print('1\n')
        else:
            print('0\n')
    elif word[0] == 'top':
        if len(L1) != 0:
            print(f"{L1[-1]}\n")
        else:
            print('-1\n')