D1 = {0:10,1:10,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
L1 = []
for i, j in zip(list(map(int, input().split())),['H','T','C','K','G']):
    L1.append([i,j])
M = int(input())

def ten_to_n(n, b):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        n, m = n//b, n%b
        result += str(m)
    return result[::-1]

def add(L1):
    result = 0
    for i in L1:
        result += i[0]
    return result

for _ in range(M):
    jinbup = D1[add(L1)%10]
    for i, v in enumerate(list(map(int, input().split()))):
        L1[i][0] -= v
    print(f"{ten_to_n(add(L1),jinbup)}7H")
    L2 = sorted(L1, key=lambda x:(-x[0],x[1]))
    if add(L1) != 0:
        for i in L2:
            if i[0] != 0:
                print(i[1],end='')
        print('')
    else:
        print('NULL')