from collections import defaultdict
import sys

N = int(input())
D1 = defaultdict(int)

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if D1[word[::-1]] != 0:
        print(f"{len(word)} {word[len(word)//2]}")
        exit()
    else:
        D1[word] = 1
    
    if word == word[::-1]:
        print(f"{len(word)} {word[len(word)//2]}")
        exit()
