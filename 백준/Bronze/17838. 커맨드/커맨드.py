import sys
from collections import Counter
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    word = input().rstrip()
    if len(word) > 7:
        print("0\n")
        continue
    if len(Counter(word).keys()) != 2:
        print("0\n")
        continue
    A,B = list(Counter(word).keys())[0], list(Counter(word).keys())[1]
    S1,S2 = f'{A}{A}{B}{B}{A}{B}{B}',f'{B}{B}{A}{A}{B}{A}{A}'
    if word != S1 and word != S2:
        print("0\n")
        continue
    print("1\n")