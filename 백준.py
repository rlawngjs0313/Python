import sys

N = int(sys.stdin.readline())
L1 = []

for i in range(N):
    L1.append(int(sys.stdin.readline()))

cnt1, location1 = list([0] * -min(L1)), list([0] * -min(L1))
cnt2, location2 = list([0] * (max(L1)+1)), list([0] * (max(L1)+1))

for i in L1:
    if i < 0:
        cnt1[i] += 1
        location1[i] = i
    else:
        cnt2[i] += 1
        location2[i] = i
for i in range(len(cnt2)):
    cnt1.append(cnt2[i])
    location1.append(location2[i])
L1 = []
for i in range(len(cnt1)):
    if cnt1[i] == 0:
        continue
    else:
        for j in range(cnt1[i]):
            L1.append(location1[i])
sys.stdout.write(f"{round(sum(L1)/N)}"+'\n')
sys.stdout.write(f"{L1[int(N/2)]}"+'\n')
n1 = cnt1.index(max(cnt1))
n2 = 0
if cnt1.count(max(cnt1)) == 1:
    n2 = n1
else:
    n2 = cnt1.index(max(cnt1), n1+1)
sys.stdout.write(f"{location1[n2]}"+'\n')
sys.stdout.write(f"{max(L1)-min(L1)}"+'\n')