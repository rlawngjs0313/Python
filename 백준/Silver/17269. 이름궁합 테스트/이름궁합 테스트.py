N, M = map(int, input().split())
A, B = map(str, input().split())
D1 = {"A":3,"B":2,"C":1,"D":2,"E":4,"F":3,"G":1,"H":3,"I":1,"J":1,"K":3,"L":1,"M":3,"N":2,"O":1,"P":2,"Q":2,"R":2,"S":1,"T":2,"U":1,"V":1,"W":1,"X":2,"Y":2,"Z":1}

result = []
for i,j in zip(A,B):
    result.append(D1[i])
    result.append(D1[j])
if N > M:
    for i in A[M:]:
        result.append(D1[i])
else:
    for i in B[N:]:
        result.append(D1[i])

while len(result) > 2:
    temp = []
    for i in range(len(result)-1):
        temp.append((result[i]+result[i+1])%10)
    result = temp[:]

if result[0] == 0:
    print(f"{result[1]}%")
else:
    print(f"{result[0]}{result[1]}%")