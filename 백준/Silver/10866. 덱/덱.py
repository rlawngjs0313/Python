import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = deque([])

for _ in range(N):
    word = list(map(str,input().split()))
    if word[0] == "push_front":
        L1.appendleft(word[1])
    elif word[0] == "push_back":
        L1.append(word[1])
    elif word[0] == "pop_front":
        if len(L1) == 0:
            print(f"-1\n")
        else:
            print(f'{L1.popleft()}\n')
    elif word[0] == "pop_back":
        if len(L1) == 0:
            print(f'-1\n')
        else:
            print(f'{L1.pop()}\n')
    elif word[0] == "size":
        print(f'{len(L1)}\n')
    elif word[0] == "empty":
        if len(L1) == 0:
            print(f'1\n')
        else:
            print(f'0\n')
    elif word[0] == "front":
        if len(L1) == 0:
            print(f'-1\n')
        else:
            print(f'{L1[0]}\n')
    elif word[0] == "back":
        if len(L1) == 0:
            print(f'-1\n')
        else:
            print(f'{L1[-1]}\n')