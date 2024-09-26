import sys

H, M = map(int, input().split(":"))
L1 = list(map(int, input().split()))
L = int(input())
result = 0
for _ in range(L):
    T, cmd = map(str, sys.stdin.readline().split())
    if cmd == "^":
        L1[H//2] = 0
    elif cmd == "10MIN":
        M += 10
    elif cmd == "30MIN":
        M += 30
    elif cmd == "50MIN":
        M += 50
    elif cmd == "2HOUR":
        H += 2
    elif cmd == "4HOUR":
        H += 4
    elif cmd == "9HOUR":
        H += 9
    H += M//60
    M = M%60
    H %= 12
    if L1 == [0,0,0,0,0,0]:
        print(0)
        exit()

print(sum(L1) if sum(L1) <= 100 else 100)