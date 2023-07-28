A = input()
B = input()
LCS = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

for Bidx, Bvalue in enumerate(B):
    for Aidx, Avalue in enumerate(A):
        if Bvalue == Avalue:
            LCS[Bidx+1][Aidx+1] = LCS[Bidx][Aidx]+1
        else:
            LCS[Bidx+1][Aidx+1] = max(LCS[Bidx][Aidx+1], LCS[Bidx+1][Aidx])
print(LCS[-1][-1])