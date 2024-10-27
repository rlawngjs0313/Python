import sys

N = int(input())
L1 = [[] for _ in range(N)]
if N == 1:
    print(0)
    exit()

for i in range(N):
    for j in sys.stdin.readline().rstrip():
        L1[i].append(j)

for i in range(N):
    for j in range(0,i+1):
        try:
            if L1[i][j] == 'R':
                if L1[i+1][j] == 'R' and L1[i+1][j+1] == 'R':
                    L1[i+1][j], L1[i+1][j+1], L1[i][j] = '', '', ''
                else:
                    exit()
            elif L1[i][j] == 'B':
                if L1[i][j+1] == 'B' and L1[i+1][j+1] == 'B':
                    L1[i][j+1], L1[i+1][j+1], L1[i][j] = '', '', ''
                else:
                    exit()
        except:
            print(0)
            exit()
print(1)