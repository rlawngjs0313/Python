import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int,input().split())
L1 = list(range(1,N+1))

for _ in range(K):
    A,B,C = map(int,input().split())
    temp = L1[A-1:B]
    L1 = L1[:A-1]+L1[B:]
    if C == 0:
        L1 = temp+L1
    else:
        L1 = L1[:C]+temp+L1[C:]

for i in range(10):
    print(F"{L1[i]}\n")