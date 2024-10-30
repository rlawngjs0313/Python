import sys
input = sys.stdin.readline
print = sys.stdout.write

D1 = {'R':'S','S':'P','P':'R'}

t = int(input())

for _ in range(t):
    n = int(input())
    Player1, Player2 = 0, 0
    for _ in range(n):
        a, b = map(str, input().split())
        if D1[a] == b:
            Player1 += 1
        elif D1[b] == a:
            Player2 += 1
    if Player1 == Player2:
        print("TIE\n")
    else:
        print(f'{"Player 1" if Player1 > Player2 else "Player 2"}\n')
    