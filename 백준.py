import sys

word = sys.stdin.readline().rstrip()
S1 = set()
N = len(word)

for i in range(N):
    for j in range(i, N):
        S1.add(word[i:j+1])
print(len(S1))