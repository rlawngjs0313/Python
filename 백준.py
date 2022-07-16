import sys

N, M = map(int, input().split())
L1 = []
L2 = []
cnt = 0

for i in range(N):
    L1.append(sys.stdin.readline().rstrip())
    
L1.sort(key=len)

for i in range(M):
    L2.append(sys.stdin.readline().rstrip())

def binarySearch(word):
    l = 0
    r = N-1
    while l <= r :
        index = (l+r)//2
        if L1[index] == word:
            return 1
        elif len(L1[index]) > len(word):
            r = index - 1
        elif len(L1[index]) < len(word):
            l = index + 1
        elif len(L1[index]) == len(word):
            if word in L1[l:r+1]:
                return 1
            else:
                return 0
    return 0

for i in L2:
    cnt += binarySearch(i)
print(cnt)