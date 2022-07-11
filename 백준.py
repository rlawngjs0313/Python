import sys
N = int(sys.stdin.readline())
L1 = list(map(int, sys.stdin.readline().rstrip().split()))
D1 = {}
L2 = sorted(list(set(L1)))
for i in range(len(L2)):
    D1[L2[i]] = i

for i in L1:
    sys.stdout.write(str(D1[i])+' ')