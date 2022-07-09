import sys

N = int(input())
L1 = [0]*10000
cnt = [0]*10000

for i in range(N):
    data = int(sys.stdin.readline())
    L1[data-1] = data
    cnt[data-1] += 1
for i in range(len(cnt)):
    if cnt[i] == 0:
        continue
    else:
        for j in range(cnt[i]):
            sys.stdout.write(str(L1[i])+'\n')