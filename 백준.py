import sys
N, M = map(int, input().split())
S1 = set(map(int, sys.stdin.readline().split()))
S2 = set(map(int, sys.stdin.readline().split()))
print(len(S1.symmetric_difference(S2)))