import sys
from collections import Counter

T = int(input())
for _ in range(T):
    S1, S2 = map(str, sys.stdin.readline().split())
    if Counter(S1) != Counter(S2):
        print(f"{S1} & {S2} are NOT anagrams.")
    else:
        print(f"{S1} & {S2} are anagrams.")