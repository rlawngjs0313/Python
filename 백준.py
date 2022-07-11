import sys
N = int(input())
L1 = set([])
for i in range(N):
    L1.add(sys.stdin.readline().rstrip())
L1 = list(L1)
L1.sort()
L1.sort(key=len)
for i in L1:
    print(i)