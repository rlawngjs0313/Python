import sys
sys.setrecursionlimit(100000)

G = int(input())
P = int(input())
L1 = list(range(G+1))
result = 0

def find(n):
    if L1[n] != n:
        L1[n] = find(L1[n])
    else:
        L1[n] -= 1
    return L1[n]

for i in range(P):
    data = int(sys.stdin.readline())
    if find(data) == -1:
        print(result)
        exit()
    result += 1

print(result)