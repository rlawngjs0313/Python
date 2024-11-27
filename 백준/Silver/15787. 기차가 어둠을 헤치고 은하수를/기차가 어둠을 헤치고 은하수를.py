import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int,input().split())
L1 = [0 for _ in range(N)]

for _ in range(M):
    word = list(map(str,input().split()))
    if word[0] == '1':
        L1[int(word[1])-1] |= (1 << int(word[2])-1)
    elif word[0] == '2':
        L1[int(word[1])-1] &= ~(1 << int(word[2])-1)
    elif word[0] == '3':
        L1[int(word[1])-1] <<= 1
        if L1[int(word[1])-1] >= 1048576:
            L1[int(word[1])-1] &= ~(1 << 20)
    else:
        L1[int(word[1])-1] >>= 1

result = []
for i in L1:
    if i not in result:
        result.append(i)

print(F"{len(result)}\n")