import sys
input = sys.stdin.readline

N = int(input())
L1 = list(map(int, input().split()))
D1 = {}
for i in L1:
    D1[i] = 2
res = []

def BF(queue:dict,result:list):
    global res
    if len(result) == 2*N:
        res.append(result)
    temp = queue.copy()
    for i in queue.keys():
        if temp[i] == 0 or (i in result and abs(result.index(i)-(len(result)-1)) != i):
            continue
        temp[i] -= 1
        BF(temp,result+[i])
        temp[i] += 1

BF(D1,[])
res = sorted(res)
if len(res) != 0:
    print(*res[0])
else:
    print('-1')