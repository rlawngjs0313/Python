import sys
input = sys.stdin.readline

N = int(input())
L1 = list(map(int,input().split()))

def BF(result,queue):
    if len(queue) == 0:
        print(*result)
        exit()
    for i in range(len(queue)):
        if (result[-1]%3 == 0 and result[-1]//3 == queue[i]) or result[-1]*2 == queue[i]:
            BF(result+[queue[i]],queue[:i]+queue[i+1:])

for i in range(N):
    BF([L1[i]],L1[:i]+L1[i+1:])