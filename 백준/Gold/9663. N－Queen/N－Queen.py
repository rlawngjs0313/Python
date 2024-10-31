import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
result = 0

def NQueen(L1,dim):
    global result
    if dim == N:
        result += 1
        return 0
    for i in range(N):
        if L1[i] != '':
            continue
        else:
            A, B = dim-i, dim+i
            for idx,val in enumerate(L1):
                if val == '':
                    continue
                elif val-idx == A:
                    break
                elif val+idx == B:
                    break
            else:
                L1[i] = dim
                NQueen(L1,dim+1)
                L1[i] = ''

NQueen(['' for _ in range(N)],0)
print(f"{result}\n")