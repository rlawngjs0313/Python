import sys
input = sys.stdin.readline
print = sys.stdout.write
 
N = int(input())
L1 = [0]
result = [0]

for _ in range(N):
    word = int(input())
    max_num = []
    for i,v in enumerate(L1):
        if v < word:
            max_num.append(result[i])
    L1.append(word)
    result.append(max(max_num)+word)

print(f"{max(result)}\n")