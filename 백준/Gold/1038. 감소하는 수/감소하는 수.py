N = int(input())
A = 0

while N != 0 and A < 9876543211:
    A += 1
    if 0 < A < 10:
        N -= 1
        continue
    for i in range(len(str(A))-1):
        if str(A)[i] <= str(A)[i+1]:
            C = str(A)
            C = C[:i] + str(int(C[i])+1) + "0"*len(C[i+1:])
            A = int(C)-1
            break
    else:
        N -= 1

if N > 0:
    print(-1)
else:
    print(A)