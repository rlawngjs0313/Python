A = input()
if int(A) < 10:
    A = list(A)
    A.append(0)
    A.reverse()
B = [0, 0]
C = []
B[0], B[1] = int(A[1]), int(A[0])+int(A[1])
k = 1
while int(A[0]) != B[0] or int(A[1]) != B[1]:
    k += 1
    for i in str(B[0]+B[1]):
        C.append(i)
    B[0], B[1] = B[1], int(C[-1])
    C = []
print(k)